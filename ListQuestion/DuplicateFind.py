'''
Created on Feb 17, 2024

@author: Noushad
'''
count=0;
arr=[2,4,9,2,9,4,9,25,5,5]
for i in range(len(arr)):
    count=0
    for j in range(i+1,len(arr),1):
        if arr[i]==arr[j]:
            arr[j]=' '
            count+=1
        
    
    if count>0 and arr[i]!=' ':
        print(arr[i],end=" ")        