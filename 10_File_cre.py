'''FIle Operation'''
'''Creating a FILE when file doesnot exit'''
#File=open("MyFirstFile.txt")
#print(File.read())
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())