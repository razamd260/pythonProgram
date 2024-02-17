'''
Created on Feb 17, 2024

@author: Noushad
'''
sum1=0;
arr=[1,3,4]
for i in range(len(arr)):
    sum1=sum1+arr[i]
   
sum2=0

for i in range(1,arr[len(arr)-1]+1):
    sum2=sum2+i
 
print("Missing Number : ",sum2-sum1)  
    
    
