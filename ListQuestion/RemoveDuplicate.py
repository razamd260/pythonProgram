'''
Created on Feb 17, 2024

@author: Noushad
'''
arr=[1,4,8,2,9,1,4,2,4]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            break;
    
    if i==j:
        print(arr[i],end=" ")    
    
