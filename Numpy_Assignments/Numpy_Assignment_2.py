import numpy as np

arr2 = np.array([1,2,3,4,5])
arr3 = np.array([6,5,2,4,1])

def greater(n,m):
    print("Element wise '>' opertion")
    for i in range(len(n)):
        for j in range(len(m)):
            if(n[i]>m[j]):
                print(f"{n[i]} is greater than {m[j]}")
            elif(m[j]>n[i]):
                print(f'{m[j]} is greater than {n[i]}')
    print("")
def less_than(n,m):
    print("Element wise '<' opertion")
    for i in range(len(n)):
        for j in range(len(m)):
            if(n[i]<m[j]):
                print(f"{n[i]} is less than {m[j]}")
            elif(m[j]<n[i]):
                print(f'{m[j]} is less than {n[i]}')
    print("")
def less_equal(n,m):
    print("Element wise '<=' opertion")
    for i in range(len(n)):
        for j in range(len(m)):
            if(n[i]<=m[j]):
                print(f"{n[i]} is less than or equal to {m[j]}")
            if(m[j]<=n[i]):
                print(f"{m[i]} is less than or equal to {n[j]}")
    print("")

def greater_equal(n,m):
    print("Element wise '>=' opertion")
    for i in range(len(n)):
        for j in range(len(m)):
            if(n[i]>=m[j]):
                print(f"{n[i]} is greater than or equal to {m[j]}")
            if(m[j]>=n[i]):
                print(f"{m[i]} is greater than or equal to {n[j]}")
    print("")


less_than(arr2,arr3)
greater(arr2,arr3)
less_equal(arr2,arr3)
greater_equal(arr2,arr3)
