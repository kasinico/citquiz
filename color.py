
def throws():
    return 5/0
x = 5
y = 0
z = x/y
    
try:
    z = x / y
except ZeroDivisionError:
    z = 5
    print ('Caught an exception')
