import numpy as np
from scipy.linalg import block_diag
import matplotlib.pyplot as plt
import time

st = time.time()

# Adjacency matrix of the graph network
Adj = np.array([
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0]
])

Din = np.array([
    [1, 0, 0, 0],   
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 1]
])

# Adj = np.array([
#     [0, 1, 1, 1],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0]
# ])

# Adj = Adj.T
# Adj = np.array([
#     [0, 1, 1, 1],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0]
# ])


# Indegree matrix of the graph network

#Unbalanced:

Adj = np.array([
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]
])

Din = np.array([
    [1, 0, 0, 0],
    [0, 3, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

n = len(Adj)


# Identity matrices
I1 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

I2 = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

# Matrix A and vector b for each node
A1 = np.array([[5, 0, 2, 3], [5, 2, 2, 6], [3, 4, 5, 8], [0, 5, 4, 2], [8, 2, 2, 0]])
A2 = np.array([[6, 1, 6, 4], [4, 0, 4, 2], [1, 0, 3, 6], [0, 0, 0, 1], [4, 1, 2, 3]])
A3 = np.array([[2, 1, 0, 3], [6, 2, 3, 5], [1, 4, 6, 0], [2, 3, 2, 2], [0, 3, 1, 0]])
A4 = np.array([[-6, 2, 0, -5], [-8, -1, -2, -5], [0, -4, -6, -6], [1, -2, -1, -3], [-4, 0, -3, 2]])

# A1 = np.array( [[4, 5, -5, -5], [-1, 2, -3, -5], [-1, -4, -1, -1], [-2, -5, 0, 2], [-4, 3, 4, -4]] )
# A2 = np.array( [[-5, 3, 5, 4], [0, -4, 0, 4], [3, 3, 4, -1], [-5, -4, 5, -2], [-4, -2, 2, 3]] )
# A3 = np.array( [[-1, 0, 1, -5], [1, 3, -4, -1], [-2, 3, 3, 2], [-2, 4, -5, 2], [-1, 5, 0, 5]] )
# A4 = np.array( [[7, -7, 1, 15], [2, -1, 8, 5], [9, 8, -4, 1], [10, 12, 6, 2], [11, -2, 2, -3]] )

b1 = np.array([[61], [51], [1], [55], [1]])
b2 = np.array([[112], [11], [2], [80], [1]])
b3 = np.array([[57], [38], [100], [58], [53]])
b4 = np.array([[-117], [-4], [6], [-107], [12]])

p = len(A1)
q = len(A1[0])

# Compute Asum and bsum
Asum = A1 + A2 + A3 + A4
bsum = b1 + b2 + b3 + b4
p = len(A1)
q = len(A1[0])
print("Sum(Ai):")
print(Asum)
print("Sum(bi):")
print(bsum)

# Laplacian computation
L = Din - Adj
print(L)
LL = np.kron(L, I1)
LL1 = np.kron(L, I2)

# Initialize solution vectors
x = np.array([[0]] * (n * len(A1[0])))
ld = x

v = np.array([[5]] * (n * len(A1[0])))

v_dash = np.array([[5]] * (n * len(A1)))


# Block diagonal matrix A and concatenated vector b
A = block_diag(A1, A2, A3, A4)
b = np.concatenate([b1, b2, b3, b4])
y = -1 * b

# print(LL1)
# print(y)
# Step sizes
alpha, beta = 25, 5e-2
delta = 1e-3
iterations = 300000
times=[0]
frac_change = 5e-1
update_duration = 10
# Iterative upates

# print(LL)
# print(np.linalg.det(LL))
# LL_inv = np.linalg.inv(LL)
# print(np.dot(LL,LL_inv))

oe = np.array([[1]]*q)
ol = np.array([[1]]*p)
#print(oe)
one = np.kron(oe,I2)
o_ = np.kron(ol,I2)
#print(one)

# v_vect = np.array([
#     [0.8660254037844387],
#     [0.2886751345948129],
#     [0.28867513459481287],
#     [0.2886751345948129]
# ])

# v_vect = np.array([
#     [3],
#     [1],
#     [1],
#     [1]
# ])

# # v_vect = np.array([
# #     [1],
# #     [1],
# #     [1],
# #     [1]
# # ])

# print("------",np.dot(L,v_vect))

# v_k = np.kron(v_vect,oe)
# V = np.diag(v_k.flatten())

# v_k1 = np.kron(v_vect,ol)
# V1 = np.diag(v_k1.flatten())

cap = 1000

xvals = [x.tolist()]
sol, residuals, rank, s = np.linalg.lstsq(Asum, bsum, rcond=None)
sols = [sol.tolist()]
print(sol.T)

for i in range(iterations):
    #x_change = (-1 * alpha) * np.dot(LL, ld) - (n * beta) * np.dot(A.T, y)
    # AT = np.dot(A.T,one)
    # axb = np.dot(A,x) - b
    # ot = np.dot(one.T,axb)
    # x_change = (-1 * alpha) * np.dot(LL, ld) - (beta)*np.dot(AT,ot)
    #x_change = (-1 * alpha) * np.dot(LL, ld) -(beta)*(np.dot(np.dot(A.T,one),np.dot(one.T,(np.dot(A,x)-b))))
    #x_change =  -1*np.dot(LL, ld) - (2)*(np.dot(np.dot(A.T,one),np.dot(one.T,(np.dot(A,x)-b)))) - alpha*np.dot(LL, x)
    
    V = np.diag(v.flatten())
    V_dash = np.diag(v_dash.flatten())
    x_change =  -1*np.dot(np.dot(LL,V), ld) - (2*n*beta)*(np.dot(A.T,y)) - alpha*np.dot(np.dot(LL,V), x)
    l_change =  np.dot(np.dot(LL,V), x)
    y_change = -1*np.dot(np.dot(LL1,V_dash),y) + np.dot(A,-1*np.dot(np.dot(LL,V), ld) - (2*n*beta)*(np.dot(A.T,y)) - alpha*np.dot(np.dot(LL,V), x))
    v_change = -np.dot(LL,v)
    v_dash_change = -np.dot(LL1,v_dash)
    #print(np.dot(LL1,y).shape,(alpha*np.dot(LL, x)).shape,y_change.shape)
    # print(-1*np.dot(LL, ld))
    # print((2*n*beta)*(np.dot(A.T,y)))
    # print(alpha*np.dot(LL, x))
    
    #y_change = (-1 * alpha) * np.dot(A, np.dot(LL, ld)) - (n * beta) * np.dot(np.dot(A, A.T), y) - (gamma) * (np.dot(LL1, y))
    
    # print("-----",y[0:5])
    # print("-------------",-1*np.dot(LL1,y))
    
    # print(i)
    # print("x up",x_change[0:4])
    # print("y up",y_change[0:5])
    # print("ld up",l_change[0:4])
    # print("gap")
    # print("norm",np.dot(A,- (2*n*beta)*(np.dot(A.T,y)))[0:5])
    # print("v1",-1*np.dot(LL1,y)[0:5])
    # print("v2",-1*np.dot(A,- alpha*np.dot(LL, x))[0:5])
    # print("v3",np.dot(A,-1*np.dot(LL, ld))[0:5])
    
    
    x = x + delta * x_change
    ld = ld + delta * l_change
    y = y + delta * y_change
    v = v + delta * v_change
    v_dash = v_dash + delta * v_dash_change
    
    
    # print(i)
    #print(x.T)
    # print(ld.T)
    # print(y.T)
    
    # if(i==100000):
    #     A1 = np.array( [[4, 5, -5, -5], [-1, 2, -3, -5], [-1, -4, -1, -1], [-2, -5, 0, 2], [-4, 3, 4, -4]] )
    #     A2 = np.array( [[-5, 3, 5, 4], [0, -4, 0, 4], [3, 3, 4, -1], [-5, -4, 5, -2], [-4, -2, 2, 3]] )
    #     A3 = np.array( [[-1, 0, 1, -5], [1, 3, -4, -1], [-2, 3, 3, 2], [-2, 4, -5, 2], [-1, 5, 0, 5]] )
    #     A4 = np.array( [[7, -7, 1, 15], [2, -1, 8, 5], [9, 8, -4, 1], [10, 12, 6, 2], [11, -2, 2, -3]] )
    #     A = block_diag(A1, A2, A3, A4)
    #     print(A1+A2+A3+A4)
    #     b1 = np.array( [[7], [11], [4], [3], [1]] )
    #     b2 = np.array( [[3], [-4], [13], [15], [6]] )
    #     b3 = np.array( [[6], [5], [-5], [7], [-2]] )
    #     b4 = np.array( [[-6], [60], [39], [-5], [97]] )
    #     b = np.concatenate([b1, b2, b3, b4])    
    #     print(b1+b2+b3+b4)
    #     y = np.dot(A,x)-1 * b
        # x = np.array([[0]] * (n * len(A1[0])))
        # ld = np.array([[0]] * (n * len(A1[0])))
        # print(y)
        
    
    # if(i==100000):
        # Adj = np.array([
        #     [0, 1, 0, 1],
        #     [0, 0, 1, 0],
        #     [1, 1, 0, 1],
        #     [0, 0, 1, 0]
        # ])

        # Din = np.array([
        #     [1, 0, 0, 0],   
        #     [0, 2, 0, 0],
        #     [0, 0, 2, 0],
        #     [0, 0, 0, 2]
        # ])
        # L = Din - Adj
        # print(L)
        # LL = np.kron(L, I1)
        # LL1 = np.kron(L, I2)
    
    if(i==0):
        # A1_ = A1
        # A2_ = A2
        # A3_ = A3
        # A4_ = A4
        b1_ = b1
        b2_ = b2
        b3_ = b3
        b4_ = b4
    
    if(i%update_duration==0 and i<=200000):
        # A1_ = frac_change*A1+A1_
        # A2_ = frac_change*A2+A2_
        # A3_ = frac_change*A3+A3_
        # A4_ = frac_change*A4+A4_
        # fin_A = A1_ + A2_ + A3_ + A4_
        # A = block_diag(A1_,A2_,A3_,A4_)
        b1_ = frac_change*b1+b1_
        b2_ = frac_change*b2+b2_
        b3_ = frac_change*b3+b3_
        b4_ = frac_change*b4+b4_
        b = np.concatenate([b1_, b2_, b3_, b4_])    
        fin_b = b1_+b2_+b3_+b4_
        y = np.dot(A,x)-1 * b 
        
        
    if (i%cap==0):
        times += [i+1]
        xvals += [x.tolist()]
        sol, residuals, rank, s = np.linalg.lstsq(Asum, fin_b, rcond=None)
        sols += [sol.tolist()]
        # print(sol.T)
        # print(i)
        
    
# print(fin_A)
# print(sols)


x1 = []
x2 = []
x3 = []
x4 = []
s1 = []
s2 = []
s3 = []
s4 = []

j=0



for i in range(0,iterations//cap+1):
    x1+=xvals[i][j]
    x2+=xvals[i][j+1]
    x3+=xvals[i][j+2]
    x4+=xvals[i][j+3]
    s1+=sols[i][j]
    s2+=sols[i][j+1]
    s3+=sols[i][j+2]
    s4+=sols[i][j+3]
    
    

print("___________________________")

#print(time,x1)

#print(x.T, "X \n")
#print(y.T, "Y \n")
#print(ld.T, "Ld \n")

for i in range(0,n):
    print(f"Node {i+1} has values:",x[i*q:i*q+q].T)
    # print(f"V_vector of Node {i+1}:",v[i*q:i*q+q].T)
    
residual = np.dot(np.dot((np.dot(A,x)-b).T,one),np.dot(one.T,np.dot(A,x)-b))

print(residual[0][0]**(0.5))
    
end_t = time.time()

print("Time taken:",end_t-st)
    
plt.plot(times,x1,label=f'v1')
plt.plot(times,x2,label=f'v2')
plt.plot(times,x3,label=f'v3')
plt.plot(times,x4,label=f'v4')
plt.plot(times,s1,linestyle='--',label=f's1')
plt.plot(times,s2,linestyle='--',label=f's2')
plt.plot(times,s3,linestyle='--',label=f's3')
plt.plot(times,s4,linestyle='--',label=f's4')



plt.xlabel('Iterations')
plt.ylabel('Values')
plt.title(f'Change in values of node_{int((j+4)/4)}')
plt.legend()
plt.grid(True)
#plt.xscale("log")
plt.show()


