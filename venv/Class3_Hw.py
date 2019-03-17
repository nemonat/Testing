#1
#a = 1/0

#if __name__ == '__main__':

 #   try:
  #      a = 1/0
   # except:
    #    print("Division by zero")

# 3
# Yes Try can come with finally

#4
# Except handles all types of exceptions

#5
#Except IOError - handles I/O exceptions
#Except ZeroDivisionError - handles division by zero

#6
My_file=open("C:\\Users\\Rikman\\Documents\\Devops\\words.txt",'w')
My_file.write("Einat")
My_file.close()

#9
My_file=open("C:\\Users\\Rikman\\Documents\\Devops\\words.txt",'r')
content = My_file.read()
print(content)
My_file.close()

#10
my_file2 = open("C:\\Users\\Rikman\\Documents\\Devops\\words.txt",'w',encoding='utf-8')
my_file2.write("עינת")
my_file2.close()

my_file2 = open("C:\\Users\\Rikman\\Documents\\Devops\\words.txt",'r',encoding='utf-8')
content = my_file2.read()
print(content)




