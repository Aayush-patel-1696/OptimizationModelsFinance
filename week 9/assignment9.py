import pandas as pd
import numpy as np
from scipy import optimize


def Q1problema():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]

    lhs_ineq = np.zeros((12,23))
    for i in range(12):
        lhs_ineq[i,i] = -1  # vk
        lhs_ineq[i,12:22] = -1*array[:,i]  # Rk
        lhs_ineq[i,-1] = 1    # n

    rhs_ineq = np.zeros((1,12))
    lhs_eq = np.zeros((1,23))
    lhs_eq[0,12:22] = 1
    rhs_eq = [100000]

    bnd = []
    for i in range(23):
        bnd.append((0,float('inf')))
    bnd[-1] = (float('-inf'),float('inf'))

    j=0.3
    obj = np.ones((1,23))*(1/j)*(1/12)
    obj[0,-1] = -1
    obj[0,12:22] = 0
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

    print(opt)
    print(opt.x)
    print(np.sum(opt.x[12:22]))


def Q1problemb(j,c):

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]
    mean = np.resize(array.mean(axis=1),(10,1))

    lhs_ineq = np.zeros((12,23))

    for i in range(12):
        lhs_ineq[i,i] = -1  # vk
        lhs_ineq[i,12:22] = -1*array[:,i] # Rk
        lhs_ineq[i,-1] = 1    # n

    print(lhs_ineq)
    rhs_ineq = np.zeros((1,12))

    lhs_eq = np.zeros((1,23))
    lhs_eq[0,12:22] = 1
    rhs_eq = [100000]

    bnd = []
    for i in range(23):
        bnd.append((0,float('inf')))

    bnd[-1] = (float('-inf'),float('inf'))

    obj = np.ones((1,23))*(1/j)*(1/12)*c
    obj[0,-1] = -1*c
    obj[0,12:22] = -1*(1-c)*np.array(np.transpose(mean))
    print("obj",obj)
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

    print(opt)
    print(opt.x[-1])
    print(opt.x[12:22])
    print(np.sum(opt.x[12:22]))
    np.savetxt(rf"week 9/Question_1_ans_alpha_{j}_c_{c}.csv", opt.x, delimiter=',')

# The file is automaticall
Q1problemb(0.3,0.23)
Q1problemb(0.3,0.5)
Q1problemb(0.3,0.75)
Q1problemb(0.3,1)
# Q1problema()



def Q2problemb(j=0.3,c=.23):

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]
    mean = np.resize(array.mean(axis=1),(10,1))
    print(mean)

    lhs_ineq = np.zeros((12,22))

    for i in range(12):
        lhs_ineq[i,i] = -1  # vk
        lhs_ineq[i,12:22] = -1*array[:,i] + np.transpose(mean)  # Rk
        #lhs_ineq[i,-1] = 1    # n

    print(lhs_ineq)
    rhs_ineq = np.zeros((1,12))

    lhs_eq = np.zeros((1,22))
    lhs_eq[0,12:22] = 1
    rhs_eq = [100000]

    bnd = []
    for i in range(22):
        bnd.append((0,float('inf')))

    #bnd[-1] = (float('-inf'),float('inf'))

    obj = np.ones((1,22))*(1/12)*c
    obj[0,12:22] = -1*np.array(np.transpose(mean))

    print(obj)
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

    print(opt)
    print(opt.x[-1])
    print(opt.x[12:22])
    print(np.sum(opt.x[12:22]))

    np.savetxt(rf"week 9/Question_2_ans_alpha_{j}_c_{c}.csv", opt.x, delimiter=',')


# Q2problemb(0.3,0.23)
# Q2problemb(0.3,0.5)
# Q2problemb(0.3,0.75)
# Q1problemb(0.3,1)






































#     covariance_matrix = np.cov(array,bias=1)
    
   
#     mean = np.resize(array.mean(axis=1),(10,1))
   
#     x_val = np.zeros(10)
#     x_val[8] = 100000

#     mean_value = np.dot(np.transpose(mean),x_val)
    
#     sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))
   
#     print(mean_value)
#     print(sigma)
#     z_alpha = [-1.282,-0.842,-0.524]
#     Var = []
#     for i in z_alpha:
#         temp_var = i*sigma+mean_value
#         Var.append(temp_var)

#     print(Var)


# def Q3problem2():

#     df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
#     array = df.iloc[:,1:].to_numpy()[1:]

#     covariance_matrix = np.cov(array,bias=1)

   
#     mean = np.resize(array.mean(axis=1),(10,1))

#     x_val = (100000/10)*np.ones(10)

#     mean_value = np.dot(np.transpose(mean),x_val)
    
#     sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))
  
#     print(mean_value)
#     print(sigma)
#     z_alpha = [-1.282,-0.842,-0.524]
#     Var = []
#     for i in z_alpha:
#         temp_var = i*sigma+mean_value
#         Var.append(temp_var)

#     print(Var)

# def Q3problem3():

#     df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
#     array = df.iloc[:,1:].to_numpy()[1:]

#     covariance_matrix = np.cov(array,bias=1)

   
#     mean = np.resize(array.mean(axis=1),(10,1))

#     x_val = np.zeros(10)
#     index = [1,2,5,7,8]
#     money = 100000/(len(index))
#     for i in index:
#         x_val[i] = money

#     mean_value = np.dot(np.transpose(mean),x_val)
#     sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))

#     print(mean_value)
#     print(sigma)

#     z_alpha = [-1.282,-0.842,-0.524]
#     Var = []
#     for i in z_alpha:
#         temp_var = i*sigma+mean_value
#         Var.append(temp_var)

#     print(Var)


# Q3problem1()
# Q3problem2()
# Q3problem3()

                    




