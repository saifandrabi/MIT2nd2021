list=['syed',"mohsin",123]
def sum(a,b):
    print("the result=",a+b)
def mul(a,b):
    print("the multiplication=",a*b)
def sub(a,b):
    print("the subtraction=",a-b)
    print("i am in sum function")
def table(n):
    count=0
    limt=15
    if(n>0):
     while(count<limt):
        print(n, "*", count, "=", n * count)
        count = count + 1