My_file=open("C:\\Users\\Rikman\\Documents\\Devops\\class3.txt" , 'r', encoding='utf-8')
content = My_file.read()
print(content)
My_file.close()

#IO input Output
#decorator extend the function without modifying it
class shar:
    @staticmethod
    def drink():
        print(123)


#try:
My_file=open("C:\\Users\\Rikman\\Documents\\Devops\\class3.txt" , 'r', encoding='utf-8')
#    My_file.write()
#except IOError as e:
#    print(e)
#    print("could not open file...")

#print(123)

#except ValueError:
#    print('error')

try:
    t = open("C:\\Users\\Rikman\\Documents\\Devops\\class3.txt", 'r')
except IOError:
    print("fatal error...")
finally:
    print("this will run anyway")

try:
    t = open("C:\\Users\\Rikman\\Documents\\Devops\\class3.txt", 'r')
finally:
    print("this will run anyway")

#breakpoint on eline before


    x=5
    x=8
    x=80
ptint(x)

#PIP import Packages PYPI = Python Package index