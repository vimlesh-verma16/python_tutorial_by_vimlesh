# PascsalCase = EmployeeName
# camelCase = employeeName
# Lists are slightly faster than sets when you just want to iterate over the values. Sets, however, are significantly faster than lists if you want to check if an item is contained within it. They can only contain unique items though

'''type casting the is the way of converting one datatype to other .'''

# a="33"
# print(type(a))
# a=int(a) #this is typecasting
# print(type(a))
# print(a+5)

''' INPUT FUNCTION'''
# a= input("enter the number :")
# print(type(a))
# a=int(a)  #typecasting
# print(type(a))
# print(a)

''' STRING SLICING'''
# greeting="goodmorning"
# print(greeting[0:1])
# name="harry"
# c=greeting+name #string concatinate
# print(c)
# print(name[2])
# print(name[0:4])

'''STRING FUNCTION'''
# print("hello world its py ".istitle())
# print("hello world how are u its py".split("world"))
# print("0".isalpha())
# print("hello world its pyczcz2434 ".isnumeric())
# print("hello world its pyczcz2434 ".isupper())
# print("hello world its py ".find('its'))
# story="once upon a time there was a good coder named as harry"
# print("the length of story is :",len(story))
# print(story.startswith("once"))
# print(story.count("a"))
# print(story.replace("harry","code with harry"))
# s='hooo'
# print(s.replace("h",""))

#printing value with ascii
# print(ord('A'))
# print(chr(100))

'''ESCAPE SEQUENCES'''
# sentence="harry is\tgood coder,\nhe is a\\youtuber."
# print(sentence)

'''Python Collections (Arrays)'''
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered and changeable. No duplicate members.

'''CREATING A LIST '''
# a=[2,"vimmu",44,55.5,55,True]
# print(a)
# a[0]=99 #chaning the value of list
# print(a)

'''LIST SLICING'''
# friends =["vimlesh","vimmu","harry","divya",455]
# #         ,-5      ,  -4    , -3    , -2   ,-1
# print(friends[0:2]) #it includes 0 but excludes 2
# print(friends[-4:]) #it prints last four values

'''LIST METHODS'''
# x=[1,2]
# y=[3,4]
# li=['x','y',2,4,5,2,2,2,2,2,2,2,0]
# t=li.copy()
# print(list)
# list=['vimmu','harry']
# print(" ".join(list)) #another way to print list data
# fruit=["pineapple","orange","cherry","bannana"]
# print(fruit)
# fruit.append("anything")
# print(fruit)
# print(fruit.index('cherry'))
# x=list.count(2) #counting the occurences
# list.clear() #removes all element from the list
# list.sort() #sort the list in ascending order
# list.reverse()    #reverse the current list
# list.append(22) #add 22 at the end of the list
# list.insert(2, 100) # insert element at index 2
# list.pop(1) # removes element at index 1
# list.remove(2) # remove elemnt 2 from the list
# list.remove(2)  # remove another elemnt 2 from the list

'''iterate over 2+ li at the same time '''
# name=['jack','john']
# animal=['tiger','lion']
# z=zip(name,animal)
# for name,animal in z:
#     print(name,"has",animal)

#---------------------------------------------
''' TUPPLE '''
# the main differnce between a tuple and list is we cannot change tuple values
# t=(2,9,0,1,12)
# print(t)
# print(t.count(2)) #counting the numkber of 2 in tuple
# print(t.index(0)) #printing the ind3ex of 0
# print(t[2]) #printing the element
# t1=(1,) # printing the tuple with single element
# print(t1)

'''we cannot add item or delete item from tuple we can do it by changing tuple to list and vice versa'''
# x=('a','b','c','d')
# print(x[1:4])
# y=list(x)
# y.append("e")
# z=tuple(y)
# print(z)
# s= "".join(x) # converting a tuple into string
# print(s)

'''DICTIONARY'''  # collection of key :value pairs, it is unordered,it is mutable

# myDict ={
#     "harry": "he is coder",
#     "vimlesh": "he is one of the learner",
#     22:333,
#     "myinfo": {
#         "phone": "903003039"
#     },
# }
# myDict[0]=[22,3,4]
# print(myDict["myinfo"]["phone"])
# print(myDict)


'''DICTIONARY METHODS'''
# print(list(myDict.keys())) #prints the keys of dictionary
# print(list(myDict.values())) #prints the value of dictionary
# print(myDict.items())   #prints the (key:value) of dictionary
# updateDict ={
#     "striver":"a cp"
#     "lavsh" :"friend"
# }
# myDict.update(updateDict)
# print(myDict)
# print(myDict.get("harry"))
# print(myDict.["harry"])
# the differnce between them is
# print(myDict.get("harry2")) #returns none as harry2 is not present in the dict
# print(myDict.["harry2"]) #it throws an error as hrar2 is not present bin dict that why we avoid using this method


'''More example in dictionary'''
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(car.get("model"))
# print(car.items()) #Get a list of the key:value pairs
# print(car)
# car['color']='red' # adding an item
# Check if "model" is present in the dictionary:
# if 'brand' in car:
#     print("yes it is present in dictionary")
# del car # completely deletes the dictionary
# car.clear() # it empties the dictionary
# print(car)


'''loops in dictionary'''
# for x in car:
#     print(x) #Print all key names in the dictionary, one by one:
# print(car[x]) #Print all values in the dictionary, one by one:

# for x in car.keys():
# for x in car.values():
# for x,y in car.items():
#     print(x,y)

# car_copy=car.copy()
# print(car_copy)

'''SETS IN PYTHON '''  # set is a collection of non-repeatative items,it is non-mutable ,it is unorderd ,it is unindexed .
# important = this syntax will create empty dictonary and not an sets
# a={}
# print(type(a))

# an empty set can be created by using
# b=set()
# print(type(b))

# e=set{1,2,3,"3"}

# adding values in sets
# b.add(2)
# b.add(4)
# b.add(3)
# b.add(6)
# print(b)
# print(len(b)) # prints length of set b
# b.remove(3) #removes 3 from set b
# print(b.pop())

# sets={2,2,2,1,1,9,4,7,4,'he'}
# print(sets)
# print('he' in sets) #checking if a specific element exits in the sets

# a={2,4}
# print(a.issubset(sets))
# print(a.issubset(a))
# y=a.copy()
# y.add(3)
# y.remove(4)
# print(y)

'''  ARRAY's  '''
# from array import*
# num =array('i',[1,2,3,23,2,3,4,45])
# print(num.count(2)) # counting the occurences
# for i in range(len(num)):
#     print('index',[i],"=",num[i])
# num.append(22) # adding element at the end of array
# a=array('i',[9,8])
# num.extend(a) # joining arrays at the end of other
# num.remove(1) # removing the first occurence of 1
# num.remove(2) # removing the first occurence of 2
# num.reverse()    # revering the order of array
# n= num.index()
# num.remove(n)
# for i in range(len(num)):
#     print('index',[i],"=",num[i])

'''CONDITIONAL EXPRESSION '''
# if elif else LADDER

# a= 33
# if (a>12):
#     print("the value of a is greater than 12")
# elif(a>1):
#     print("the value of a is greater than 1")
# elif(a>40):
#     print("the value of a is greater than 40")
# elif(a>10):
#     print("the value of a is greater than 10")
# else:
#     print("the value of a is greater than 0")


# MULTIPLE IF STATEMENT
# a =25
# if (a>12):
#     print("the value of a is greater than 12")
# if(a>1):
#     print("the value of a is greater than 1")
# if(a>40):
#     print("the value of a is greater than 40")
# if(a>10):
#     print("the value of a is greater than 10")
# else:
#     print("the value of a is less than 10")

'''WHILE LOOP '''

# fruits =["banana","cherry","mango","cherry","orange","kiwi"]
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

''' FOR LOOP'''
# fruits =["banana","cherry","mango","cherry","orange","kiwi1"]
# for item in fruits:
#   print(item)

# range function
# for i in range(1,20):
#     print(i)


'''PRINTING TABLE WITH FOR LOOP'''
# num =int(input("Enter the number you want to print the table for: "))
# for i in range(1,11):
#   print(str(num)+" x "+str(i) +" =", str(num*i) )
# print(f"{num}x{i}={num*i}")
'''FOR LOOP WITH ELSE '''
# for i in range(8):
#     print(i)
#     # break
# else:
#     print("else is used in for loop")

'''BREAK STATEMENT '''
# for i in range(10):
#     print(i)
#     if i==5 :
#      break
# else:
#     print("the loop executed succesfully")


'''CONTINUE STATEMENT '''
# for i in range(10):
#     if i==4:
#         continue
#     print(i)
# else:
#     print("the loop executed succesfully")

''' PASS STATEMENT '''

# if i>0:
#     pass

# print("hello how are you")

#--------------------------------------------------------

'''FUNCTIONS '''
# def great(num1, num2, num3):
#     if(num1 > num2 and num1 > num3):
#         return num1
#     elif(num2 > num1 and num2 > num3):
#         return num2
#     else:
#         return num3


# print(great(422, 222, 65))

#----------------------------------------------------------
'''RECURSION EXAMPLE'''

# def sum(n):
#     if (n == 0 or n == 1):
#         return 1
#     return n+sum(n-1)


# print(sum(4))

# --------------------------------------------------------------

'''File I/O '''
# use open function to read the content of the file
# f=open('sample.txt','r')
# # d=f.read(10) # read first 10 character

# d=f.readline() # read first line
# print(d)
# d=f.readline() #read second line  and soo on .
# print(d)
# f.close()

# writing to a file
# f=open('another.txt','w')
# f.write("hello this is new file ")
# f.close()

# appending to a file
# f=open('another.txt','a')
# f.write("i am appending")
# f.close()

# Another method for writing into a file
# with open('another.txt','r') as f:
#     a=f.read()
# with open('another.txt','w') as f:
#     a=f.write(' hello i am writin')
# with open('another.txt','r') as f:
#     a=f.read() #it automatically closes the file
# print(a)

''' use of File I/O for game score '''
# def game(prev,score):
#     f=open('highscore.txt','w')
#     if score>prev:
#         f.write(str(score))
#         f.close()
#     else:
#         f.write(str(prev))
#         f.close()

# game(3,2)
# f=open('highscore.txt')
# d=f.read()
# print(d)
# f.close()

'''Generating a table for given range with the use of I/O '''
# for i in range(2,21):
#     with open(f"tables/table_of_{i}.txt","w") as f:
#       for j in range(1,11):
#           f.write(f"{i}X{j}={i*j}\n")

''' write a program to update a word with ######'''

# with open("poem.txt") as f:
#     content=f.read()
#     content=content.replace('donkey',"######")

# with open("poem.txt",'w') as f:
#     f.write(content)

#---------------------------------------------------------------

''' Object Oriented programming '''
# class Employee:
#     company='Google'
#     salary=100

# harry=Employee()
# rajni=Employee()
# # Employee.company='youtube'
# # print(harry.company)
# # print(rajni.company)
# # creating instance attribute for both the objects
# harry.salary=300
# # rajni.salary=400
# print(harry.salary)
# print(rajni.salary)

# --------------------------------------------------------------------
# class Employee:
#     company='youtube'
#     def getsalary(self,signature):
#         print(f'Salary for employee working in {self.company} is {self.salary}\n{signature}')

#     @staticmethod
#     def greet():
#         print("Goodmorning, Sir")

# harry=Employee()
# harry.salary=1000
# harry.getsalary('thanks')  #it is same as Employee.getsalary(harry)
# harry.greet()  # we want Employee.getsalary()
# ----------------------------------------------------------------------
''' special method or init function(Constructor)'''
# class Employee:
#     company='youtube'

#     def __init__(self,name,salary,subunit):
#         self.name=name
#         self.salary=salary
#         self.subunit=subunit
#         print("Employee constructor is initilised: ")

#     def getDetails(self):
#         print(f'employee name is {self.name} and his salary is {self.salary} and his unit is {self.subunit}')

#     def getsalary(self,signature):
#         print(f'Salary for employee working in {self.company} is {self.salary}\n{signature}')

#     @staticmethod
#     def greet():
#         print("Goodmorning, Sir")

# harry=Employee('harry',100,'Gmail')
# harry.getDetails()

''' inheritance in Oops  '''
# single level inheritance
# class Employee:
#     company='Google'
#     def showDetail(self):
#         print("this is an employee")
# class Programmer(Employee):
#     language='python'
#     def showDetail(self):
#         print("this is programmer")

# e=Employee()
# p=Programmer()
# e.showDetail()
# p.showDetail()
# print(p.company)

''' multiple inheritance '''
# class Employee:
#     company='Google'

# class Freelancer:
#     level=1
#     company='youtube'
#     def upgrade(self):
#         self.level=self.level+1

# class Programmer(Employee,Freelancer):
#     language='python'

# p=Programmer()
# p.upgrade()
# print(p.level)

'''multilevel inheritance with super function'''


# class Person:
#     country = 'india'

#     def __init__(self):
#         print("initialising person....")

#     def takebreath(self):
#         print("i am person and i em breating ")


# class Employee(Person):
#     company = 'honda'

#     def __init__(self):
#         super().__init__()
#         print("initialising Employee....")

#     def takebreath(self):
#         # super().takebreath()
#         print("i am employee and i am heavily breathing ")


# class Programmer(Employee):
#     company = "fiverr"

#     def __init__(self):
#         # super().__init__()
#         print("initialising Programmer....")

#     def takebreath(self):
#         # super().takebreath()
#         print("it is Programmer class ")

# p=Person()
# p.takebreath()

# e=Employee()
# e.takebreath()


# pr = Programmer()
# pr.takebreath()

'''Class Method or changing the attribute of class'''
# class Employee:
#     company="Google"
#     salary=100
# def changesalary(self,sal):
#     self.__class__.salary=sal  #__class__ is called dunder method or class
#     print(self.salary)

#     @classmethod
#     def changesalary(cls,sal):
#         cls.salary=sal
#         print(cls.salary)

# e=Employee()
# print(e.salary)
# e.changesalary(300)
# print(e.salary)

'''class decorator or getters or setters '''


# class Employee:
#     salary = 5700
#     bonous = 300
#     # totalsalary=6000

#     @property  # it is a getter function
#     def totalsalary(self):
#         return self.salary+self.bonous

#     @totalsalary.setter  # it is setting some value
#     def totalsalary(self, val):
#         self.bonous = val-self.salary


# e = Employee()
# print(e.totalsalary)
# e.totalsalary =65000
# print(e.bonous)
# print(e.salary)

'''operator overloading '''


# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print('lets add')
#         return self.num+num2.num

#     def __mul__(self, num2):
#         print('lets multiply')
#         return self.num*num2.num

#     def __str__(self):
#         return f'this is decimal number {self.num}'

#     def __len__(self):
#         return 1

# n1 = Number(4)
# n2 = Number(6)
# sum = n1+n2
# sum = n1*n2
# print(sum)


# n=Number(9)
# print(n)
# print(len(n))


# -----------------------------------------------------------------------
'''Advanced Python'''

# EXCEPTION HANDLING
''' TRY and EXCEPT '''

# while(True):
#     print("Press q to quit")
#     a = input("Enter a number: ")
#     if a == 'q':
#         break
#     try:
#         print("Trying...")
#         a = int(a)
#     except Exception as e:
#         print(f"Your input resulted in {e}")
#         print("Thanks for playing this game")
# -------------------------------------------------------------------------------------------
''' Try with Else Clause'''
# try:
#     i = int(input("Enter a number: "))
#     c = 1/i
# except Exception as e:
#     print(e)
# else:
#     print("We were successful")
# -----------------------------------------------------------------------------------------
''' Try Except Finally'''

# try:
#     i = int(input())
#     c = 1/i
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print("We are done")

# print("Thanks for using the program")
# ------------------------------------------------------------
'''Enumerate '''  # it is used to print index of element in any iterator
# list=[1,22,33,43242,'vimmu',11.1,True]

# for index,item in enumerate(list):
#         print(index,item)
# --------------------------------------------------------------
'''LIST Comprehension '''
# from operator import itemgetter


# a=[2,33,22,3,2,6,7,8]
# b=[i for i in a if i%2==0]
# print(b)
# --------------------------------------------------------------------------------

'''Lambda Function  or anonmous function'''
# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# result=[]
# people.sort(key=lambda x: (-x[0], x[1]))
# print(people)
# for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
#     result.insert(k, [h, k])
# print(result)


# fun=lambda a:a+5
# square=lambda a:a**2
# sum=lambda a,b,c :a+b+c
# print(fun(2))
# print(square(3))
# print(sum(2,3,5))

# -----------------------------------------------------------------------------------
'''Map function '''
# def square(num):
#     return num**2

# l=[1,3,4]
# print(list(map(square,l)))
# -----------------------------------------------------------------------------------
''' Filter Function '''
# def greater_then_5(num):
#     if num>5:
#         return True
#     else:
#         return False

# l=[2,6,7,8,9,14,33,22]
# print(list(filter(greater_then_5,l)))
# -----------------------------------------------------------------------------------
'''Reduce function '''
# from functools import reduce
# l=[1,2,3]
# sum=lambda a,b:a+b
# r=reduce(sum,l)
# print(r)
# ---------------------------------------------------------------------
'''For Cp'''
# import sys
# sys.stdout=open("cp/output.txt",'w')
# sys.stdin=open("cp/input.txt",'r')
# -----------------------------------------------------------

'''Advanced python'''

# from operator import itemgetter, attrgetter
# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# l=sorted(student_tuples, key=itemgetter(2))
# print(l)


# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# s = sorted(x.items(), key=itemgetter(1))
# print(s)
# ------------------------------------------------------

# Python code to demonstrate the working of
# zip_longest()

# from itertools import zip_longest
# using zip_longest() to combine two iterables.
# print ("The combined values of iterables is  : ")
# print (*(zip_longest('GesoGes', 'ekfrek', fillvalue ='' )))

# another way to write is
#  return ''.join(a + b for a, b in zip_longest(w1, w2, fillvalue=''))
# -----------------------------------------------------------------

# short trick to join string of array using map and * [very important]

# arr = ['sunday', 'monday', 'tuesday', 'wednesday']

# # without using asterisk
# print(' '.join(map(str,arr)))

# # using asterisk
# print (*arr)


# ----------------------------------------------------------------

# x=10
# y=5
# ans=divmod(x,y)
# print(ans)

# -------------------------------------------------------------
'''Printing binary number '''
# for i in range(1,5):
#     t=int(bin(i).split('0b')[1])
#     print(t)

#------------------------------------------------------------------
'printing all subarray with iterative call '
# def subArray(arr, n):
#     # Pick starting point
#     for i in range(0,n):
 
#         # Pick ending point
#         for j in range(i,n):
 
#             # Print subarray between
#             # current starting
#             # and ending points
#             print(arr[i:j+1])
 
             
# arr = [1, 2, 3, 4]
# n = len(arr)
# subArray(arr, n);
#-----------------------------------------------------------------------