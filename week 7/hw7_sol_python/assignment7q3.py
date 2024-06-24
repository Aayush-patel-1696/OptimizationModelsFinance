import pandas as pd
import numpy as np




def Q3problem1():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]

    covariance_matrix = np.cov(array,bias=1)
    
   
    mean = np.resize(array.mean(axis=1),(10,1))
   
    x_val = np.zeros(10)
    x_val[8] = 100000

    mean_value = np.dot(np.transpose(mean),x_val)
    
    sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))
   
    print(mean_value)
    print(sigma)
    z_alpha = [-1.282,-0.842,-0.524]
    Var = []
    for i in z_alpha:
        temp_var = i*sigma+mean_value
        Var.append(temp_var)

    print(Var)


def Q3problem2():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]

    covariance_matrix = np.cov(array,bias=1)

   
    mean = np.resize(array.mean(axis=1),(10,1))

    x_val = (100000/10)*np.ones(10)

    mean_value = np.dot(np.transpose(mean),x_val)
    
    sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))
  
    print(mean_value)
    print(sigma)
    z_alpha = [-1.282,-0.842,-0.524]
    Var = []
    for i in z_alpha:
        temp_var = i*sigma+mean_value
        Var.append(temp_var)

    print(Var)

def Q3problem3():

    df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
    array = df.iloc[:,1:].to_numpy()[1:]

    covariance_matrix = np.cov(array,bias=1)

   
    mean = np.resize(array.mean(axis=1),(10,1))

    x_val = np.zeros(10)
    index = [1,2,5,7,8]
    money = 100000/(len(index))
    for i in index:
        x_val[i] = money

    mean_value = np.dot(np.transpose(mean),x_val)
    sigma = np.sqrt(np.matmul(np.matmul(x_val,covariance_matrix),np.transpose(x_val)))

    print(mean_value)
    print(sigma)

    z_alpha = [-1.282,-0.842,-0.524]
    Var = []
    for i in z_alpha:
        temp_var = i*sigma+mean_value
        Var.append(temp_var)

    print(Var)


Q3problem1()
Q3problem2()
Q3problem3()

                    




