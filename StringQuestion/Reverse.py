'''
Created on Feb 17, 2024

@author: Noushad

for i in range(len(str)-1,-1,-1): 
considered index
Automatic len(str)   take len(str)-1
'''   
str="i am noushad ansari"
newstr=""
final=""
str=str.split(" ")
for i in range(len(str)):
    newstr=str[i][len(str): : -1]
    for j in range(len(newstr)):
        final=final+newstr[j];
    
    newstr=""
    final=final+" "
    
print(final)    
        
    
