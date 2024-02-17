'''
Created on Feb 17, 2024

@author: hii
'''
str="noushad260"
count=0
for i in range(len(str)):
    if str[i]>='a' and str[i] <='z':
        count+=1
    
print("Total Alphabate : ",count)        