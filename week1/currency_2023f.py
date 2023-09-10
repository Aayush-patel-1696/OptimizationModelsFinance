
"""
Solve current system of equations

Maximize : f(x) = [sigma(sum i)]r_i2*(sigma(sum j)x_ij)

Constraints:

Inequality:
1. sigma(sum over j) x_ij >= b_i

Equality:
2. sigma(sum over i) r_ij*x_ij = b_i

Bound
3. xij >= 0


	Initial 	Desired
	Position	Position
		
EUR	 70	        62
USD	 20	        20
AUD	 8	        6
GBP	 3	        8
NZD	 15	        10
CAD	 7	        15
CHF	 2	        3
JPY	 1,500	1,800
HKD	 35	       40
SGD	 18	       13

Cross rates		Currency Sold									
		            EUR	USD	AUD	GBP	NZD	CAD	CHF	JPY	HKD	SGD
Currency Purchased	EUR	1	1.09168	1.67831	0.85905	1.82269	1.4786	0.95762	159.247	8.56588	1.47414
	                USD	0.9159	1	1.53754	0.78712	1.669	1.35443	0.8772	145.869	7.8467	1.35017
                    AUD	0.59566	0.65045	1	0.51173	1.08585	0.88094	0.57054	94.88	5.0985	0.87837
                    GBP	1.16387	1.2706	1.95353	1	2.12164	1.72111	1.11469	185.365	9.969	1.70973
                    NZD	0.54848	0.59886	0.92058	0.47122	1	0.81104	0.52534	87.359	4.6995	0.80833
                    CAD	0.6761	0.73817	1.1346	0.5807	1.2316	1	0.64761	107.696	5.79359	0.9965
                    CHF	1.0438	1.1396	1.75112	0.8968	1.9027	1.5432	1	166.282	8.9456	1.53981
                    JPY	0.00628	0.00685	0.01053	0.00539	0.01144	0.00928	0.00601	1	0.05358	0.00923
                    HKD	0.11669	0.12739	0.19586	0.10025	0.21254	0.17256	0.11177	18.58813	1	0.17202
                    SGD	0.6782	0.7402	1.13833	0.5827	1.2324	1.003512293	0.6494	107.952	5.8086	1




"""

from scipy import optimize
import numpy as np

# Initialize the variables
# position_matrix = np.random.randint(100, size=(10, 2))   # n*2
# rate_conversion_matrix = np.random.randint(3, size=(10, 10))   # n*n
# size = position_matrix.shape[0]

position_matrix = np.array([[70,62],
                            [20,20],
                            [8,6],
                            [3,8],
                            [15,10],
                            [7,15],
                            [2,3],
                            [1500,1800],
                            [35,40],
                            [18,13]])   # n*2

rate_conversion_matrix = np.array([[1,1.09168,1.67831,0.85905,1.82269,1.4786,0.95762,159.247,8.56588,1.47414],
                                    [0.9159,1,1.53754,0.78712,1.669,1.35443,0.8772,145.869,7.8467,1.35017],
                                    [0.59566,0.65045,1,0.51173,1.08585,0.88094,0.57054,94.88,5.0985,0.87837],
                                    [1.16387,1.2706,1.95353,1,2.12164,1.72111,1.11469,185.365,9.969,1.70973],
                                    [0.54848,0.59886,0.92058,0.47122,1,0.81104,0.52534,87.359,4.6995,0.80833],
                                    [0.6761,0.73817,1.1346,0.5807,1.2316,1,0.64761,107.696,5.79359,0.9965],
                                    [1.0438,1.1396,1.75112,0.8968,1.9027,1.5432,1,166.282,8.9456,1.53981],
                                    [0.00628,0.00685,0.01053,0.00539,0.01144,0.00928,0.00601,1,0.05358,0.00923],
                                    [0.11669,0.12739,0.19586,0.10025,0.21254,0.17256,0.11177,18.58813,1,0.17202],
                                    [0.6782,0.7402,1.13833,0.5827,1.2324,1.003512293,0.6494,107.952,5.8086,1]])   # n*n
size = position_matrix.shape[0]


def optimize_us_dollar_wealth(position_matrix,rate_conversion_matrix,size):

    # Create the coefficient matrix for constraint 1
    A_in = np.zeros((size,size*size),dtype =int)
    for index,rows in enumerate(A_in):
        rows[index*size:(index+1)*size] = -1

    b_in = np.array(position_matrix[:,1]*-1)     # desired position matrix

    # Create the coefficient matrix for constraint 2
    A_eq = np.zeros((size,size*size),dtype =float)
    for index,row in enumerate(A_eq):
        temp = np.zeros((size,size),dtype=float)
        temp[:,index] = rate_conversion_matrix[:,index]
        row[:] = temp.flatten()

    b_eq = np.array(position_matrix[:,0])     # desired position matrix

    # Create Bound matrix for variables
    bnd = []
    for i in range(size*size):
        bnd.append((0,float('inf')))
    print("bnd",bnd)

    #  Creare Objective function matrix
    Obj = np.ones((size,size))
    dollar_index = 1
    for index,row in enumerate(Obj):
        row[:] = -rate_conversion_matrix[index,dollar_index]
        
    Obj = Obj.flatten()
    print("Obj",Obj)

    # Solve Optimization 
    opt = optimize.linprog(c=Obj, A_ub=A_in, b_ub=b_in,A_eq=A_eq, b_eq=b_eq,bounds=bnd,method="highs")
    print(opt)
    print("Ans",opt.x)

    data = np.asarray((opt.x).reshape(10,10))
    np.savetxt(r'week1/ans_optimize_us_dollar.csv', data, delimiter=',')

    return None

def get_arbitrage(position_matrix,rate_conversion_matrix,size):

    # Create the coefficient matrix for constraint 1
    A_in = np.zeros((size,size*size),dtype =int)
    for index,rows in enumerate(A_in):
        rows[index*size:(index+1)*size] = -1

    b_in = np.array((position_matrix[:,0])*-1)     # desired position matrix

    print("A_in",A_in)

    # Create the coefficient matrix for constraint 2
    A_eq = np.zeros((size,size*size),dtype =float)
    for index,row in enumerate(A_eq):
        temp = np.zeros((size,size),dtype=float)
        temp[:,index] = rate_conversion_matrix[:,index]
        row[:] = temp.flatten()

    b_eq = np.array(position_matrix[:,0])     # desired position matrix

    print("A_eq",A_eq)

    # Create Bound matrix for variables
    bnd = []
    for i in range(size*size):
        bnd.append((0,float('inf')))
    print("bnd",bnd)

    #  Creare Objective function matrix
    Obj = rate_conversion_matrix-1
    Obj = Obj.flatten()
    print("Obj",Obj)


    # Solve Optimization 
    opt = optimize.linprog(c=Obj, A_ub=A_in, b_ub=b_in,A_eq=A_eq, b_eq=b_eq,bounds=bnd,method="highs")
    print(opt)
    print("Ans",)

    data = np.asarray(((opt.x)*rate_conversion_matrix.flatten()).reshape(10,10))
    print(np.sum(data,axis=0))
    np.savetxt(r'week1/ans_arbitrage.csv', data, delimiter=',')

    return None



if __name__ == "__main__":

    problem_1 = optimize_us_dollar_wealth(position_matrix,rate_conversion_matrix,size)
    problem_2 = get_arbitrage(position_matrix,rate_conversion_matrix,size)






    

    


    













