#1.
count=0
while 1 > 0:
    print(count)
    count +=1
    if count >= 11:
        break

#2.
num = float(input("Enter a plus or minus number"))
if num > 0:
    print("+", num)
else:
   print (num)

#3.
x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
if x > y:
    print(x)
E`lse:
    print(y)

#4.
age = int(input("Enter your age"))
height = int(input ("Enter your height"))
if age >10 and height >120:
    print("Welcome to the rollercoaster")
else:
    print("Sorry...Maybe next time")

#5.
number1 = int(input("Enter 1st number"))
number2 = int(input("Enter 2nd number"))
if number1 == number2:
   print("Equal")
else:
    print("Not Equal")

#6. That the loop will never end and the program will get stuck. Computer shutdown.

#7.
def getname(name):
    return "Hello"+" "+(name)

if __name__ == '__main__':
    print(getname("Einat"))

#8.
num = int(input("Enter a number"))
if num > 100:
    print("True")
else:
    print("False")