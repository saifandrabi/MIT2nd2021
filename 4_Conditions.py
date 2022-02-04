''' Prog to Demo various Conditional Statements '''
''' A: IF Statement'''
a = 33
b = 200
if b > a:
  print("b is greater than a")
'''If-ELSE that ELIF'''
a = 33
b = 8
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
    print("No Conslusions Drawn")
'''Use Of Logical Operators in Conditional Statemtns'''
'''AND'''
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
'''OR'''
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
'''NOT'''

'''The pass Statement'''
'''if statements cannot be empty, but if you 
for some reason have an if statement with no content, put in the pass statement 
to avoid getting an error.'''
a = 33
b = 200

if b > a:
  pass# We are not interested in any body assocaited wiht if statemnt