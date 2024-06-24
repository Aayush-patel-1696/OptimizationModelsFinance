import pandas as pd
import numpy as np
from scipy.optimize import minimize



df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')


array = df.iloc[:,1:].to_numpy()[1:]




# # Calculate Expected return 
mean = np.resize(array.mean(axis=1),(10,1))



# # #Calculate the covariance matrix
# centered_return_rate = array-mean
# # print("Hi",centered_return_rate)
# centered_return_rate_2 = np.matmul(centered_return_rate,np.transpose(centered_return_rate))
# covariance_matrix=np.cov(centered_return_rate_2)
# print(centered_return_rate_2)

covariance_matrix = np.cov(array,bias=1)
print(covariance_matrix)


def minimize_func(x,cov):
    value = np.matmul(np.matmul(x,cov),np.transpose(x))
    print(x)
    print(value)
    return value


x = np.ones(10)
con = {"type":"eq","fun":lambda x: np.matmul(np.ones(10),np.transpose(x))-1}

result = minimize(minimize_func,0.1*np.ones(10),covariance_matrix,bounds=None,constraints=con,tol= 10**-15)
shorting_allowed_x = result.x
print("shorting allowed result",result)
shorting_allowed_expected_portfoilio_result = np.matmul(np.transpose(shorting_allowed_x ),mean)
print("mean" ,shorting_allowed_expected_portfoilio_result)



con_2 = ({"type":"eq","fun":lambda x: np.sum(x)-1},
       {"type":"eq","fun":lambda x: np.matmul(np.transpose(x),mean)-0.02})
result = minimize(minimize_func,0.1*np.ones(10),covariance_matrix,bounds=None,constraints=con_2,tol= 10**-15)
print("shorting_allowed_x_2",result)
shorting_allowed_x_2 = result.x
print("shorting_allowed_x_2",shorting_allowed_x_2)
shorting_allowed_expected_portfoilio_result_2 = np.matmul(np.transpose(shorting_allowed_x_2 ),mean)
print("shorting_allowed_x_2",shorting_allowed_expected_portfoilio_result_2)

print(shorting_allowed_x)
print(np.matmul(np.matmul(shorting_allowed_x,covariance_matrix),np.transpose(shorting_allowed_x)))



# efficient_portfolio = []
# values = [0.1213]
# for i in range(1,11):

#     # value = shorting_allowed_expected_portfoilio_result +i*(5/1000)
#     # values.append(value)
#     value = values[i-1]
#     temp_array = shorting_allowed_x - np.divide((shorting_allowed_x-shorting_allowed_x_2),shorting_allowed_expected_portfoilio_result-shorting_allowed_expected_portfoilio_result_2)*(shorting_allowed_expected_portfoilio_result-value)

#     efficient_portfolio.append(temp_array)


# print(efficient_portfolio)
# print(values)



# import numpy as np
# from scipy import optimize 

# def MinimizeRisk(CovarReturns, PortfolioSize):
    
#     def  f(x, CovarReturns):
#         func = np.matmul(np.matmul(x, CovarReturns), x.T) 
#         return func

#     def constraintEq(x):
#         A=np.ones(x.shape)
#         b=1
#         constraintVal = np.matmul(A,x.T)-b 
#         return constraintVal
    
#     xinit=np.repeat(0.1, PortfolioSize)
#     cons = ({'type': 'eq', 'fun':constraintEq})
#     lb = 0
#     ub = 1
#     bnds = tuple([(lb,ub) for x in xinit])

#     opt = optimize.minimize (f, x0 = xinit, args = (CovarReturns),  bounds = bnds, \
#                                 constraints = cons, tol = 10**-15)

#     return opt

# opt = MinimizeRisk(covariance_matrix,10)
# print(opt.x)
