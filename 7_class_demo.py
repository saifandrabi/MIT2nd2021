'''Demo for  Creating a Class, Contructor and Object'''
class First_class:
    name="andrabi"
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def dispay(self):
        print(obj1.name, obj1.phone)
'''Creating Object of Class First_class'''
obj1=First_class("syed",123) # calling default constructor
obj1.dispay()
print(obj1.name)


