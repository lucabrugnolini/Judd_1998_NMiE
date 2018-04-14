# Judd 1998, Chapter 1 exercise
import numpy as np

# Ex.1 
print "Ex. 1"
def ADDXY(x, y):
    return x + y  # Return values with a return statement

def MXY(x, y):
    return x*y

def DXY(x, y):
    return x/y

def PRINT_ADD_M_D(x,y):
    summ = ADDXY(x,y)
    mul =   MXY(x,y)
    div =   DXY(x,y)
    print "The sum of {0} and {1} is {2}".format(x,y,summ)
    print "The product of {0} and {1} is {2}".format(x,y,mul)
    print "The division of {0} and {1} is {2}".format(x,y,div)
    
PRINT_ADD_M_D(3,2)

# Ex. 2
print "Ex. 2"
def SQRD_DIFF(x,y):
    return (x-y)**2

def FEVAL(x,y,z):
    return z(x,y)

z = FEVAL(2,3,SQRD_DIFF)
print z

# Ex. 3
print "Ex. 3"
def sum_elem_vec(x):
    A = np.random.uniform(0,1,(x,))
    return [sum(A) for i in A] 

print sum_elem_vec(10)

# Ex. 4  
print "Ex. 4"
def sum_row_array(x,y):
    A = np.random.uniform(0,1,(x,y))
    return A.sum(axis=1)

print sum_row_array(5,3)

# Ex. 5
print "Ex. 5"
def mul_array_vec(x,y,z,w):
    A = np.random.uniform(0,1,(x,y))
    b = np.random.uniform(0,1,(1,z))
    c = np.random.uniform(0,1,(w,))
    Ac = A*c
    bA =  b.T*A
    return Ac,bA

print mul_array_vec(5,3,5,3)