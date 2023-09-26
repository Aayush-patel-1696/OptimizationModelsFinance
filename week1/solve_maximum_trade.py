


trade_list = [(1,3,10),(2,5,50),(3,8,20),(12,15,30),(17,18,20),(17,30,20)]

solved = []
for i in (0,len(trade_list)):

    temp_start = trade_list[i][0]
    temp_end = trade_list[i][1]
    temp_val =  trade_list[i][2]
    j= i+1
    while j < len(trade_list)-1:
       
        j+=1
        
        if ((trade_list[j][0]<=temp_end) & (trade_list[j][1]>= temp_end)):
            print("hello",trade_list[j])
            temp_start = trade_list[j][0]
            temp_end = trade_list[j][1]
            temp_val = trade_list[j][2]

        else:
            pass

    extract_profit =[]

    for m in trade_list:

        if m[0] <= temp_end:
          
            if len(extract_profit)==0:
                
                extract_profit.append([(m[0],m[1],m[2])])
                print(extract_profit)
            else:
                flag_append = 0
                for q in range(0,len(extract_profit)):
                    print("hi",extract_profit,q)
                    if ((extract_profit[q][-1][1] <= m[0]) and (extract_profit[q][-1][1]<= m[1]) ):
                        extract_profit[q].append((m[0],m[1],m[2]))
                    else:
                        extract_profit.append([(m[0],m[1],m[2])])
                        break


    print(extract_profit)
    break




    
    


    