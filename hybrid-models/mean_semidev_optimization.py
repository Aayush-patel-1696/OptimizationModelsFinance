import pandas as pd
import numpy as np
from scipy import optimize

"""
ρ = [Z(x)] = -E[Z(x)] + c σ[Z(x)]
where σ[Z] = E{ max(0,E[Z] – Z)} is the lower semideviation of the first order.
 for c= 0.23, 0.5, 0.75
 """


class MeanSemidevOpt:

    def __init__(self,file_path,investment_amount):
        self.filepath = file_path
        self.df = pd.read_excel(file_path)
        self.array = self.df.iloc[:, 1:].to_numpy()[1:]
        self.num_assets = len(self.array[:,1])
        self.num_senarios = len(self.array[0,:])
        self.investment_amount = investment_amount
        self.array_transpose = np.transpose(self.array)

    def optimize_objective(self,c,j):

        
        """
            ρ =  Hybrid Risk Measure
            ρ = [Z(x)] = -E[Z(x)] + c σ[Z(x)]

            where σ[Z] = E{ max(0,E[Z] – Z)} is the lower semideviation of the first order.
        """

        mean = np.resize(self.array.mean(axis=1),(self.num_assets,1))
        lhs_ineq = np.zeros((self.num_senarios,self.num_senarios+self.num_assets))

        for i in range(12):
            lhs_ineq[i,i] = -1  # vk
            lhs_ineq[i,self.num_senarios:self.num_senarios+self.num_assets] = -1*(self.array[:,i]) + np.transpose(mean)  # Rk

        rhs_ineq = np.zeros((1,self.num_senarios))

        lhs_eq = np.zeros((1,self.num_senarios+self.num_assets))
        lhs_eq[0,self.num_senarios:self.num_senarios+self.num_assets] = 1
        rhs_eq = [self.investment_amount]

        bnd = []
        for i in range(self.num_senarios+self.num_assets):
            bnd.append((0,float('inf')))


        obj = np.ones((1,self.num_senarios+self.num_assets))*(1/self.num_senarios)*c
        obj[0,self.num_senarios:self.num_senarios+self.num_assets] = -1*np.array(np.transpose(mean))

        print(obj)
        opt = optimize.linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,A_eq=lhs_eq,b_eq=rhs_eq, bounds=bnd,method="highs")

        print(opt)
        print(opt.x[-1])
        print(opt.x[self.num_senarios:self.num_senarios+self.num_assets])
        print(np.sum(opt.x[self.num_senarios:self.num_senarios+self.num_assets]))



mean_semideviation_analysis = MeanSemidevOpt(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\senario_data.xlsx',100000)
mean_semideviation_analysis.optimize_objective(1,0.3)

       