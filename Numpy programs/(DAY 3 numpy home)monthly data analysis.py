import numpy as np

sales = np.arange(1, 13) * 10          
monthly = sales.reshape(3, 4)
print("Reshaped:\n", monthly)


ravelled  = monthly.ravel()
flattened = monthly.flatten()
print("ravel()  :", ravelled)
print("flatten():", flattened)

dept1 = np.array([100, 200, 300])
dept2 = np.array([400, 500, 600])
print("hstack:", np.hstack([dept1, dept2]))
print("vstack:\n", np.vstack([dept1, dept2]))


a = np.array([[1, 2]])
b = np.array([[3, 4]])
print("Row-wise:\n", np.concatenate([a, b], axis=0))
print("Col-wise:\n", np.concatenate([a, b], axis=1))


arr1d = np.array([10, 20, 30, 40, 50, 60])
print("split:", np.split(arr1d, 3))

arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("hsplit:", np.hsplit(arr2d, 2))
print("vsplit:", np.vsplit(arr2d, 2))