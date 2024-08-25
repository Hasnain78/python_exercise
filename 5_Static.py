# 1. Define a static variable and access that through a class 
class python:
  variable=200
  
print(python.variable)
-----------------------------------------------------------------
>>>>  200

*****************************************************************************************************************************************
# 2. Define a static variable and access that through a instance 
class python:
  variable=200

instance=python()
print(instance.variable)
-----------------------------------------------------------------
>>>>  200

*****************************************************************************************************************************************
# 3. Define a static variable and change within the instance 
class java:
  element=300

k=java()
k.element=7000
print(k.element)
print(java.element)
-----------------------------------------------------------------
>>>>  7000
      300

*****************************************************************************************************************************************
# 4. Define a static variable and change within the class 
class final:
  element=10

final.element=40000
print(final.element)
-----------------------------------------------------------------
>>>>  40000
