class MIT_4th:
    roll_no=0000
    name= "notentered"
    phone=0000000
    def __init__(self,rollno,name,phone):
        self.roll_no=rollno
        self.name=name
        self.phone=phone
    def display_det(self):
        print("The name of the student is ",self.name,"\nthe rollno of the student is ",self.roll_no,"\nand his phone is ",self.phone)
        print(MIT_4th.roll_no,"\n",MIT_4th.name,"\n",MIT_4th.phone)


Stu1=MIT_4th(100,'syed',9419000000)
Stu1.display_det()




