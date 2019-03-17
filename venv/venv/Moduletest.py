import datetime
print(datetime.datetime.now())

from datetime import datetime
print(datetime.now())

import array as arr
a = arr.array("i",[3,6,9])
#a[0] = 5

#print(a[1])

a.append(123)
print(a)

a.pop(0)
print(a)

a.insert(1,7)
print(a)

#number of elements
print(len(a))

# Getting all elements
for x in a:
    print(x)

for i in range(len(a)):
    print(a[i])

#my_list=[5,"a",true]
#print(my_list)

#x_tuple = 1,2,3 ,4,5
#y_tuple=('a','b')

my_dictionary = ('A':1,'B':2)
    print(my_dictionary.keys())

