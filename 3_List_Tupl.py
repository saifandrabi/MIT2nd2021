'''Prog to demo the use of Collection Data Structure'''
''' List and Tuple'''
'''==== Tuple====='''
print("====TUPLE====")
Tuple = (1,2,'syed',5678,'andrabi') # Creating Tuple
print(Tuple)
'''Accessing Tuple Items'''
print("====Accessing Tuple Items====")
print(Tuple[1:4])
print(Tuple[3])
print(Tuple[:3])
print(Tuple[-2:])
'''Tuples are Immutable'''
print("Tuples are Immutable")
#Tuple[2]='syed moshin' # if we try to add some item to list it will generate Error as it is not allowed
#print(Tuple)

'''====LIST===='''
print("====LIST====")
List=[1,3,7,'odd',2,4,6,'even'] # Creating List
print(List)
'''Accessing List Items'''
print(List[:])
print(List[3:])
print(List[1:-4])
''' Adding items to list as list is mutable'''
List[3]='odd num'
print(List)
''' Appending Two Lists'''

print("Ading two Tuples")
Tuple=Tuple+Tuple# will applend two tupples
print(Tuple)
print("Ading two Lists")
New_List=List+List# Actually it will append two lists
print(New_List)
''' We can add two lists using add function also'''
print(List.__add__(List)) # List=List1._add_(List2))
#print(List.__add__(List))
New_List=New_List.__add__(List)
print(New_List)
A=[1,2,3]
B=[8,4,5]
c=A.__add__(B)
print(c)
'''Poping Item from List at a given Index'''
print("===Poping item at particular index ===")
c.pop(0)
print(c)
'''Removing specified item by name from list'''
print("===Remoing item===")
c.remove(3)
print(c)
'''Inserting Item at given index'''
c.insert(1,"orange")
print(c)
a=c.__len__()
print(a)
