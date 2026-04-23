import numpy as np
print("_______Normalized scores_____")
print(np.random.rand(5))
print("_______Normal Distribution")
print(np.random.randn(5))
print("_______3*4 Array__________")
arr=np.random.randint(35, 100,(3,4))
print(arr)
print("________Random Student Selection________")
arr_1=[101, 102, 103, 104, 105]
print(np.random.choice(arr,size=2))