'''
Created on Feb 17, 2024

@author: Noushad
'''

arr=[8976,34,6778,2000,6999,7000,2,5]
max=0;
for i in range(len(arr)):
    if max< arr[i]:
        max=arr[i]
    
max2=0
for i in range(len(arr)):
    if max2<arr[i] and max!=arr[i]:
        max2=arr[i]
    
    
max3=0
for i in range(len(arr)):
    if max3<arr[i] and max!=arr[i] and max2!=arr[i]:
        max3=arr[i]
    
print(max3)        
                 
    
