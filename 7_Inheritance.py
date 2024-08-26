'''A, B and C are classes  

A is a super class. B is a sub class of A. C is a sub class of B. 

Create three methods in each class, 2 methods are specific to each class and third method (override method) 
should be in all three Classes A, B and C  

Create a class with main method. Create an object for each class A, B and C in main method and 
call every method of each class using its own object/instance.

Call an overridden method with super class reference to B and C class’s objects  

Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members  
 '''

class A:
  def method_a1(self):
    print('Method a1 in class A')

  def method_a2(self):
    print('Method a2 in class A')

  def method_override(self):
    print('Method override in class A')

class B(A):
  def method_b1(self):
    print('Method b1 in class B')
  
  def method_b2(self):
    print('Method b2 in class B')
  
  def method_override(self):
    print('Method override in class B')

class C(B):
  def method_c1(self):
    print('Method c1 in class C')
  def method_c2(self):
    print('Method c2 in class C')

  def method_override(self):
    print('Method override in class C')


def main():
  # creating objects
  obj_A=A()
  obj_B=B()
  obj_C=C()

  # calling methods
  obj_A.method_a1()
  obj_A.method_a2()

  obj_B.method_b1()
  obj_B.method_b2()

  obj_C.method_c1()
  obj_C.method_c2()

  obj_A.method_override()
  obj_B.method_override()
  obj_C.method_override()

main()
------------------------------------------------------------------------------------------------
>>>>  Method a1 in class A
      Method a2 in class A
      Method b1 in class B
      Method b2 in class B
      Method c1 in class C
      Method c2 in class C
      Method override in class A
      Method override in class B
      Method override in class C
