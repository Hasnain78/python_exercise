from abc import ABC , abstractmethod
class Calculator(ABC):
  def __init__(self,a,b):
    self.a=a
    self.b=b
  @abstractmethod
  def add(self):
    pass
  def sub(self):
    return self.a-self.b
  def mul(self):
    return self.a*self.b
  def div(self):
    return self.a/self.b

  def manual(self):
    user_choice=input('enter any operator ')
    if user_choice=='+':
      return self.add()
    elif user_choice=='-':
      return self.sub()
    elif user_choice=='*':
      return self.mul()
    elif user_choice=='/':
      return self.div()


class CLI(Calculator):
  def add(self):
    return self.a+self.b


line=input('enter 2 value ').split()
a=int(line[0])
b=int(line[1])
s=CLI(a,b)
print(s.a)
print(s.b)
s.manual()
---------------------------------------------------------------------------
>>>>  enter 2 value 7 9
      7
      9
      enter any operator +
      16

*************************************************************************************************************************************

''' 
1. Create an abstract class with abstract and non-abstract methods. 

2. Create a sub class for an abstract class. Create an object in the child class for the  abstract class and 
access the non-abstract methods  

3. Create an instance for the child class in child class and call abstract methods

4. Create an instance for the child class in child class and call non-abstract methods 
'''
        
from abc import ABC, abstractmethod
 
class Polygon(ABC): #base class / super class
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Triangle: I have 3 sides")
 
class Pentagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Pentagon: I have 5 sides")
 
class Hexagon(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Hexagon: I have 6 sides")
 
class Quadrilateral(Polygon): #subclass
 
    # overriding abstract method
    def noofsides(self):
        print("Quadrilateral: I have 4 sides")
 
# Driver code
# Creating the objects to call the abstract method.
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()

--------------------------------------------------------------------------------------------------------------
>>>>  Triangle: I have 3 sides
      Quadrilateral: I have 4 sides
      Pentagon: I have 5 sides
      Hexagon: I have 6 sides

***************************************************************************************************************************
