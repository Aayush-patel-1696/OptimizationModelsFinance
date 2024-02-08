import pandas as pd
import numpy as np


def Q2problem1 ():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]
    array_transpose = np.transpose(array)


    x_val = np.zeros(10)
    x_val[8] = 100000
    mean_values = []
    for i in array_transpose:
        mean_value = np.dot(i,x_val)
        mean_values.append(mean_value)




    sorted_mean_values = np.sort(mean_values).tolist()
    print(sorted_mean_values)
    # np.savetxt(r'week 7\sorted_mean_values_1.csv', sorted_mean_values, delimiter=',')
    cdf = []
    temp_value = 0
    for i in range(0,12):

        temp_value += 1/12
        cdf.append(temp_value)

    print(cdf)

    alpha_range = [0.1,0.2,0.3]
    Var = []
    for i in alpha_range:

        for index,j in enumerate(cdf):
            if j > i:
                Var.append(sorted_mean_values[index])
                break


    print(Var)




def Q2problem2 ():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]
    array_transpose = np.transpose(array)


    x_val = (100000/10)*np.ones(10)
 
    mean_values = []
    for i in array_transpose:
        mean_value = np.dot(i,x_val)
        mean_values.append(mean_value)




    sorted_mean_values = np.sort(mean_values).tolist()
    print(sorted_mean_values)
    # np.savetxt(r'week 7\sorted_mean_values_2.csv', sorted_mean_values, delimiter=',')

    cdf = []
    temp_value = 0
    for i in range(0,12):

        temp_value += 1/12
        cdf.append(temp_value)

    print(cdf)

    alpha_range = [0.1,0.2,0.3]
    Var = []
    for i in alpha_range:

        for index,j in enumerate(cdf):
            if j > i:
                Var.append(sorted_mean_values[index])
                break


    print(Var)



def Q2problem3 ():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]
    array_transpose = np.transpose(array)


    x_val = np.zeros(10)
    index = [1,2,5,7,8]
    money = 100000/(len(index))
    for i in index:
        x_val[i] = money
        
    print(x_val)
    mean_values = []
    for i in array_transpose:
        mean_value = np.dot(i,x_val)
        mean_values.append(mean_value)




    sorted_mean_values = np.sort(mean_values).tolist()
    print(sorted_mean_values)
    # np.savetxt(r'week 7\sorted_mean_values_3.csv', sorted_mean_values, delimiter=',')

    cdf = []
    temp_value = 0
    for i in range(0,12):

        temp_value += 1/12
        cdf.append(temp_value)

    print(cdf)

    alpha_range = [0.1,0.2,0.3]
    Var = []
    for i in alpha_range:

        for index,j in enumerate(cdf):
            if j > i:
                Var.append(sorted_mean_values[index])
                break


    print(Var)


# Q2problem1()
#Q2problem2()
Q2problem3()
from scipy import optimize
import numpy as np


def problem1_a():

    alpha = [0.1,0.2,0.3]
    for j in alpha:

        porfolio1_z = [-3000.0, -2400.0, -1100.0, -400.0, 1700.0000000000002, 1900.0, 2000.0, 2100.0, 2500.0, 3900.0, 5400.0, 5600.0]
        lhs_ineq = np.zeros((12,13))

        for i in range(12):
            lhs_ineq[i,i] = -1

        lhs_ineq[:,-1] = 1
        rhs_ineq = np.array(porfolio1_z)
     

        # Create Bound matrix for variables
        bnd = []
        for i in range(13):
            bnd.append((0,float('inf')))

        bnd[-1] = (float('-inf'),float('inf'))
 

        obj = np.ones((1,13))*(1/j)*(1/12)
        obj[0,-1] = -1
 
        # # Solve Optimization 
        opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd,method="highs")

        Var = list(opt.x)[-1]
        Avar = np.dot(np.reshape(np.array(opt.x),(1,13)),np.transpose(obj))
      
        print(f" For 1st Porfoilio alpha = {j} x values are {opt.x}")
        print(f"For  1st Porfoilio alpha = {j} the AVar value is {Avar} and Var value is {-Var}")

def problem1_b():

    alpha = [0.1,0.2,0.3]
    for j in alpha:

        porfolio1_z = [-170.0, -40.0, 320.0, 530.0, 810.0, 1050.0, 1420.0, 1460.0, 1580.0, 1860.0, 1970.0, 2220.0]
        lhs_ineq = np.zeros((12,13))

        for i in range(12):
            lhs_ineq[i,i] = -1

        lhs_ineq[:,-1] = 1
        rhs_ineq = np.array(porfolio1_z)


        # Create Bound matrix for variables
        bnd = []
        for i in range(13):
            bnd.append((0,float('inf')))

        bnd[-1] = (float('-inf'),float('inf'))
        print("bnd",bnd)

        obj = np.ones((1,13))*(1/j)*(1/12)
        obj[0,-1] = -1
   
        # # Solve Optimization 
        opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd,method="highs")

        Var = list(opt.x)[-1]
        Avar = np.dot(np.reshape(np.array(opt.x),(1,13)),np.transpose(obj))
      
        print(f" For 2nd Porfoilio alpha = {j} x values are {opt.x}")
        print(f"For  2nd Porfoilio alpha = {j} the AVar value is {Avar} and Var value is {-Var}")


def problem1_c():

    alpha = [0.1,0.2,0.3]
    for j in alpha:

        porfolio1_z = [-1300.0, -880.0, 0.0, 580.0, 880.0, 940.0, 1160.0, 1720.0, 1860.0, 2660.0, 3660.0, 3940.0]
        lhs_ineq = np.zeros((12,13))

        for i in range(12):
            lhs_ineq[i,i] = -1

        lhs_ineq[:,-1] = 1
        rhs_ineq = np.array(porfolio1_z)
    
        # Create Bound matrix for variables
        bnd = []
        for i in range(13):
            bnd.append((0,float('inf')))

        bnd[-1] = (float('-inf'),float('inf'))
        print("bnd",bnd)

        obj = np.ones((1,13))*(1/j)*(1/12)
        obj[0,-1] = -1
   
        # # Solve Optimization 
        opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,bounds=bnd,method="highs")

        Var = list(opt.x)[-1]
        Avar = np.dot(np.reshape(np.array(opt.x),(1,13)),np.transpose(obj))
      
        print(f" For 3rd Porfoilio alpha = {j} x values are {opt.x}")
        print(f"For  3rd Porfoilio alpha = {j} the AVar value is {Avar} and Var value is {-Var}")


problem1_a()
problem1_b()
problem1_c()







    
           
    
    
           
    