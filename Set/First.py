'''
Created on Feb 17, 2024

@author: Md Noushad Ansari
# Definition  Set :-  Set is the collection of the unordered  items.
Each element in the set must be unique and immutable.
#duplicate alues are not allowed
#empty set syntax  null_set=set()
#empty dictionary  dict={}
# note-> list and dictionary never can be store   bcz mutable
# we can store boolean,int,float,str,tupple
# 


'''
set={2,5,7,2}
print(set)
print(type(set))
print(len(set))   
''' 
length= 3 why duplicate not consiter

'''
'''set.add("java")
print(set)
set.remove(5)
print(set)
set.add((1,3,6))
print(set)
set.add([1,4,6])
print(set)  
print(set.pop())
set1={2,8,9}
print(set.union(set1))
print(set.interaction(set1))
set.clear()
print(set)'''
set2={1,4,8,7}
set1={2,8,9}
print(set1.interaction(set2))





