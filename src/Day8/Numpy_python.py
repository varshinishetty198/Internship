import numpy as np
a=np.array(([1,2,3],
           [4,5,6]))
b=np.array([10,20,30])
result=a+b
print(result)

arr=np.random.rand(1000000)
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