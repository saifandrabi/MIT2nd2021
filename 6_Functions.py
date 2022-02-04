# demonestration of functions
'''Creating Function named as Sum()'''
def sum(a,b):
    s=a+b
    print(s)
    print("hello")
a=int(input("enter a"))
b=int(input("enter b"))
'''Calling FUnction sum(a,b)'''
sum(a,b)

'''Functions Returning Values'''
def MUL(a,b):
    return a*b
a=int(input("enter a"))
b=int(input("enter b"))
'''Calling FUnction sum(a,b)'''
A=MUL(a,b)
print("the result=",A)
''' Another Way to to call and print'''
print("Result =",MUL(a,b))
