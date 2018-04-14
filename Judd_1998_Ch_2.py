# Judd 1998, Chapter 2 exercise
from __future__ import division
import numpy as np

# Ex.1 
print "Ex. 1"
def compute_fun_ex1(x,y):
    result = (1682*x*y**4 + 3*x**3 + 29*x*y**2 - 2*x**5 +832)/107751
    return result

print compute_fun_ex1(192119201,35675640)

# Ex.2 
print "Ex. 2"
print "Direct method"
def compute_fun_ex2_direct(x):
    result = 8118*x**4 + 11482*x**3 + 5741*x - 2030
    return result

print compute_fun_ex2_direct(0.707107)

print "Horner method with exp"
A = np.array([-2030, 5741, 0, 11482, 8118])
def compute_fun_ex2_horner(x,A):
    length_A = A.size-1
    SUM = A[length_A]
    for i in range(length_A-1,-1,-1):
        SUM = A[i]+SUM*x
        print i,SUM
    return SUM

print compute_fun_ex2_horner(0.707107,A)

# Ex.3 
# print "Ex. 3"
# A = np.array([64919121, -159018721, -1], [41869520.5, -102558961, 0])

# Ex.4 
print "Ex. 4"
h = 10**(-6)
x = 1
n = range(1,10,1)
def f(x):
    return (4970*x-4923)/(4970*x**2 - 9799*x + 4830)

def compute_derivative(f,h,x,n):
    f_x = ((f(x+h) - f(x))/h)**n
    return f_x

print [compute_derivative(f,h,x,i) for i in n]

# proof - analitical first derivative
print "Check the numerical first derivative against the analytical derivative"
def f_x(x):
    return (4970*(4970*x**2 - 9799*x + 4830) - (4970*x-4923)*(2*4970*x - 9799))/(4970*x**2 - 9799*x + 4830)**2

print compute_derivative(f,h,x,1), f_x(1)

# Ex.5 
print "Ex. 5"
x = 9478657
y = 2298912
def compute_fun_ex5_direct(x,y):
    return 83521*y**8 + 578*x**2*y**4 - 2*x**4 + 2*x**6 - x**8

print compute_fun_ex5_direct(x,y)






