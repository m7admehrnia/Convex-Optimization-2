import cvxpy as cp
import numpy as np

x = cp.Variable(5)
# c = np.array([15, 40, 35, 9, 80])
c = np.random.rand(5) * 10
# print(c)

obj = cp.Minimize(c @ x)

A = np.array([[0.1, 0.5, 0.3, 0.1, 0.7], [0.8, 0.15, 0.1, 0.9, 0], [0.1, 0.35, 0.6, 0, 0.3]])
b = np.array([0.6, 0.3, 0.1])

constraints = [A @ x == b, x >= 0]

problem = cp.Problem(obj, constraints)
problem.solve()

print(problem.status)
print(x.value)
