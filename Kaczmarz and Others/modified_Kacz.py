import numpy as np
import matplotlib.pyplot as plt
import math

a = np.array([[5,4,3,2],[6,5,3,1],[7,3,2,1],[6,5,2,1],[9,12,15,18]])
b = np.array([36,38,28,33,45])

a = np.array([
    [7, 4, 8, 5],
    [7, 3, 7, 8],
    [5, 4, 8, 8],
    [3, 6, 5, 2],
    [8, 6, 2, 5]
])
b = np.array([113, 96, 109, 86, 67])

m = len(b)
n = len(a[0])
iter = [0]
z = b

x = np.array([0]*n)
x_list = []
for i in range(0,n):
    x_list.append(list([0]))

for k in range(0,1600):
    i = (k)%m
    j = (k)%n
    norm_squared = np.dot(a[i],a[i])
    if(norm_squared!=0):
        lam = 1
        column = (a[:,j:j+1].T)[0]
        alter_norm = np.dot(column,column)
        znew = z - (np.dot(column,z)/alter_norm)*column
        xnew = x + (lam)*((b[i]-znew[i]-np.dot(a[i],x))/norm_squared)*(a[i].T)
        z = znew
        
    else:
        xnew = x
    x = xnew
    if(k%m==m-1):
        print(f"{(k+1)/m}th iteration:",x)
        iter.append((k+1)/m)
        for u in range(0,n):
            x_list[u].append(float(x[u]))
    
y = np.dot(a,x) - b
#print(y)
residual = 0
for u in y:
    residual += (u**2)
print(math.sqrt(residual))

r = (np.dot(a.T,a))
if(np.linalg.det(r)==0):
    print("Inverse doesnt exist")
else:
    r_inv = np.linalg.inv(r)
    act = np.dot(np.dot(r_inv,a.T),b)
    print(np.dot(np.dot(r_inv,a.T),b))
    y = np.dot(a,act) - b
    residual = 0
    for u in y:
        residual += (u**2)
    print(math.sqrt(residual))

for v in range(0,n):
    plt.plot(iter,x_list[v],label=f'x{v+1}')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Change in values')
plt.legend()
plt.grid(True)
plt.show()