import numpy as np
#Q.11
n = np.array([10,20,30,40,50])
m = np.array([60,70,80,90,100])
print(f"Add:- {n+m}, Subtract:- {n-m}, Multiplication:- {n*m}, Divide:- {m/n}")
#Q.12
a = np.arange(10,22)
print(a.reshape(3,4))
#Q.13
print(np.eye(3))
#Q.14
c = np.matrix([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(f"No. of rows: {c.shape[0]}")
print(f"No. of columns: {c.shape[1]}")
#Q.15
print(np.diag([1,2,3,4,5]))
#Q.16
print(np.random.randint(1,100, size=(3,3,3)))
#Q.18
ls = [1,12,3,4,5]
print(np.array(ls))
#Q.17
print(np.random.randint(1,100, size=(2,3,4)))
#Q.19
print(np.random.randint(2,10, size=(3,3)))
#Q.20
print(np.arange(12,38))
#Q.21
g = np.arange(1,10)
print(g)
print(np.flip(g))
#Q.22
b = 3232
print(float(b))
#Q.23
print(np.array([1,2,3,4]))
#Q.24
n3 = np.array([10,20,30,40,50,60])
n4 = np.array([2,5,1,6,1,9])
print(np.mod(n3,n4))
#Q.25
n8 = np.arange(20,50)
print(np.mod(n8,3))