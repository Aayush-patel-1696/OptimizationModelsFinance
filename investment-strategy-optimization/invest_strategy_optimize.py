
from scipy import optimize,stats
import numpy as np

def optimize_investment_1():

    """You have to determine an investment strategy for the next three years. At present (time 0) the amount
    of $100,000 is available for investment. Five investments are available. The cash flows associated with
    investing $1 in each of them are given in the table below. Returns from investments can be reinvested
    immediately. For example, if we decide to invest 10,000 in A and 10,000 in C, then the resulting cash
    flows will be -10,000 in year 1, -5,000 in Year 2, etc.
    At most $75,000 can be placed in any single investment. Cash earns 8% per year.
    The cash flows are given in the table below.
    Time 0 1 2 3
    Investment A -$1.00 $0.50 $1.00 $0.00
    Investment B -$1.00 $1.20 $0.00 $0.00
    Investment C $0.00 -$1.00 $0.50 $1.00
    Investment D -$1.00 $0.00 $0.00 $1.90
    Investment E $0.00 $0.00 -$1.00 $1.50
    This table should be read as follows: for every dollar committed to Investment A, there is an outflow
    of $1 at time 0 (now), inflow of $0.50 at time 1, and inflow of $1 at time 2. Each dollar committed to
    Investment C results in an outflow of $1 at time 1, inflow of $0.50 at time 2, and inflow of $1 at time 3,
    etc. Money obtained from Investments A or B at time 1 can be used to invest in C."""

    A_in = [[0.5,1.20,1,0,0],[1.25,0.6,0.5,0,1]]
    b_in = [75000,75000]

    A_eq = np.ones((1,5))
    b_eq = [100000]

    bnd = [(0,75000),(0,75000),(0,float('inf')),(0,75000),(0,float('inf'))]
    Obj = [-1.1153,-0.8403,-0.5836,-0.6403,-0.42]

    opt = optimize.linprog(c=Obj, A_ub=A_in, b_ub=b_in,A_eq=A_eq, b_eq=b_eq,bounds=bnd,method="simplex")
    print(opt)
    print("Ans",opt.x)


def optimize_bond_fund_2():
    
    """ You are holding hold a bond portfolio of four bonds, 100 units of each of them. You are considering
        rebalancing it. The bid and ask prices of the bonds are given in the table below.
        Bid Price Ask Price
        Bond 1 $980 $990
        Bond 2 $960 $972
        Bond 3 $970 $985
        Bond 4 $940 $954
        The cash payments of the bonds in the next three years are as follows.
        Bond 1 Bond 2 Bond 3 Bond 4
        Year 1 $100 $70 $80 $60
        Year 2 $110 $80 $90 $50
        Year 3 $1100 $1090 $1020 $1110
        1
        Cash on hand earns 5% interest. You want to re-balance the portfolio in such a way that at any time
        in the future your cash position will be at least as good as the position that would result from your current
        portfolio. How much money you can take out today under this condition? """
    
    size = 4
    ask_bid_matrix = np.array([[980,990],[960,972],[970,985],[940,954]])
    A_eq_1 = np.zeros((size,size*size),dtype=float)
    for index,rows in enumerate(A_eq_1):
        rows[index*size:(index+1)*size] = 1
        rows[index*size +index] = 0
    A_in_2 = A_eq_1 
    b_in_2 = [100]*size

    return_matrix = np.array([[100,70,80,60],[110,80,90,50],[1100,1090,1020,1110]])
    A_in = np.zeros((3,size*size))
    for index,rows in enumerate(A_in):
        temp = np.zeros((size,size))
        for indexj,rowj in enumerate(A_eq_1):
            temp[indexj,indexj] = -1*return_matrix[index,indexj]
            
        rows[:] =  temp.flatten()
    b_in = -1*(np.sum(return_matrix,axis=1))

    A_in_3 = np.concatenate((A_in,A_in_2),axis=0)
    b_in_3 = np.concatenate((b_in,b_in_2))

    # Create Bound matrix for variables
    bnd = []
    for i in range(size*size):
        bnd.append((0,float('inf')))

    Obj_1 = np.ones((size,size),dtype=float)
    for index,row in enumerate(Obj_1):
        row[:] = row[:]*ask_bid_matrix[index,0]
        row[index] = 0
    print(Obj_1)
    Obj_2 = np.ones((size,size),dtype=float)
    for index,row in enumerate(Obj_2.T):
        row[:] = row[:]*ask_bid_matrix[index,1]
        row[index] = 0

    print(Obj_2)
    Obj = 1*(Obj_1-Obj_2).flatten()


    opt = optimize.linprog(c=Obj, A_ub=A_in_3, b_ub=b_in_3,bounds=bnd,method="highs")
    print(opt)
    print("Ans",opt.x)
    print("Obj",np.sum(Obj*100))


def optimize_pension_fund_3():

    """The pension fund manager of the Association of Business Professors identified three reliable mutual
    funds, which have a long time successful record of operation: the Growth Fund, the Global Fund and the
    Income Fund. All these funds invest in four asset categories: U.S. large capitalization stocks, U.S. small
    capitalization stocks, foreign stocks and U.S. bonds, in proportions given in the following table.
    Asset Category Growth Global Income
    U.S. Large Stocks 45% 20% 25%
    U.S. Small Stocks 40% 10% 5%
    Foreign Stocks 10% 60% 5%
    U.S. Bonds 5% 10% 65%
    Average return rate 17% 14% 10%
    The table also shows an average annual return of these funds observed over a long time period.
    The pension fund offers to its participants a Balanced Package. The minimum and maximum investments of the package in each asset category package is given in the table below.
    Asset Category Minimum Maximum
    U.S. Large Stocks 25% 35%
    U.S. Small Stocks 15% 25%
    Foreign Stocks 20% 30%
    U.S. Bonds 20% 30%
    The pension fund has 5 million dollars. How much should the manager invest in the Growth Fund, Global
    Fund and Income Fund to construct the package and to maximize the annual return?"""


    A_in_1 = [[0.45,0.20,0.25],[0.40,0.10,0.05],[0.10,0.60,0.05],[0.05,0.10,0.65]]
    b_in_1 = [5*0.35,5*0.25,5*0.30,5*0.30]

    A_in_2 = [[-0.45,-0.20,-0.25],[-0.40,-0.10,-0.05],[-0.10,-0.60,-0.05],[-0.05,-0.10,-0.65]]
    b_in_2 = [-5*0.25,-5*0.15,-5*0.20,-5*0.20]

    A_in = np.concatenate((A_in_1,A_in_2),axis=0)
    b_in = np.concatenate((b_in_1,b_in_2))
    
    A_eq = [[1,1,1]]
    b_eq = [5]

    bnd = [(0,5),(0,5),(0,5)]
    Obj = [-0.17,-0.14,-0.10]


    opt = optimize.linprog(c=Obj, A_ub=A_in, b_ub=b_in,A_eq=A_eq, b_eq=b_eq,bounds=bnd,method="highs")
    print(opt)
    print("Ans",opt.x)
  

if __name__ == "__main__":

    optimize_investment_1()
    optimize_bond_fund_2()
    optimize_pension_fund_3()
   





    

    


    













