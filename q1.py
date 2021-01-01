
import random
import statistics
from collections import Counter
import operator

#set a ramdom seed generator
random.seed(2020)
#set number of integers
integers = 10000
random_number= [random.randrange(1000,2001) for _ in range(integers)]
def finding_all_even_numbers(n):
    list1 = []
    for i in n:
        if i%2==0 and i%7==0:
            list1.append(i)
    return list1

list1 = finding_all_even_numbers(random_number)
def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq
   
    
dict1 = CountFrequency(list1)

#for key in sorted(dict1.keys()):
    #print ("% d : % d"%(key, dict1[key]))
for key in sorted(dict1.keys()):
    print(f'{key} : {dict1[key]}')
