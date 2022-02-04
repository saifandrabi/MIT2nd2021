'''COnditionals in Numpy'''
import numpy as np
x = np.arange(10)
condlist = [x<3, x>5]
choicelist = [x, x**2]#considers x if first part of condlist is true, and x**2 when second part of condlist that isx>5 is true
A=np.select(condlist, choicelist)
print(A)
rr_1 = np.random.rand(3, 3)
print(rr_1)