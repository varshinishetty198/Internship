import numpy as np
a=np.array(([1,2,3],
           [4,5,6]))
b=np.array([10,20,30])
result=a+b
print(result)

arr=np.random.rand(100)
squared=arr**2
print(squared)

#0
import numpy as np
a = np.array(10)
print(a)
print(a.ndim)

#1 dimentional
import numpy as np
arr1 = np.array([10, 20, 30, 40])
print(arr1)
print("Dimension:", arr1.ndim)

#2 dimentional
import numpy as np

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr2)
print("Dimension:", arr2.ndim)

#3
import numpy as np

arr3 = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr3)
print("Dimension:", arr3.ndim)


arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print("vstack",vstacked)
hstacked=np.hstack((a,b))
print("hstack",hstacked)

data=np.array([[10,20,30],
               [40,50,60]])
print(np.mean(data))
print(np.mean(data, axis=0))
print(np.mean(data,axis=1))

A=np.array([[1,2], [3,4]])
B=np.array([[5,6], [7,8]])
print(np.dot(A,B))


arr=np.linspace(0,3,5)
print(arr)

arr=np.random.rand(2,2)
print(arr)

arr=np.array([1.2,2.8,-3.7])
print(np.floor(arr))


