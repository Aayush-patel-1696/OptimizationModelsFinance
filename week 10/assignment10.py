import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


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
    rhs_eq = [1]

    bnd = []
    for i in range(23):
        bnd.append((0,float('inf')))

    bnd[-1] = (float('-inf'),float('inf'))

    obj = np.ones((1,23))*(1/j)*(1/12)*c
    obj[0,-1] = -1*c
    obj[0,12:22] = -1*(1-c)*np.array(np.transpose(mean))
    print("obj",obj)
    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

    # print(opt)
    # print(opt.x[-1])
    print(opt.x[12:22])
    # print(np.sum(opt.x[12:22]))
    # np.savetxt(rf"week 10/porfolio_ans_alpha_{j}_c_{c}.csv", opt.x, delimiter=',')

    return opt.x[12:22]




def find_worst_probabilitites(mean_values,alpha,c):

    lhs_ineq = -1*np.identity(12)
    rhs_ineq = ((1/12)*np.ones((1,12))*(1/alpha)*c)[0]

    lhs_eq = [[1,1,1,1,1,1,1,1,1,1,1,1]]
    rhs_eq = [-1/2]

    bnd = []
    for i in range(12):
        bnd.append((-float('inf'),0))

    obj= -1*np.array(mean_values)

    # print(obj)

    opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

    uk = -1*((-c)*np.ones((1,12))*(1/12) + np.array(opt.x))

    # print("Worst Probabilitites",uk)
    # print("Sum of Probabilities",np.sum(uk))
    # print("Cumilitive distribution",np.cumsum(uk))

    return np.cumsum(uk)

alpha = 0.3
c =0.5
df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
array = df.iloc[:,1:].to_numpy()[1:]

optimized_portfolio_values = Q1problemb(alpha,c)

array_transpose = np.transpose(array)


x_val = (optimized_portfolio_values)
print("x_val",x_val)

# print(array_transpose)

mean_values = []
for i in array_transpose:
    mean_value = np.dot(i,x_val)
    mean_values.append(mean_value)


mean_values = np.sort(mean_values)
cdf_on_optimized_portfolio= find_worst_probabilitites(mean_values,alpha,c)

print("Zk on optimzed weighted ",mean_values)
print("cdf on optimized weighted",cdf_on_optimized_portfolio)
equally_likely = np.cumsum((1/12)*np.ones((1,12)))
print("cdf of probability senarioes from normal",equally_likely)

result = pd.DataFrame(np.transpose([mean_values,cdf_on_optimized_portfolio,equally_likely]),columns=['Z_k','CDF_worst','CDF_nominal'])
result.to_csv("week 10\\Result of CDFs on porfolios having optimized weights.csv")

fig = plt.figure(figsize=(9,6))
plt.step(mean_values,cdf_on_optimized_portfolio,'b',label='worst probablility distribution' )
plt.step(mean_values,equally_likely,'r',label="Uniform distribution")

plt.xlabel('$Z_{k}$')
plt.ylabel('$CDF$')
plt.legend()

plt.title('Comparision of  CDF between worst and uniform on optimized portfolio');
plt.savefig("week 10\\comparision_pdf_optimized.png")
      



x_val= (0.1*np.ones((1,10))).tolist()[0]

print("x_val",x_val)
mean_values = []
for i in array_transpose:
    mean_value = np.dot(i,x_val)
    mean_values.append(mean_value)

mean_values = np.sort(mean_values)

cdf_on_equally_weighted_portfolio = find_worst_probabilitites(mean_values,alpha,c)

print("Zk on equally weighted ",mean_values)
print("cdf on equally weighted",cdf_on_equally_weighted_portfolio)

equally_likely = np.cumsum((1/12)*np.ones((1,12)))
print("cdf of probability senarioes from normal",equally_likely)

fig = plt.figure(figsize=(9,6))
plt.step(mean_values,cdf_on_equally_weighted_portfolio,'b',label='worst probablility distribution' )
plt.step(mean_values,equally_likely,'r',label="Uniform distribution")

plt.xlabel('$Z_{k}$')
plt.ylabel('$CDF$')
plt.legend()

plt.title('Comparision of  CDF between worst and uniform on eqaully weighted portfolio');
plt.savefig("week 10\\comparision_pdf_equally_weighted.png")

result = pd.DataFrame(np.transpose([mean_values,cdf_on_equally_weighted_portfolio,equally_likely]),columns=['Z_k','CDF_worst','CDF_nominal'])
result.to_csv("week 10\\Result of CDFs on portfolios having equal weights.csv")
      




