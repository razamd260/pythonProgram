'''
Created on Feb 17, 2024

@author: Noushad
'''
arr=[3,7,9,2,6]
temp=0;
for i in range(len(arr)):
    for j in range(i+1,len(arr),1):
        if arr[i] > arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        
    
for i in range(len(arr)):
    print(arr[i],end=" ")            
