import numpy as np 
print("______1D Array______")
arr1D=np.array([60, 70, 80, 90, 100])
print(arr1D)
print("_______2D Array______")
arr2D=np.array([
    [80,90,66],
    [60,50,70]
])
print(arr2D)
print("_______3D Array______")
arr3D=([
    [
        [80, 75, 90],
        [70, 85, 88]
    ],
    [
        [60, 65, 70],
        [90, 92, 95]
    ]
])
print(arr3D)
print("="*40)
print("___Shape,Dimension,Datatype,Size of 2D Array____")
print(arr1D.shape)
print(arr2D.ndim)
print(arr2D.dtype)
print(arr2D.size)
print("="*40)
print("____Zeros Array____")
arr_zeros=np.zeros((2,3))
print(arr_zeros)
print("____Ones Array____")
arr_ones=np.ones((2,3))
print(arr_ones)
print("____Array with value of 5_____")
arr_five=np.full((3,3),5)
print(arr_five)
print("="*40)
print("_______Array10 to 50 with step 10_______")
arr_range=np.arange(10, 50, 10)
print(arr_range)
print("_______LineSpace_____")
arr_linespace=np.linspace(0, 100, 5)
print("="*40)
print("______Identity matrix_______")
arr_identity=np.eye(4)
print(arr_identity)
print("_____Diagonal_____")
arr_diagonal= np.diag([10, 20, 30, 40])
print(arr_diagonal)