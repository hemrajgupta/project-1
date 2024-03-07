
# python programme for simple calculator

# function add two numbers

def add(n1,n2):
    return n1+n2

# function subtract two numbers

def subtract(n1,n2):
    return n1-n2

# function multipy two numbers

def multiply(n1,n2):
    return n1*n2

# function divide two numbers

def divide(n1,n2):
    return n1/n2

print("please select operation--\n"\
      "1.add\n"\
      "2.subtract\n"\
      "3.multiply\n"\
      "4.divide\n")

 #take input from user

select = int(input("select operation from 1,2,3,4 : "))
number_1=int(input("enter the first number "))
number_2=int(input("enter the second number "))

if select == 1:
    print(number_1,'+',number_2,'=',add(number_1,number_2))
elif select == 2:
    print(number_1,'-',number_2,'=',subtract(number_1,number_2))
elif select == 3:
    print(number_1,'*',number_2,'=',multiply(number_1,number_2))
elif select == 4:
    print(number_1,'/',number_2,'=',divide(number_1,number_2))
else :
    print("invalid input")
    