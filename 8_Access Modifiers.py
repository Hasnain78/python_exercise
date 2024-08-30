'''1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. 
Call the private method in main method.  

Create a sub class and try to access the private fields and methods from sub class.   

2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package. 

Also, Access the PROTECTED fields and methods from child class located in a different package 

Access the PROTECTED fields and methods from any class in different package   

3. Create a class with PUBLIC fields and methods.   

Access the public methods and fields from any class in the same package or different package.  '''

class First:
  a=None
  _b=None
  __c=None

  def __init__(self,a,b,c):
    self.a=a
    self._b=b
    self.__c=c

  def public_member(self):
    print('Public Data Member',self.a)
  
  def protected_member(self):
    print('Protected Data Member',self._b)

  def private_member(self):
    print('private data member',self.__c)

# private can't be accessed in object/sub class
  def access_private(self):
    self.private_member()

class Sub(First):
  #constructor
  def __init__(self,a,b,c):
    First.__init__(self,a,b,c)

  def access_protected(self):
    self.protected_member()

obj=Sub('m',200,'m')

obj.public_member()
obj.access_protected()
obj.access_private()

# Object can access protected member
print("Object is accessing protected member:", obj._b)
 
# object can not access private member, so it will generate Attribute error
#print(obj.__c)

>>>>  Public Data Member m
      Protected Data Member 200
      private data member m
      Object is accessing protected member: 200

*********************************************************************************************************************************
