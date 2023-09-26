
from scipy import optimize,stats
import numpy as np

# Initialize the variables
# position_matrix = np.random.randint(100, size=(10, 2))   # n*2
# rate_conversion_matrix = np.random.randint(3, size=(10, 10))   # n*n
# size = position_matrix.shape[0]



def optimize_investment_1():

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

    size = 4
    ask_bid_matrix = np.array([[980,990],[960,972],[970,985],[940,954]])
    A_eq_1 = np.zeros((size,size*size),dtype=float)
    for index,rows in enumerate(A_eq_1):
        rows[index*size:(index+1)*size] = 1
        rows[index*size +index] = 1

    A_eq_2 = np.zeros((size,size*size))
    for index,rows in enumerate(A_eq_2):
        temp = np.zeros((size,size),dtype=float)
        temp[:,index] = -1*ask_bid_matrix[:,0]/ask_bid_matrix[index,1]
        temp[index,index] = 0
        rows[:] = temp.flatten()


    A_eq = A_eq_1 + A_eq_2
    b_eq = [100]*size

    return_matrix = np.array([[100,70,80,60],[110,80,90,50],[1100,1090,1020,1110]])
    A_in = np.zeros((3,size*size))
    for index,rows in enumerate(A_in):
        temp = np.zeros((size,size))
        for indexj,rowj in enumerate(A_eq):
            temp[indexj,indexj] = -1*return_matrix[index,indexj]
            
        rows[:] =  temp.flatten()
    b_in = -1*(np.sum(return_matrix,axis=1))


    # Create Bound matrix for variables
    bnd = []
    for i in range(size*size):
        bnd.append((0,float('inf')))

    Obj = np.zeros((size,size),dtype=float)
    for index,row in enumerate(Obj):
        row[index] = -1*(np.sum(np.multiply(return_matrix[:,index],[1.1025,1.05,1])))
    Obj = Obj.flatten()

    opt = optimize.linprog(c=Obj, A_ub=A_in, b_ub=b_in,A_eq=A_eq, b_eq=b_eq,bounds=bnd,method="highs")
    print(opt)
    print("Ans",opt.x)
    print("Obj",np.sum(Obj*100))


def optimize_pension_fund_3():


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





    

    


    













