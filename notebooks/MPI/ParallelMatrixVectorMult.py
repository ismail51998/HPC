#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:20:22 2020

@author: kissami
"""
import numpy as np
from scipy.sparse import lil_matrix
from numpy.random import rand, seed
from numba import njit
from mpi4py import MPI


''' This program compute parallel csc matrix vector multiplication using mpi '''

COMM = MPI.COMM_WORLD
nb = COMM.Get_size()
RANK = COMM.Get_rank()

seed(42)

def matrixVectorMult(A, b, x):
   
    row, col = A.shape
    for i in range(row):
        a = A[i]
        for j in range(col):
            x[i] += a[j] * b[j]

    return 0

########################initialize matrix A and vector b ######################
#matrix sizes
SIZE = 1000
Local_size = int(SIZE/nb)

# counts = block of each proc
#counts =

if RANK == 0:
    A = lil_matrix((SIZE, SIZE))
    A[0, :100] = rand(100)
    A[1, 100:200] = A[0, :100]
    A.setdiag(rand(SIZE))
    A = A.toarray()
    b = rand(SIZE)
else :
    A = None
    b = None



#########Send b to all procs and scatter A (each proc has its own local matrix) #####
LocalMatrix = np.zeros(Local_size*SIZE)
# create sendcount and displacment
sendcount = [Local_size*SIZE for i in range(nb)]
displacement = [i*Local_size*SIZE for i in range(nb)]

# Scatter the matrix A
b = COMM.bcast(b ,root=0)
COMM.Scatterv([A,tuple(sendcount),tuple(displacement),MPI.DOUBLE],LocalMatrix,root=0)
#####################Compute A*b locally#######################################
LocalX = np.zeros(Local_size)

start = MPI.Wtime()
matrixVectorMult(LocalMatrix.reshape(Local_size,SIZE), b, LocalX)
stop = MPI.Wtime()
if RANK == 0:
    print("CPU time of parallel multiplication is ", (stop - start)*1000)

##################Gather the results ###########################################
# sendcouns = local size of result
sendcounts = np.array(COMM.gather(len(LocalX),root=0))
if RANK == 0:
    X = np.empty(sum(sendcounts))
else:
    X = None

# Gather the result into X
COMM.Gatherv(sendbuf=LocalX, recvbuf=( X , sendcounts ) , root=0 )

##################Print the results ###########################################

if RANK == 0 :
    X_ = A.dot(b)
    print("The result of A*b using dot is :", np.max(X_ - X))
    print("The result of A*b using parallel version is :", X)
   