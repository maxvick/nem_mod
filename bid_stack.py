import numpy as np
import pandas as pd
import random as rd 
#create the bid stack
bid_dict = {'volume': [10, 10, 25, 50], 'bid':[45, 64, 0, 5]}
bid_stack = pd.DataFrame(data=bid_dict)
demand = rd.randint(0, 100)

#sort the stack
bid_stack = bid_stack.sort_values(by=['bid'])

price = -1000
found = False
#run the stack
bid_stack['cum_vol'] = bid_stack['volume'].cumsum()
bid_stack['marginal_setter'] = bid_stack['cum_vol'] < demand
for i in range(1, bid_stack.shape[0]):
     if (not bid_stack['marginal_setter'].iloc[i] and  
         bid_stack['marginal_setter'].iloc[i - 1]):
         
         #this is the settlement price
         price = bid_stack['bid'].iloc[i]

#print the output
print('The price was ' + str(price))
print('The demand was ' + str(demand))
print('The bid stack was:')
print(bid_stack)

