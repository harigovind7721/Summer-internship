import numpy as np
daily_sales=np.array([250.75, 300.40, 275.60, 400.90, 150.30, 500.50, 350.80])
Weekly_sales=np.sum(daily_sales)
Avg_daily_sales=np.mean(daily_sales)
Median_Sales=np.median(daily_sales)
Sales_variation=np.std(daily_sales)
Minimum_Maximum_sales=np.min(daily_sales),np.max(daily_sales)

print("_____Daily Sales_____\n",daily_sales)
print("_____Weekly Sales_____\n",Weekly_sales)
print("_____Avg Daily Sales____\n",Avg_daily_sales)
print("_____Median Sales______\n",Median_Sales)
print("_____Max&Min Sales_____\n",Minimum_Maximum_sales)

floor=np.floor(daily_sales)
print("____Floor____\n",floor)
ceil=np.ceil(daily_sales)
print("____Ceil____\n",ceil)
round=np.round(daily_sales)
print("____Round____\n",round)
exp_values = np.exp([1, 2, 3])
print("\nExponential Values (e^x):", exp_values)

cumulative = np.cumsum(daily_sales)
print("\n--- Cumulative Sales ---")
print(cumulative)

A = np.array([[2, 1],
              [3, 4]])

B = np.array([[1, 2],
              [5, 6]])

print("\n--- Matrix Operations ---")

print("A @ B:\n", A @ B)


det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)


inv_A = np.linalg.inv(A)
print("\nInverse of A:\n", inv_A)

eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)



coeff = np.array([[2, 1],
                  [3, 4]])
constants = np.array([5, 11])

solution = np.linalg.solve(coeff, constants)

print("\n--- Solution of Linear Equations ---")
print("x =", solution[0])
print("y =", solution[1])