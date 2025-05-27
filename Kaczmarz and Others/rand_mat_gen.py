import numpy as np
import matplotlib.pyplot as plt
import math
import random

a = np.array([
    [1,7,5,6,4],
    [7,5,4,6,1],
    [2,4,7,2,1],
    [4,5,9,1,3],
    [5,1,7,2,3],
    [1,1,1,1,1],
    [3,7,3,7,3]
])

b = np.array([[10],[7],[6],[14],[-10],[15],[8]])

n = 6
p = len(a)
q = len(a[0])

A = []
B = []

#print([0]*p)
A_sum = np.array([([0]*q)]*p)
B_sum = np.array([[0]]*p)

for i in range(0,n-1):
    temp = np.array([([0]*q)]*p)
    t2 = np.array([[0]]*p)
    for j in range(0,p):
        for k in range(0,q):
            temp[j][k] = random.randint(-5,5)
        t2[j][0] = random.randint(-5,15)
    A_sum += temp
    B_sum += t2
    A.append(temp)
    B.append(t2)

A.append(a-A_sum)
B.append(b-B_sum)

for i in range(0,n):
    print(f"A{i+1} = np.array(",A[i].tolist(),")")
    
print(" ")
    
for i in range(0,n):
    print(f"b{i+1} = np.array(",B[i].tolist(),")")