
import math

def function(a,b,c):
    y = a*(x**2) + b*x + c
    return y



def function_solved(x,y):
    str = "At x = {}, y = {}"
    print(str.format(x,function(a,b,c)))
    
    
    
a = float(input("Coefficient a: "))
b = float(input("Coefficient b: "))
c = float(input("Coefficient c: "))

str = "Parabola y={}x^2 + {}x + {}"
print(str.format(a,b,c))

x=0
y=function(a,b,c)
for x in range(0,10,1):
    function_solved(x,y)

x=10
y=function(a,b,c)
while x == 10:
    function_solved(x,y)
    x=10**2
    function_solved(x,y)
    x=10**3
    function_solved(x,y)
    x=10**4
    function_solved(x,y)
    x=10**5
    function_solved(x,y)
    x=10**6
    function_solved(x,y)
    x=10**7
    function_solved(x,y)
    


    
    
    
    
    
    
   
   
    


    
    
