


#This code checks if a number is positive, negative or zero

x = int(input("enter a number :")) #Taking input from user
if (x > 0): #Checking if the number is positive
    print("Given number is positive") 
    
elif(x == 0): #Checking if the number is zero
        print("Given number is zero")
        
elif(x < 0): #Checking if the number is negative
    print("Given number is negative")



#This code checks if a student passed or failed in a subject

x = int(input("enter midterm exam grade :")) #Taking midterm exam grade as input
y = int(input("enter final exam grade :")) #Taking final exam grade as input

if (y < 60): #Checking if the student failed in the final exam
    print("failed")
    
elif (x*0.4+y*0.6<55): #Checking if the student's grade point failed in the subject
    print("failed")
    
else:
    print("passed") #Checking if the student passed
    



#This code checks which number is the biggest

x = int(input("Enter x value :")) #Taking input from user
y = int(input("Enter y value :")) #Taking input from user
z = int(input("Enter z value :")) #Taking input from user

if (x>y & x>z): #Checking if x is the biggest
    print("x is the biggest")
    
elif (z>y & z>x): #Checking if z is the biggest
        print("z is the biggest")
        
elif (y>z & y>x): #Checking if y is the biggest
        print("y is the biggest")




#This code checks if a number is divisible by 6

x = int(input("enter a number :")) #Taking input from user

if (x%6==0): #Checking if the number is divisible by 6
    print("number is divisible by 6 :")
    
else: #Checking if the number is not divisible by 6
    print("number is not divisible by 6 :")
    




#This code checks which grade the student has

x =int(input("enter a grade :")) #Taking input from user

if (100>=x>90): #Checking if the grade is AA
    print("AA")
    
elif (90>x>=85): #Checking if the grade is BA
    print("BA")
    
elif (85>x>=80): #Checking if the grade is BB
    print("BB")
    
elif (80>x>=70): #Checking if the grade is CB
    print("CB")
    
elif (70>x>=60): #Checking if the grade is CC
    print("CC")
    
elif (60>x>=55): #Checking if the grade is DC
    print("DC")
    
elif (55>x>=50): #Checking if the grade is DD
    print("DD")
    
elif (50>x>=40): #Checking if the grade is FD
    print("FD")
    
else: #Checking if the grade is FF
    print("FF")




#This code calculates the salary based on the number of children

x = input("enter the number of workers :") #Taking input from user
y = input("enter the number of children :") #Taking input from user

if y==1: #Checking if the number of children is 1
    print("new salary :",x*1.05)
    
elif y==2: #Checking if the number of children is 2 
    print("new salary :",x*1.10)
    
elif y>=3: #Checking if the number of children is more than 2
    print("new salary :",x*1.15)




#This code performs simple arithmetic operations

print("1:Add 2:Sub 3:Mul 4:Div") #Printing the operation

b = int(input("Enter the first number :")) #Taking first input from user
c = int(input("Enter the second number :")) #Taking second input from user
a = int(input("Enter the operation :")) #Taking operation from user

if a == 1: #Checking if the operation is addition
    print("Addition result :", b+c) 
    
elif a == 2: #Checking if the operation is subtraction
    print("Subtraction result :", b-c)
    
elif a == 3: #Checking if the operation is multiplication
    print("Çarpma sonucu :", b*c)
    
elif a ==4:  #Checking if the operation is division
    print("Bölme sonucu :", b/c)
    
else: #Checking if the operation is invalid
    print("Hatalı seçim")




#This code checks if a point is inside a circle or not

import math #Importing math library

a = int(input("enter a :")) #Taking value of a
b = int(input("enter b :")) #Taking value of b
c = int(input("enter c :")) #Taking value of c
dx = int(input("enter dx :")) #Taking value of dx
dy = int(input("enter dy :")) #Taking value of dy
r = int(input("enter r :")) #Taking value of r
d =abs(a*dx + b*dy + c)/ (a**2 + b**2) #Calculating distance

if (d>r): #Checking if the point is inside the circle
    print("The point is outside the circle")
    
elif(d==r): #Checking if the point is on the circle
    print("The point is on the circle")
     
else: #Checking if the point is inside the circle
    print("The point is inside the circle")






