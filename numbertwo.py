# Python program to sort elements
 
# function to return the second element of the
# two elements passed as the parameter
def sortSecond(val):
    return val[1]
 
# list1 to demonstrate the use of sorting
list1 = [(1,2),(3,3),(1,1)]
 
# sorts the array in ascending according to
list1.sort(key=sortSecond)
print(list1)
 
# sorts the array in descending according to
list1.sort(key=sortSecond,reverse=True)
print(list1)