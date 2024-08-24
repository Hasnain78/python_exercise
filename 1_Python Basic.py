# 1. Write a program to print your name.
print('Hasnain Ansari')
--------------------------------------------
>>>  Hasnain Ansari


***************************************************************************************************************************************
# 2. Write a program for a Single line comment and multi-line comments
#this line is single line comment
'''this is 
  multi line 
  comment'''
--------------------------------------------------------------------------
>>>  this is \n multi line \n comment


***************************************************************************************************************************************

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
a=10
print(type(a))
b=True
print(type(b))
c='This is string'
print(type(c))
d=10.5
print(type(d))
--------------------------------------------------------------------------------------------------------------------
>>>  <class 'int'>
      <class 'bool'>
      <class 'str'>
      <class 'float'>

***************************************************************************************************************************************


# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
a=20
def fun():
  print('in fun()',a)
def fun2():
  a=750
  print('in fun2()',a)
def fun3():
  a=370
  print('in fun3()',a)
def fun4():
  global a
  a=2
  print('in fun4()',a)  


print('global',a)
fun()
print('global',a)
fun2()
print('global',a)
fun3()
print('global',a)
fun4()
print('global',a)
----------------------------------------------------------------------------------------------------------------------------
>>>  global 20
      in fun() 20
      global 20
      in fun2() 750
      global 20
      in fun3() 370
      global 20
      in fun4() 2
      global 2


*****************************************************************************************************************************************
  
#6. Write a  program to print even number between 10 and 20 using while
a=10
b=20
while a<=b:
  if a%2==0:
    print(a)
  a+=1
  -----------------------------------------------------------------------------
>>>  10
      12
      14
      16
      18
      20

*****************************************************************************************************************************************
#7. Write a program to print 1 to 10 using the do & while loop statement.
a=1
while True:
  print(a)
  a+=1
  if a>10:
    break
-----------------------------------------------------------------------------
1
2
3
4
5
6
7
8
9
10

***************************************************************************************************************************************

# 8. Write a program to find Armstrong number or not
a=int(input('enter any number '))
def armstrong():
  length=len(str(a))
  sum=0
  for i in str(a):
    sum+=int(i)**length
  if sum==a:
    print(a ,' is armstrong number')
  else:
    print(a ,' is not armstrong number')
      
armstrong()
--------------------------------------------------------------
>>>  enter any number 345
      345  is not armstrong number

***********************************************************************************************
# 8. Write a program to find Armstrong number or not
a=int(input('enter any number '))
sum=0
temp=a
while temp>0:
  length=len(str(a))
  digit=temp%10
  sum+=digit**length
  temp//=10
if a==sum:
    print(a,'is armstrong number')
else:
    print(a,'is not armstrong number')
--------------------------------------------------------------
>>>  enter any number 153
      153 is armstrong number

**********************************************************************************************************************************

# 9. Write a program to find the prime or not. 
a=int(input('enter any number '))
def prime():
  if a>1:
    for i in range(2,a):
      if a%i==0:
        print(a,'is not prime number')
        break
    else:
      print(a,'is prime number')
  
prime()
--------------------------------------------------------
>>>  enter any number 73
      73 is prime number

**********************************************************************************************************************************

 #10. Write a program to palindrome or not.
a=int(input('enter any number'))
temp=a
reverse=0
while temp>0:
  digit=temp%10
  reverse=reverse*10+digit
  temp=temp//10
if reverse==a:
  print(a,'is palindrome number')
else:
  print(a,'is not palindrome number')
--------------------------------------------------------
>>>  enter any number123
      123 is not palindrome number

*********************************************************************************
a=int(input('enter any number'))
def palindrome():
  reverse=0
  temp=a
  while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
  if reverse==a:
    print(a,'is palindrome number')
  else:
    print(a,'is not palindrome number')
palindrome()
--------------------------------------------------------
>>>  enter any number121
      121 is palindrome number

************************************************************************************************************************************
# 11. Program to check whether a number is EVEN or ODD using switch
a=int(input('enter any number '))
if a%2==0:
  print(a,'is even number')
else:
  print(a,'is odd number')
----------------------------------------------------------------------------
>>>  enter any number 67
      67 is odd number

************************************************************************************************************************************
# 12. Print gender (Male/Female) program according to given M/F using switch
a=input('enter Male/Female ')
if a=='M':          #or if a.upper()='M'
  print('Male')
elif a=='F':        # or if a.upper()='F'
  print('Female')
else:
  print('Invalid input')
----------------------------------------------------------------------------------
>>>  enter Male/Female m
      Male

************************************************************************************************************************************
