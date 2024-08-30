# 1. Write a class with a default constructor, one argument constructor and two argument constructors. 
# Instantiate the class to call all the constructors of that class from a main class  

class MyClass:
  def __init__(self, arg1=None, arg2=None):
    if arg1 is None and arg2 is None:
      print("Default Constructor")
    elif arg2 is None:
      print("One Argument Constructor")
    else:
      print("Two Argument Constructor")

obj1 = MyClass()
obj2 = MyClass(1)
obj3 = MyClass(1, 2)
---------------------------------------------------------------------------------------------------------
>>>>  Default Constructor
      One Argument Constructor
      Two Argument Constructor

**************************************************************************************************************************************

# 2. Call the constructors(both default and argument constructors) of super class from a child class  

class MyChildClass(MyClass):
  def __init__(self, arg1=None, arg2=None):
    super().__init__(arg1, arg2) # Call the superclass constructor using super()
    if arg1 is None and arg2 is None:
      print("Child Default Constructor")
    elif arg2 is None:
      print("Child One Argument Constructor")
    else:
      print("Child Two Argument Constructor")

obj1 = MyChildClass()
obj2 = MyChildClass(1)
obj3 = MyChildClass(1, 2)
---------------------------------------------------------------------------------------------------------
>>>>  Default Constructor
      Child Default Constructor
      One Argument Constructor
      Child One Argument Constructor
      Two Argument Constructor
      Child Two Argument Constructor

**************************************************************************************************************************************
# 3. Apply private, public, protected and default access modifiers to the constructor
class AccessModifiers:
  def __init__(self):
    print("Public Constructor")

  def _protected_constructor(self):
    print("Protected Constructor")

  def __private_constructor(self):
    print("Private Constructor")

# Public constructor can be accessed directly
obj = AccessModifiers()

# Protected constructor can be accessed using _
obj._protected_constructor()

# Private constructor can be accessed using _classname__
obj._AccessModifiers__private_constructor()
---------------------------------------------------------------------------------------------------------
 >>>> Public Constructor
      Protected Constructor
      Private Constructor


**************************************************************************************************************************************
# 4. Write a program which illustrates the concept of class and instance variables  
class MyClass:
  class_attribute = "This is a class attribute"

  def __init__(self, instance_attribute):
    self.instance_attribute = instance_attribute

# Accessing class attribute
print(MyClass.class_attribute)

# Creating an instance of the class
obj = MyClass("This is an instance attribute")

# Accessing instance attribute
print(obj.instance_attribute)
-----------------------------------------------------------------------------------------
>>>>  This is a class attribute
      This is an instance attribute

**************************************************************************************************************************************
