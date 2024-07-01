import pandas as pd
import numpy as np
from scipy import optimize


"""
You have collected data on the monthly returns of 10 securities, as shown in the table 
below
Monthly Returns
Asset 1 2 3 4 5 6 7 8 9 10 11 12
1 0.004 -0.025 0.009 0.012 0.047 -0.019 0.006 -0.037 0.025 0.021 0.017 0.019
2 0.014 0 -0.039 0.016 -0.006 0.07 -0.021 -0.022 0.019 0.025 0.054 0.04
3 0.001 0.006 0.005 0.019 0.016 0.057 -0.052 0.027 0.039 0 0.011 0.002
4 -0.012 -0.021 0.062 0.036 -0.002 -0.038 0.015 -0.003 0.024 0.012 0.048 -0.007
5 -0.043 0.005 0.023 0 0.023 0.04 0.034 0.029 -0.013 -0.04 0.011 0.003
6 0.015 -0.027 -0.01 -0.027 0.002 0.038 0.056 -0.004 0.08 0.001 0.013 0.026
7 -0.001 0.011 0.056 -0.024 0.019 -0.048 -0.015 0.019 0.062 0.023 0.002 -0.017
8 0.039 0.03 0.003 -0.004 0.016 -0.021 0.003 0.018 -0.026 -0.022 0.026 0.073
9 0.017 0.02 -0.024 -0.004 0.019 0.039 -0.03 0.025 0.021 0.054 -0.011 0.056
10 0.108 -0.003 0.061 0.008 0.024 -0.037 -0.013 0.053 -0.009 -0.021 0.026 -0.009


You treat these realizations as equally likely scenarios, each with a probability of 1/12.
You plan to invest $100,000 and you are considering three possible portfolios:
Portfolio 1: All money in asset 9;
Portfolio 2: Money distributed uniformly among all assets (equally weighted);
Portfolio 3: Invest equally in assets 2, 3, 6, 8, and 9 and nothing in the other assets.


Calculate the Value at Risk and the Average Value at Risk of the profit of these 
portfolios, for the risk levels α = 0.1, 0.2, and 0.3. Use linear programming"""

class VarCvar:
    def __init__(self, filepath,investment_amount=100000):
        self.filepath = filepath
        self.df = pd.read_excel(filepath)
        self.array = self.df.iloc[:, 1:].to_numpy()[1:]
        self.num_assets = len(self.array[:,1])
        self.num_senarios = len(self.array[0,:])
        self.investment_amount = investment_amount
        self.array_transpose = np.transpose(self.array)

    def calculate_mean_values(self, x_val):
        mean_values = []
        for row in self.array_transpose:
            mean_value = np.dot(row, x_val)
            mean_values.append(mean_value)
        return mean_values

    def calculate_cdf(self, length=12):
        cdf = []
        temp_value = 0
        for i in range(length):
            temp_value += 1 / length
            cdf.append(temp_value)
        return cdf

    def find_var(self, sorted_mean_values, cdf, alpha_range):
        var = []
        for alpha in alpha_range:
            for index, value in enumerate(cdf):
                if value > alpha:
                    var.append(-1*sorted_mean_values[index])
                    break
        return var
    
    def cvar_var_linear_optimization(self,sorted_mean_values, alpha):

        for j in alpha:
            lhs_ineq = np.zeros((self.num_senarios , self.num_senarios +1))

            # Equation Setup
            for i in range(self.num_senarios):
                lhs_ineq[i, i] = -1
            lhs_ineq[:, -1] = 1
            rhs_ineq = np.array(sorted_mean_values)

            # Bounds 
            bnd = [(0, float('inf'))] * self.num_senarios  + [(float('-inf'), float('inf'))]

            # Objective 
            obj = np.ones((1, self.num_senarios +1)) * (1 / j) * (1 / self.num_senarios )
            obj[0, -1] = -1
            opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="highs")

            var = list(opt.x)[-1]
            avar = np.dot(np.reshape(np.array(opt.x), (1, 13)), np.transpose(obj))
            print(f"For alpha = {j} x values are {opt.x}")
            print(f"The AVar value is {avar[0][0]} and Var value is {var}")

    def problem1_var(self):
        x_val = np.zeros(self.num_assets)
        x_val[8] = self.investment_amount 
        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()
        cdf = self.calculate_cdf()
        alpha_range = [0.1, 0.2, 0.3]
        var = self.find_var(sorted_mean_values, cdf, alpha_range)
        print(f"Sorted Mean Values: {sorted_mean_values}")
        print(f"CDF: {cdf}")
        print(f"Var: {var}")

    def problem2_var(self):
        x_val = (self.investment_amount  / self.num_assets) * np.ones(self.num_assets)
        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()
        cdf = self.calculate_cdf()
        alpha_range = [0.1, 0.2, 0.3]
        var = self.find_var(sorted_mean_values, cdf, alpha_range)
        print(f"Sorted Mean Values: {sorted_mean_values}")
        print(f"CDF: {cdf}")
        print(f"Var: {var}")

    def problem3_var(self):
        x_val = np.zeros(self.num_assets)
        indices = [1, 2, 5, 7, 8]
        money = self.investment_amount / len(indices)
        for i in indices:
            x_val[i] = money
        print(f"x_val: {x_val}")
        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()
        cdf = self.calculate_cdf()
        alpha_range = [0.1, 0.2, 0.3]
        var = self.find_var(sorted_mean_values, cdf, alpha_range)
        print(f"Sorted Mean Values: {sorted_mean_values}")
        print(f"CDF: {cdf}")
        print(f"Var: {var}")

    def problem1_avar(self):

        x_val = np.zeros(self.num_assets)
        x_val[8] = self.investment_amount 
        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()

        alpha_range = [0.1, 0.2, 0.3]

        self.cvar_var_linear_optimization(sorted_mean_values, alpha_range)

    def problem2_avar(self):
        x_val = (self.investment_amount  / self.num_assets) * np.ones(self.num_assets)
        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()
        cdf = self.calculate_cdf()
        alpha_range = [0.1, 0.2, 0.3]
        self.cvar_var_linear_optimization(sorted_mean_values, alpha_range)

 
    def problem3_avar(self):
        x_val = np.zeros(self.num_assets)
        indices = [1, 2, 5, 7, 8]
        money = self.investment_amount / len(indices)
        for i in indices:
            x_val[i] = money

        mean_values = self.calculate_mean_values(x_val)
        sorted_mean_values = np.sort(mean_values).tolist()
        alpha_range = [0.1, 0.2, 0.3]

        self.cvar_var_linear_optimization(sorted_mean_values, alpha_range)



var_cvar_analysis = VarCvar(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\senario_data.xlsx')
var_cvar_analysis.problem1_var()
var_cvar_analysis.problem2_var()
var_cvar_analysis.problem3_var()

var_cvar_analysis.problem1_avar()
var_cvar_analysis.problem2_avar()
var_cvar_analysis.problem3_avar()

