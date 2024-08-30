# prompt: 1. Create a program to create two class. 
# 1.1. Create a constructor and a method for each class  

# file_one.py
class ClassOne:
  def __init__(self, name):
    self.name = name

  def method_one(self):
    print(f"Hello! I am {self.name} from ClassOne")

# file_two.py
class ClassTwo:
  def __init__(self, age):
    self.age = age

  def method_two(self):
    print(f"My age is {self.age} from ClassTwo")

#  1.2. Create a __init__.py for adding all packages
# __init__.py 
# This file should be empty and placed in the same directory as file_one.py and file_two.py

# prompt: 1.3. Import the respective packages 

# main.py
import file_one 
import file_two


# prompt: 1.4. Call each class by creating an object to it  

object_one = ClassOne("Alice")
object_two = ClassTwo(30)

-------------------------------------------------------------------------------------------------------
>>>>  Hello! I am Alice from ClassOne
      My age is 30 from ClassTwo

************************************************************************************************************************************
