#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:39:30 2021

@author: um6p
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:09:22 2020

@author: kissami
"""
# integration numerique par la methode des rectangles avec alpha = a

import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI
COMM=MPI.COMM_WORLD
SIZE= COMM.Get_size()
RANK = COMM.Get_rank()
#print("process {RANK} on {SIZE}".format(RANK=RANK,SIZE=SIZE))


def compute_integrale_rectangle(h, y,deb,nbi):
    
    integrale =0.
    for i in range(deb,nbi):
        integrale = integrale + y[i]*(h)
        
    return integrale
    
def plot_integrale(x, y, nbi):
  
    for i in range(nbi):
        # dessin du rectangle
        x_rect = [x[i], x[i], x[i+1], x[i+1], x[i]] # abscisses des sommets
        y_rect = [0   , y[i], y[i]  , 0     , 0   ] # ordonnees des sommets
        plt.plot(x_rect, y_rect,"r")

xmin = 0
xmax = 3*np.pi/2
nbx = 21
nbi = nbx - 1 # nombre d'intervalles
d=SIZE/(RANK+1)
nbp=int(nbi/d)
deb=int((RANK*nbi)/SIZE)
h=(xmax-xmin)/nbx
x = np.linspace(xmin, xmax, nbx)
y = np.cos(x)


res = compute_integrale_rectangle(h, y,deb ,nbp)
print("process {RANK} on {SIZE}".format(RANK=RANK,SIZE=res))
integrale=COMM.reduce(res,op=MPI.SUM,root=0)
if RANK==0:
    plot_integrale(x, y, nbi)   
    plt.plot(x,y,"bo-")
    print("integrale =", integrale)
    
    plt.show()

