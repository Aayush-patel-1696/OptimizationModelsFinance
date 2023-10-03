from scipy import optimize


def dual_of_first_second_problem():
    # Primal Problem
    obj = [-4,-3]        

    # Constraint matrix
    lhs_ineq = [[ 1,1],  
                [ 2,1]]   
    rhs_ineq = [2,  
                1]


    bnd = [(0, float("inf")),(0, float("inf")) # Bounds of x1>=0 
        ]  # Bounds of x2>=0
    

    # Solve Optimization 
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd,method="highs")

    print(opt.x)


def game_matrix_primal_third_problem():

    # Primal Problem
    obj = [1,0,0]        # Objective function: 3x1 + 2x2

    # Constraint matrix
    lhs_ineq = [[ -1,-2,1],  # 1. 2x1 + x2 <= 3
                [ -1,-3,3],
                [-1,4,-3]]   # 2. x1 + 2x2 <= 4
    rhs_ineq = [0,  
                0,
                0]

    lhs_eq = [[0,1,1]]
    rhs_eq =[1]
    # Bound Matrix
    bnd = [(-float("inf"), float("inf")),(0, float("inf")),(0, float("inf")) # Bounds of x1>=0 
        ]  # Bounds of x2>=0

    len(bnd)
    print(bnd)
    # Solve Optimization 
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq,bounds=bnd,method="highs")

    print(opt.x)




def game_matrix_dual_third_problem():
    obj = [-1,0,0,0]        

    # Constraint matrix
    lhs_ineq = [[ 1,2,3,-4],  
                [ 1,-1,-3,3]]   
    rhs_ineq = [0,  
                0]

    lhs_eq = [[0,1,1,1]]
    rhs_eq =[1]

    # Bound Matrix
    bnd = [(-float("inf"), float("inf")),(0, float("inf")),(0, float("inf")),(0, float("inf"))
        ] 

    len(bnd)
    print(bnd)

    # Solve Optimization 
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq,bounds=bnd,method="highs")

    print(opt.x)



dual_of_first_second_problem()
game_matrix_primal_third_problem()
game_matrix_dual_third_problem()





