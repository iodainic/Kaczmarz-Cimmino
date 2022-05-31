import numpy as np
import numpy.linalg as la
import time
import random

def cyclic_kaczmarz(A, b, m, n, N):
    x = np.zeros((N+1,n))
    tic = time.time()
    for k in range(N):
        i = k % m
        x[k+1] = x[k] + ((b[i] - np.dot(A[i], x[k]))/la.norm(A[i])**2)*A[i]
    t = time.time()-tic
    return x, t

def randomized_kaczmarz(A, b, m, n, N):
    x = np.zeros((N+1,n))
    tic = time.time()
    norms = la.norm(A, axis = 1)
    for k in range(N):
        i = random.choices(list(range(m)), weights = norms, k=1)
        x[k+1] = x[k] + ((b[i] - np.dot(A[i], x[k]))/la.norm(A[i])**2)*A[i]
    t = time.time()-tic
    return x, t

def Cimmino(A, b, m, n, N):
    x = np.zeros((N+1,n))
    tic = time.time()
    M = np.diag(1/(m*(la.norm(A, axis = 1)**2)))
    for k in range(N):
         x[k+1] = x[k] + np.matmul(np.matmul(A.T,M),(b-np.matmul(A,x[k])))
    t = time.time()-tic
    return x, t