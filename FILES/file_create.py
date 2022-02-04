'''Creating Stu_list.txt file with write mode, in case if this file is not exixting this
statement will create a new file'''
file1=open("Stu_list.txt",'w')
#file2=open("Stu_list.txt",'r')
#file2.write("this is my first file created demo")
#file2.writelines("this is")
file1.write("hello\n this is my first line \n this is my second line \n this is my third line")
file1.close()
file2=open("Stu_list.txt",'r')
print(file2.readline())
'''for i in file2:
    print(i)'''
print("Displaying FIle All contents of file")
print(file2.readlines())