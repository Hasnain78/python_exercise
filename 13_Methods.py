# 1. Write two methods with the same name but different number of parameters of same type and call the methods

class fun:
  def sum(self,a,b):
    print(a+b)
  def sum(self,a,b,c):
    print(a+b+c)

o=fun()
o.sum(1,2,3)
--------------------------------------------------------------------------------------------------------------
>>>> 6

**************************************************************************************************************************************

# 2. Write two methods with the same name but different number of parameters of different data type and call the methods   

class fun1:
  def sum(self,a,b):
    print(a+b)
  def sum(self,a,b,c):
    print(a+str(b)+c)

a=fun1()
a.sum('1','2','3')
--------------------------------------------------------------------------------------------------------------------------
>>>> 123

**************************************************************************************************************************************

# 3. Write two methods with the same name and same number of parameters of same type    
class fun2:
  def sum(self,a,b):
    print(a+b)
  def sum(self,a,b):
    print(a*b)

b=fun2()
b.sum(1,2)
----------------------------------------------------------------------------------------
>>>> 2

**************************************************************************************************************************************
