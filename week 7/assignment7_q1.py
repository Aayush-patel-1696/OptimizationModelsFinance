import pandas as pd
import numpy as np
from scipy.optimize import minimize

df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
array = df.iloc[:,1:].to_numpy()[1:]

covariance_matrix = np.cov(array,bias=1)
print(covariance_matrix)
np.savetxt(r'week 7\covariance_matrix.csv', covariance_matrix, delimiter=',')


mean = np.resize(array.mean(axis=1),(10,1))
np.savetxt(r'week 7\mean.csv', mean, delimiter=',')
mean_bar = mean - 0.005

def minimize_func(x,cov,mean_bar):
    deno = -1*np.matmul(np.transpose(mean_bar),x)
    neum = np.sqrt(np.matmul(np.matmul(x,cov),np.transpose(x)))
    return deno/neum

x = np.ones(10)
con = {"type":"eq","fun":lambda x: np.matmul(np.ones(10),np.transpose(x))-1}

result = minimize(minimize_func,0.1*np.ones(10),args=(covariance_matrix,mean_bar),bounds=None,constraints=con,tol= 10**-11)
shorting_allowed_x = result.x
print("shorting allowed result",result)
shorting_allowed_expected_portfoilio_result = np.matmul(np.transpose(shorting_allowed_x),mean)
print("mean shorting allowed" ,shorting_allowed_expected_portfoilio_result)
print("variance shorting allowed",np.matmul(np.matmul(shorting_allowed_x,covariance_matrix),np.transpose(shorting_allowed_x)))
np.savetxt(r'week 7/shorting_allowed_expected_portfoilio_result.csv', shorting_allowed_x, delimiter=',')



# x = np.ones(10)
# con = {"type":"eq","fun":lambda x: np.matmul(np.ones(10),np.transpose(x))-1}

# bnds = ((0,float('inf')),(0,float('inf')),
#         (0,float('inf')),(0,float('inf')),
#         (0,float('inf')),(0,float('inf')),
#         (0,float('inf')),(0,float('inf')),
#         (0,float('inf')),(0,float('inf')))

# result = minimize(minimize_func,0.1*np.ones(10),args=(covariance_matrix,mean_bar),bounds=bnds,constraints=con,tol= 10**-15)
# shorting_not_allowed_x = result.x
# print("shorting  not allowed result",result)
# shorting_not_allowed_expected_portfoilio_result = np.matmul(np.transpose(shorting_not_allowed_x),mean)
# np.savetxt(r'week 7/shorting_not_allowed_expected_portfoilio_result.csv', shorting_not_allowed_expected_portfoilio_result, delimiter=',')


# # efficient_sh_portfolio = []

# # for i in range(1,11):

# #     con_2 = ({"type":"eq","fun":lambda x: np.sum(x)-1},
# #        {"type":"eq","fun":lambda x: np.matmul(np.transpose(x),mean)-values[i-1]})
    
# #     result = minimize(minimize_func,0.1*np.ones(10),args=(covariance_matrix,mean_bar),bounds=None,constraints=con_2,tol= 10**-15)
# #     temp_array = result.x
# #     efficient_sh_portfolio.append(temp_array)

# # print(efficient_sh_portfolio)
# # np.savetxt(r'week 7/efficient_sh_portfolio.csv', efficient_sh_portfolio, delimiter=',')

# values = [0.012	,0.011	,0.010,	0.009,	0.008,	0.00775,	0.00750,	0.0065,	0.006,	0.005]
# all_portfolios = np.ones((11,10))
# sigmas = []
# for i in range(0,len(values)):

#     weight = (values[i] - shorting_allowed_expected_portfoilio_result)/(0.005-shorting_allowed_expected_portfoilio_result)
   
#     sigma = ((1-weight)**2)*(np.matmul(np.matmul(shorting_allowed_x,covariance_matrix),np.transpose(shorting_allowed_x)))
#     sigmas.append(sigma)
#     portfolio= np.array((1-weight)*shorting_allowed_x).tolist()
#     all_portfolio = np.array(weight).tolist() 
#     all_portfolio.extend(portfolio)
#     print(all_portfolio)

#     all_portfolios[:,i]= np.transpose(all_portfolio)
    


# print(all_portfolios)
# np.savetxt(r'week 7/all_porfolios_shorting_allowed.csv', all_portfolios, delimiter=',')

# print(sigmas)
# np.savetxt(r'week 7/all_porfolios_sigmas.csv', sigmas, delimiter=',')



# values = [0.012	,0.011	,0.010,	0.009,	0.008,	0.00775,	0.00750,	0.0065,	0.006,	0.005]
# all_portfolios = np.ones((11,10))
# sigmas = []
# for i in range(0,len(values)):

#     weight = (values[i] - shorting_not_allowed_expected_portfoilio_result)/(0.005-shorting_not_allowed_expected_portfoilio_result)
   
#     sigma = ((1-weight)**2)*(np.matmul(np.matmul(shorting_not_allowed_x,covariance_matrix),np.transpose(shorting_not_allowed_x)))
#     sigmas.append(sigma)
#     portfolio= np.array((1-weight)*shorting_not_allowed_x).tolist()
#     all_portfolio = np.array(weight).tolist() 
#     all_portfolio.extend(portfolio)
#     print(all_portfolio)

#     all_portfolios[:,i]= np.transpose(all_portfolio)
    


# print(all_portfolios)
# np.savetxt(r'week 7/all_porfolios_shorting_not_allowed.csv', all_portfolios, delimiter=',')

# print(sigmas)
# np.savetxt(r'week 7/all_porfolios_shorting_not_sigmas.csv', sigmas, delimiter=',')


