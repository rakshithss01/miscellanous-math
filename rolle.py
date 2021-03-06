#Rolle's Theorem
from sympy import *
from numpy import linspace
x = Symbol('x')
y = Symbol('y')
h = Symbol('h')
#Function
y = x**2+2
#Intervals
a = -2
b = 2
is_valid = True
for c in linspace(a,b,20):
#checking for continuity i.e  lhl = rhl= f(c) here;
    t = y.subs({x:c}).evalf()
    t1 = y.subs({x:c-h}).evalf()
    t2 = y.subs({x:c+h}).evalf()
    w1 = Limit(t1,h,0).doit()
    w2 = Limit(t2,h,0).doit()
#checking for differntiability i.e LHD = RHD;
    y1 = Limit((t1-y)/h,h,0).doit()
    y2 = Limit((y-t2)/h,h,0).doit()
#checking if the function is continuous and differentiable;
    if (t != w1 and t != w2 and y1!=y2):
      is_valid= False
      break
if is_valid:
   print("The Function is Continous in [",a,",",b,"]")
   print("The Function is Differentiable in (",a,",",b,")")
   print("Rolle's Theorem is verified")
#finding the first derivative 
   y1 = Derivative(y,x).doit()
# finding the point where x=0; using solve
   g=solve(y1)
   j = simplify(g)
   print("The point c is: ",j)
else:
     print("The Function is not Continous in [",a,",",b,"]")
     print("The Function is not Differentiable in (",a,",",b,")")
     print("Rolle's Theorem doesn't hold valid for the function")
