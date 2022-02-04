#ax2+bx2+c=0
import cmath
a=int(input("enter the cofficent of a"))
b=int(input("enter the cofficent of b"))
c=int(input("enter the cofficent of c"))
d=(b**2)-(4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print(root1,root2)