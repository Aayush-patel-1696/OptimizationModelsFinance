import pandas as pd
import numpy as np
from scipy.optimize import minimize



df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx',)



array = df.iloc[:,1:].to_numpy()[1:]
# print(array)
# Calculate Expected return 
mean = np.resize(array.mean(axis=1),(10,1))

print("mean",mean)
# #Calculate the covariance matrix
centered_return_rate = array-mean

centered_return_rate_2 = np.matmul(centered_return_rate,np.transpose(centered_return_rate))
#print(centered_return_rate_2)
covariance_matrix=np.cov(centered_return_rate_2)
# print(centered_return_rate_2)
print(covariance_matrix)
# np.savetxt(r'week_6\centered_return_rate_2.csv', centered_return_rate_2, delimiter=',')



def minimize_func(x,cov):
    return np.matmul(np.matmul(np.transpose(x),cov),x)

x = np.ones(10)
con = {"type":"eq","fun":lambda x: np.sum(x)-1}
# bnds_1 = ((float('-inf'),float('inf')),(float('-inf'),float('inf')),
#         (float('-inf'),float('inf')),(float('-inf'),float('inf')),
#         (float('-inf'),float('inf')),(float('-inf'),float('inf')),
#         (float('-inf'),float('inf')),(float('-inf'),float('inf')),
#         (float('-inf'),float('inf')),(float('-inf'),float('inf')))

bnds = ((0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')))
                   # objective,  # initialized_values, 
result = minimize(minimize_func,0.08*np.ones(10),centered_return_rate_2,bounds=None,constraints=con,method ='SLSQP')
shorting_allowed_x = result.x
print("shorting allowed result",result)
shorting_allowed_expected_portfoilio_result = np.matmul(np.transpose(shorting_allowed_x ),mean)
print("mean" ,shorting_allowed_expected_portfoilio_result)
np.savetxt(r'week_6\shorting_allowed_x.csv', shorting_allowed_x, delimiter=',')


result = minimize(minimize_func,0.08*np.ones(10),centered_return_rate_2,bounds=bnds,constraints=con,method ='SLSQP')
# print(result)
# print(result.x)
shorting_not_allowed_x = result.x
print("shorting not allowed result",result)
shorting_not_allowed_expected_portfoilio_result = np.matmul(np.transpose(shorting_not_allowed_x),mean)
print("mean",shorting_not_allowed_expected_portfoilio_result)
np.savetxt(r'week_6/shorting_not_allowed_x.csv', shorting_not_allowed_x, delimiter=',')



con_2 = ({"type":"eq","fun":lambda x: np.sum(x)-1},
       {"type":"eq","fun":lambda x: np.matmul(np.transpose(x),mean)-0.012})
result = minimize(minimize_func,0.08*np.ones(10),centered_return_rate_2,bounds=None,constraints=con_2,method ='SLSQP')
print("shorting_allowed_x_2",result)
shorting_allowed_x_2 = result.x
print("shorting_allowed_x_2",shorting_allowed_x_2)
shorting_allowed_expected_portfoilio_result_2 = np.matmul(np.transpose(shorting_allowed_x_2 ),mean)
print("shorting_allowed_x_2",shorting_allowed_expected_portfoilio_result_2)
#np.savetxt(r'week_6/shorting_allowed_x_2.csv', shorting_not_allowed_x, delimiter=',')

efficient_portfolio = []
values = [0.012	,0.014	,0.011,	0.015,	0.013,	0.0125,	0.0118,	0.0134,	0.0145,	0.0116]
for i in range(1,11):

    # value = shorting_allowed_expected_portfoilio_result +i*(5/1000)
    # values.append(value)
    value = values[i-1]
    temp_array = shorting_allowed_x - np.divide((shorting_allowed_x-shorting_allowed_x_2),shorting_allowed_expected_portfoilio_result-shorting_allowed_expected_portfoilio_result_2)*(shorting_allowed_expected_portfoilio_result-value)

    efficient_portfolio.append(temp_array)


print(efficient_portfolio)
print(values)

np.savetxt(r'week_6/efficient_portfolio.csv', efficient_portfolio, delimiter=',')

# result = minimize(minimize_func,0.08*np.ones(10),centered_return_rate_2,bounds=bnds,constraints=con_2,method ='SLSQP')
# # print(result)
# # print(result.x)
# shorting_not_allowed_x_2 = result.x
# shorting_not_allowed_expected_portfoilio_result_2 = np.matmul(np.transpose(shorting_not_allowed_x_2),mean)
# print(shorting_not_allowed_expected_portfoilio_result_2)



efficient_sh_nt_portfolio = []
values = [0.012	,0.014	,0.011,	0.015,	0.013,	0.0125,	0.0118,	0.0134,	0.0145,	0.0116]
for i in range(1,11):


    value_nt_sh = shorting_not_allowed_expected_portfoilio_result +i*(5/1000)
    con_2 = ({"type":"eq","fun":lambda x: np.sum(x)-1},
       {"type":"eq","fun":lambda x: np.matmul(np.transpose(x),mean)-values[i-1]})
    bnds = ((0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')),
        (0,float('inf')),(0,float('inf')))
    
    result = minimize(minimize_func,0.08*np.ones(10),centered_return_rate_2,bounds=bnds,constraints=con_2,method ='SLSQP')
    temp_array = result.x

    shorting_not_allowed_expected_portfoilio_result = np.matmul(np.transpose(temp_array),mean)
    print("shorting not allowed",shorting_not_allowed_expected_portfoilio_result)
    print("shorting not allowed",values[i-1])
    efficient_sh_nt_portfolio.append(temp_array)


print(efficient_sh_nt_portfolio)
np.savetxt(r'week_6/efficient_sh_nt_portfolio.csv', efficient_sh_nt_portfolio, delimiter=',')
# print(values_nt_sh)


# temp_val = 0.0115
# x = np.ones(10)
# con_3 = ({"type":"eq","fun":lambda x: np.sum(x)-1},
#        {"type":"eq","fun":lambda x: -np.matmul(np.transpose([0.00658333, 0.0125,    0.01091667, 0.0095,     0.006,      0.01358333,
#   0.00725,   0.01125 ,   0.01516667, 0.01566667]),x)+temp_val})
# bnds = ((0,float('inf')),(0,float('inf')),
#     (0,float('inf')),(0,float('inf')),
#     (0,float('inf')),(0,float('inf')),
#     (0,float('inf')),(0,float('inf')),
#     (0,float('inf')),(0,float('inf')))

# result = minimize(minimize_func,0.065*np.ones(10),centered_return_rate_2,bounds=bnds,constraints=con_3,method ='SLSQP')
# temp_array = result.x
# print(result)
# print(np.sum(temp_array))
# shorting_not_allowed_expected_portfoilio_result = np.matmul(np.transpose(temp_array),mean)
# print(shorting_not_allowed_expected_portfoilio_result)







