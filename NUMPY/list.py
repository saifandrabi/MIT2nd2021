import numpy as np
list=[1,2,3,4,(345,67,87),'q',9,0]
list2=[1,2,3,4,[345,67,87],'z',9,0]
#print(list)
#list2=(1,2,3,4,[345,67,87],78,9,0)
'''print(list2)
list3=[1,3,4,list2]
print(list3)
list4=(1,3,4,list)
print(list4)
list2[5]=56
print(list4)'''
list3=list+list2
print(list3)
arr = np.array([1,2,'s','b'])
arr2 = np.array([1,2,'s','b'])
print(arr+arr2)
