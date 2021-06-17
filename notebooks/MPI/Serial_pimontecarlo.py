import numpy as np
import random 
import timeit
import matplotlib.pyplot as plt
from mpi4py import MPI
COMM=MPI.COMM_WORLD
SIZE= COMM.Get_size()
RANK = COMM.Get_rank()
INTERVAL= 1000

random.seed(42*RANK)  

def compute_points(T):
    #random.seed(42)  
    
    circle_points= 0

    # Total Random numbers generated= possible x 
    # values* possible y values 
    for i in range(T**2): 
      
        # Randomly generated x and y values from a 
        # uniform distribution 
        # Rannge of x and y values is -1 to 1 
        
        
        rand_x= random.uniform(-1, 1) 
        rand_y= random.uniform(-1, 1) 
      
        # Distance between (x, y) from the origin 
        origin_dist= rand_x**2 + rand_y**2
      
        # Checking if (x, y) lies inside the circle 
        if origin_dist<= 1: 
            circle_points+= 1
      
        # Estimating value of pi, 
        # pi= 4*(no. of points generated inside the  
        # circle)/ (no. of points generated inside the square) 
    
     
    
    return circle_points
d=int(INTERVAL/SIZE)
v=COMM.reduce(compute_points(d),op=MPI.SUM,root=0)
v2=COMM.reduce(d**2,op=MPI.SUM,root=0)
if RANK==0:
    
    start = timeit.default_timer()
#circle_points = compute_points(1000)
    end = timeit.default_timer()
    pi = 4* (v/v2) 
    print("Circle points number :",v)
    print("Final Estimation of Pi=", pi, "cpu time :",end-start) 