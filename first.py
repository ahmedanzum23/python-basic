# basic of pyhton

# name='ahnaf ahmed anzum'
# age='22'
# is_age=True
# print(name)
# print(age)
# print(is_age)

# taking input

# name= input("what is your name ?")
# print("hello"+" "+name)


# type conversion

# old_age = input("what is your age ?")
# new_age =int(old_age)+2
# print(new_age)

# age =str(18)
# print(age)

# sum calculation

# num1= input("please enter your first number")
# num2=input("please enter your second number")
# sum = int(num1)+int(num2)
# print(sum)


# string 

# name= "ahnaf ahmed anzum"
# print(name.upper())
# print(name)

# second_name= "ahnaf ahmed roktim"
# print(second_name.find('r'))


# third_name= "i am hulk"
# print(third_name.replace('i am hulk', 'i am anzum'))
# print(third_name)

# keywords

# fourth_name ="i am black widow"
# print('widow'in fourth_name)


# math mathical operations
# print(5/2)
# print(5//2)
# print(5%2)
# print(5*2)
# print(5**2)

# operator precedence
# i=2
# i=+2
# i+=2
# i-=2
# i*=2
# print(i)

# powerful operations

# result= 10+2*3
# print(result)


#comparision operator
# print(3==3)
# print(3==2)
# print(3<2)
# print(3>2)
# print(3 !=3)



# logical operations
# or and not these 3 type of conversations

# print(1>2 or 3>2)  
# or always print true mostly

# print(1>2 and 3>2)
# and priority always false

# print(not 1>2)
# print(not 10>20)
# print(not 20>10)
#not always makes true false and false true


# if else conditions
# age=1

# if age>=18:
#     print('you are adult you can go now')
#     print('you can go for vote now')
# elif age<18 and age>3:
#     print('you are in school now')


# else:
#     print('you are child')


# num=20

# if num>50:
#     print("you are pass successfully")
#     print('you can go for walk')

# elif num>33:
#     print("you are pass somehow")
#     print("you need improvement")

# else: 
#     print("you are failled sorry")
#     print('you need an improvement')         



# mini project

# 

# num1=input("please enter your first number:")
# operator=input('please enter your operator like (+,-,*,/,%)')
# num2=input("please enter your second number")

# num1=int(num1)
# num2=int(num2)

# if(operator=='+'):
#     print(num1+num2)
# elif(operator=='-'):
#     print(num1-num2)
# elif(operator=='*'):
#     print(num1*num2)
# elif(operator=='/'):
#     print(num1/num2)         
# elif(operator=='%'):
#     print(num1%num2)       
# else:
#     print("you are nothing ")    


# range

# your_choise=range(15)
# print(your_choise)


    #while looping 


# i=1
# while(i<=10):
#     print(i*'anzum')
#     i=i+1



# j=10
# while(j>=1): #j<=1
#     print(j*'anzum')
#     j=j-1    



# for loop
# for item in range(5):
#  print(item+1)

# for anzum in range(7):
#     print(anzum+1)

# for roktim in range(10):
#     print(roktim+1)


# array in python

# number=[1,2,3,4,5,6,7,8,9,10]
# print(number[1])
# print(number[5:8])
# print(number[-5])
# (-) er khetre 0 theka start hobe nah  1 theka start hbe
# number.append(11)
# print(number)
# number.insert(0, 0)
# print(number)
# print(7 in number)
# print(12 in number)
#for loop with kist
# print(len(number))
#while loop for list
# i=0
# while i<len(number):
#     print(number[i])
#     i=i+1

# number.clear()
# print(number)   


# students=['ahnaf','ahmed','roktim','anzum']

# for student in students:
#     if student=='roktim':
#         break
#     print(student)



# number=['shoron' ,'shazin', 'shornab', 'badhon']

# for oka in number:
#     if number=='shornab':
#         break;
#     print(oka)  


# tupple
# marks=(100,200,300,400,400,400,400,800,900,1)
# print(marks.count(400))
# print(marks.index(400))

# ()-tupple [not changeable]
# []=list  [array]
#{}=set



#dictonary
# marks={"bangla":80, 'chemistry':90, 'physics':70}
# print(marks)
# print(marks['bangla'])
# marks['biology']=98
# print(marks)
# marks['physics']=80
# print(marks)


#function
#in build function= int, str, boolean
# import math
# print(dir(math))


""" def  print_sum(first,second):
 print(first+second)
 print(first-second)

print_sum(10,20) 
"""