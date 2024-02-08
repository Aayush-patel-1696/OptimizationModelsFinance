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
    np.savetxt(r'week 7\sorted_mean_values_1.csv', sorted_mean_values, delimiter=',')
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
    np.savetxt(r'week 7\sorted_mean_values_2.csv', sorted_mean_values, delimiter=',')

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
    np.savetxt(r'week 7\sorted_mean_values_3.csv', sorted_mean_values, delimiter=',')

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


Q2problem1()
Q2problem2()
Q2problem3()







    
           
    
    
           
    