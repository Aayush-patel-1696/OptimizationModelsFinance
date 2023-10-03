""""
Example to solve Optimization Problem using Scipy

Maximize : 3x1 + 2x2

Constraints: 
1. 2x1 + x2 <= 3
2. x1 + 2x2 <= 4


Bounds:
4. x1>=0 
5. x2>=0

Above problem will be solved by Optimize library of scipy
"""

from scipy import optimize

# # Objective Matrix
# obj = [-3, -2]        # Objective function: 3x1 + 2x2

# # Constraint matrix
# lhs_ineq = [[ 2,  1],  # 1. 2x1 + x2 <= 3
#             [1,  2]]   # 2. x1 + 2x2 <= 4
# rhs_ineq = [3,  
#             4]
# # Bound Matrix
# bnd = [(0, float("inf")),  # Bounds of x1>=0 
#       (0, float("inf"))]  # Bounds of x2>=0

# len(bnd)
# # Solve Optimization 
# opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd,method="highs")

# print(opt)

# Ans x: [ 6.667e-01  1.667e+00]
# Maximized value = 5.333



# Objective Matrix
obj = [1,1,0,0,0]        # Objective function: 3x1 + 2x2

# Constraint matrix
lhs_ineq = [[ -1,0,3,-2,2],  # 1. 2x1 + x2 <= 3
            [ 0,-1,-1,1,-1]]   # 2. x1 + 2x2 <= 4
rhs_ineq = [0,  
            0]

lhs_eq = [[0,0,1,1,1]]
rhs_eq =[1]
# Bound Matrix
bnd = [(-2,3),(-1,1),(0, float("inf")),(0, float("inf")), # Bounds of x1>=0 
      (0, float("inf"))]  # Bounds of x2>=0

len(bnd)
print(bnd)
# Solve Optimization 
opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq,bounds=bnd,method="highs")

print(opt.x)
print(opt)



# Objective Matrix
obj = [1,0,0,0]        # Objective function: 3x1 + 2x2

# Constraint matrix
lhs_ineq = [[ -1,3,-2,2],  # 1. 2x1 + x2 <= 3
            [ -1,-1,1,-1]]   # 2. x1 + 2x2 <= 4
rhs_ineq = [0,  
            0]

lhs_eq = [[0,1,1,1]]
rhs_eq =[1]
# Bound Matrix
bnd = [(-float("inf"), float("inf")),(0, float("inf")),(0, float("inf")), # Bounds of x1>=0 
      (0, float("inf"))]  # Bounds of x2>=0

len(bnd)
print(bnd)
# Solve Optimization 
opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq,bounds=bnd,method="highs")

print(opt.x)
print(opt)