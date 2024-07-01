import pandas as pd
import numpy as np
from scipy import optimize

"""Solve the problem of minimizing the function 
–(1-c) E[Z(x)] + c AVaR[Z(x)]
"""


class CvarMretOpt:

    def __init__(self,file_path,investment_amount):
        self.filepath = file_path
        self.df = pd.read_excel(file_path)
        self.array = self.df.iloc[:, 1:].to_numpy()[1:]
        self.num_assets = len(self.array[:,1])
        self.num_senarios = len(self.array[0,:])
        self.investment_amount = investment_amount
        self.array_transpose = np.transpose(self.array)

    def optimize_objective(self,ratio,j):

        
        """Solve the problem of minimizing the function 
                -(1-c) E[Z(x)] + c AVaR[Z(x)]
        """

        mean = np.resize(self.array.mean(axis=1),(self.num_assets,1))

        lhs_ineq = np.zeros((self.num_senarios,self.num_senarios+self.num_assets+1))

        for i in range(self.num_senarios):
            lhs_ineq[i,i] = -1  # vk
            lhs_ineq[i,self.num_senarios:self.num_senarios+self.num_assets] = -1*(self.array[:,i]) # Rk  
            lhs_ineq[i,-1] = 1    # n

        rhs_ineq = np.zeros((1,self.num_senarios))

        lhs_eq = np.zeros((1,self.num_senarios+self.num_assets+1))
        lhs_eq[0,self.num_senarios:self.num_senarios+self.num_assets] = 1
        rhs_eq = [self.investment_amount]

        bnd = []
        for i in range(self.num_senarios+self.num_assets+1):
            bnd.append((0,float('inf')))

        bnd[-1] = (float('-inf'),float('inf'))

        obj = np.ones((1,self.num_senarios+self.num_assets+1))*(1/j)*(1/self.num_senarios)*ratio
        obj[0,-1] = -1*ratio
        obj[0,self.num_senarios:self.num_senarios+self.num_assets] = -1*(1-ratio)*np.array(np.transpose(mean))
        opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

        print("Cvar value",opt.x[-1])
        print("Portfolio Weights",opt.x[self.num_senarios:self.num_senarios+self.num_assets])
        print(np.sum(opt.x[self.num_senarios:self.num_senarios+self.num_assets]))


cvar_mean_analysis = CvarMretOpt(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\senario_data.xlsx',100000)
cvar_mean_analysis.optimize_objective(1,0.1)

       