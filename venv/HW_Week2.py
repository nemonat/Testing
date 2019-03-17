#A.
x = 10
y = 20
if x>y:
    print("BIG")
if x<y:
    print("small")

#B.
for x in range(5):
    print("Run a for loop 5 times")

for x in range(5):
    print(x)

#C.
season = 3
if season == 1:
    print ("summer")
elif season == 2:
    print ("winter")
elif season == 3:
    print ("fall")
elif season == 4:
    print ("spring")

#D.
#1.
count = 1
while count<11:
    print(count)
    count=(count+1)

#E
My_Age = 41
Last_Name = "U"
Currency = 3.631
Abroad = "yes"
My_apt = 12

print (My_Age)
print (Last_Name)
print (Currency)
print (Abroad)
print (My_apt)
print (Currency + My_Age)

#F
name = input("Enter you phone number")
print("Your phone number is:", name)

#J
import array as arr
a=arr.array("i",{10,20,30})
for i in range(len(a)):
    print(a[i])


