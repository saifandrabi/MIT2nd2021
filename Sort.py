import numpy as np
A=np.array([1,4,2,6,3,8,4,9,3,6])
B=np.sort(A, kind= 'quicksort')
B=np.sort(A, kind= 'selectionsort')
print(B)
#''Argsort='Returns the indices that would sort an array.''
C=np.argsort(A)
print(C)