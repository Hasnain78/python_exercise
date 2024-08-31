# 1. Write a program to generate Arithmetic Exception without exception handling  

a = 10
b = 0
print (a/b)
----------------------------------------------------------------------------------
>>>> ZeroDivisionError: division by zero

****************************************************************************************************************************************

# 2. Handle the Arithmetic exception using try-catch block  
  
a=10
b=0
try:
  print(a/b)
except:
  print('Arithmetic exception')
----------------------------------------------------------
>>>> Arithmetic exception

***************************************************************************************************************************************

# 3. Write a method which throws exception, Call that method in main class without try block  

class excep:
  def div(self,a,b):
    if (b==0):
      raise Exception('Arithmetic exception')
    else:
      print(a/b)

a=excep()
a.div(10,0)
----------------------------------------------------------------------------------------------
>>>> Exception: Arithmetic exception


***************************************************************************************************************************************

# 4. Write a program with multiple catch blocks  
  
try:
  a=10
  b=0
  print(a/b)
except ZeroDivisionError:
  print('Zero Division Exception')
except ArithmeticError:
  print('Arithmetic Exception')
-------------------------------------------------
>>>> Zero Division Exception

***************************************************************************************************************************************

# 5. Write a program to throw exception with your own message  
  
a=10
b=0
try:
  print(a/b)
except:
  print('This is Exception error')
-------------------------------------------------
>>>> This is Exception error

***************************************************************************************************************************************

# 6. Write a program to create your own exception  

class custom(Exception):
  def __init__(self,msg):
    self.msg=msg
    super().__init__(self.msg)

def check(value):
  value<0
  raise custom('Value can not be Negative')

try:
  check(-9)
  print(value)
except custom as e:
  print('caught an error:',e)
---------------------------------------------------
>>>> caught an error: Value can not be Negative

***************************************************************************************************************************************

# 7. Write a program with finally block  

try:
  a=10
  b=0
  print(a/b)
except Exception as e:
  print(e)
finally:
  print('This is finally block, It will run ')
-----------------------------------------------
>>>>  division by zero
      This is finally block, It will run 

**************************************************************************************************************************************

# 8. Write a program to generate Arithmetic Exception  
        
a=10
b=0
try:
  print(a/b)
except Exception as e:
  print('Caught error:',e)
------------------------------------------------------
>>>>  Caught error: division by zero

*************************************************************************************************************************************

# 9. Write a program to generate FileNotFoundException 

try:
  a=open('t.txt')
except FileNotFoundError:
  print('File not found')
-------------------------------------------------------
>>>>  File not found

*************************************************************************************************************************************

# 10. Write a program to generate ClassNotFoundException  
  
try:
  a=funn()
except Exception as e:
  print('Class not found:',e)
--------------------------------------------------------
>>>>  Class not found: name 'funn' is not defined

*************************************************************************************************************************************
# 11. Write a program to generate IOException  

try:
  c = open("so.txt")
  try:
    c.write("Hello, python")
  except:
    print("An exception occurred")
  finally:
    c.close()
except Exception as e:
  print("Something went wrong when writing to the file:",e)
------------------------------------------------------------
>>>>  Something went wrong when writing to the file: [Errno 2] No such file or directory: 'so.txt'

*************************************************************************************************************************************

# 12. Write a program to generate NoSuchFieldException 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

try:
  person = Person("Alice", 30)
  age = getattr(person, "job")  # Try to access a non-existent field
except AttributeError as e:
  print("Caught an error:", e)
---------------------------------------------------------------------
>>>>  Caught an error: 'Person' object has no attribute 'job'

*************************************************************************************************************************************
