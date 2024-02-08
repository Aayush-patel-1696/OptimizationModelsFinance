import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\aayus\Documents\GitHub\OptimizationModelsFinance\week_6\hw6-F23-data.xlsx')
array = df.iloc[:,1:].to_numpy()[1:]
array_transpose = np.transpose(array)

cdf = []
temp_value = 0
for i in range(0,12):
    temp_value += 1/12
    cdf.append(temp_value)
print(cdf)

x_val = (100000/10)*np.ones(10)
mean_values = []
for i in array_transpose:
    mean_value = np.dot(i,x_val)
    mean_values.append(mean_value)
sorted_mean_values_equally_weighted = np.sort(mean_values).tolist()
print(sorted_mean_values_equally_weighted)

second_order_dominant_equally_weighted = []
for i in range(0,len(sorted_mean_values_equally_weighted)):
    if (i==0):
        second_order_dominant_equally_weighted.append(cdf[i])
    else:
        second_order_dominant_equally_weighted.append(second_order_dominant_equally_weighted[i-1]+ (sorted_mean_values_equally_weighted[i]-sorted_mean_values_equally_weighted[i-1])*(cdf[i]))

x_val = np.array([0,0,0,0,0,0,0,1,0,0])*((100000))
mean_values = []
for i in array_transpose:
    mean_value = np.dot(i,x_val)
    mean_values.append(mean_value)
sorted_mean_values_on_8 = np.sort(mean_values).tolist()
print(sorted_mean_values_on_8)

second_order_dominant_on_8 = []
for i in range(0,len(sorted_mean_values_on_8)):
    if (i==0):
        second_order_dominant_on_8.append(cdf[i])
    else:
        second_order_dominant_on_8.append(second_order_dominant_on_8[i-1]+ (sorted_mean_values_on_8[i]-sorted_mean_values_on_8[i-1])*(cdf[i]))

print("second_order_dominant",second_order_dominant_on_8,sorted_mean_values_on_8)


x_val = np.array([0,0.2,0.2,0,0,0.2,0,0.2,0.2,0])*((100000))
mean_values = []
for i in array_transpose:
    mean_value = np.dot(i,x_val)
    mean_values.append(mean_value)
sorted_mean_values_on_2_3_6_8_9 = np.sort(mean_values).tolist()
print(sorted_mean_values_on_2_3_6_8_9)

second_order_dominant_on_2_3_6_8_9 = []
for i in range(0,len(sorted_mean_values_on_2_3_6_8_9)):
    if (i==0):
        second_order_dominant_on_2_3_6_8_9.append(cdf[i])
    else:
        second_order_dominant_on_2_3_6_8_9.append(second_order_dominant_on_2_3_6_8_9[i-1]+ (sorted_mean_values_on_2_3_6_8_9[i]-sorted_mean_values_on_2_3_6_8_9[i-1])*(cdf[i]))

fig = plt.figure(figsize=(9,6))
plt.step(sorted_mean_values_equally_weighted,cdf,'b',label='CDF on equal weigheted portfolio' )
plt.step(sorted_mean_values_on_8,cdf,'r',label='CDF on 8  portfolio' )
plt.step(sorted_mean_values_on_2_3_6_8_9,cdf,'g',label='CDF on 2,3,6,8,9 portfolio' )
plt.xlabel('$Z_{k}$')
plt.ylabel('$CDF$')
plt.legend()

plt.title('CDF of different portfolios')
plt.savefig("week 11\\comparision_pdf.png")
plt.show()


fig = plt.figure(figsize=(9,6))
plt.plot(sorted_mean_values_equally_weighted,second_order_dominant_equally_weighted,'b',label='CDF on equal weigheted portfolio' )
plt.plot(sorted_mean_values_on_8,second_order_dominant_on_8,'r',label='CDF on 8  portfolio' )
plt.plot(sorted_mean_values_on_2_3_6_8_9,second_order_dominant_on_2_3_6_8_9,'g',label='CDF on 2,3,6,8,9 portfolio' )
plt.xlabel('$Z_{k}$')
plt.ylabel('$CDF Area$')
plt.legend()

plt.title('different portfolios')
plt.savefig("week 11\\comparision_second_order_pdf.png")
plt.show()


