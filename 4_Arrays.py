# 1. Write a function to add integer values of an array
a=[10,20,30]
sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
print(sum)
---------------------------------------------------------
>>>  60

****************************************************************************************************************************************
# 2. Write a function to calculate the average value of an array of integers 
a=[10,20,30,40,50]
sum=0
for i in range(len(a)):
  sum+=a[i]
average=sum/len(a)
print(average)
--------------------------------------------------------------------------------
>>>  30.0

****************************************************************************************************************************************

# 3. Write a program to find the index of an array element 
a=[1,34,24,54,31,55,3,3,1,54]
print(a.index(1))
print(a.index(54))
print(a.index(3))
-------------------------------------------------------------
>>>   0
      3
      6

****************************************************************************************************************************************

# 4. Write a function to test if array contains a specific value 
a=[1,2,3,4,54,43,23,15,41,65]
num=int(input('enter the number '))
if num in a:
  print(num,'exist in the list')
else:
  print(num,'does not exist in the list')
--------------------------------------------------------------------
>>>   enter the number 67
      67 does not exist in the list

***************************************************************************************************************************************

# 5. Write a function to remove a specific element from an array 
a=[1,2,3,4,54,43,23,15,41,65]
num=int(input('enter the number '))
if num in a:
  a.remove(num)
  print(a,'\n after removing the element :',num)
else:
  print(num,'does not exist in the list \n',a)
----------------------------------------------------------------------
>>>   enter the number 54
      [1, 2, 3, 4, 43, 23, 15, 41, 65] 
       after removing the element : 54

**************************************************************************************************************************************
# 6. Write a function to copy an array to another array 
a=[1,2,3,4,5,6,7,8]
b=a.copy()
print(b)
----------------------------------------------------------
[1, 2, 3, 4, 5, 6, 7, 8]

**************************************************************************************************************************************
# 7. Write a function to insert an element at a specific position in the array 
a=[1,2,3,4,5,6,7,8,9]
num=int(input('enter the new number '))
pos=int(input('enter the position '))
a.insert(pos,num)
print(a)
------------------------------------------------------------------------------------
>>>>  enter the new number 209
      enter the position 5
      [1, 2, 3, 4, 5, 209, 6, 7, 8, 9]

*************************************************************************************************************************************

# 8. Write a function to find the minimum and maximum value of an array 
a=[1,2,12,32,34,5,77,54,25]
print('minimum value :',min(a),'\t & its position is : ',a.index(min(a)))
print('maximum value :',max(a),'\t & its index position is : ',a.index(max(a)))
------------------------------------------------------------------------------------
>>>>  minimum value : 1 	 & its position is :  0
      maximum value : 77 	 & its index position is :  6

*************************************************************************************************************************************

# 9. Write a function to reverse an array of integer values 
a=[1,2,3,4,5,6,7,8]
a.reverse()
print(a)
-----------------------------------------------------------------
>>>>  [8, 7, 6, 5, 4, 3, 2, 1]

*************************************************************************************************************************************

# 10. Write a function to find the duplicate values of an array 
a=[1,2,3,4,3,5,6,7,5]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
    if a[i]==a[j]:
      print('duplicate value is',a[j])
-----------------------------------------------------------------
>>>>  duplicate value is 3
      duplicate value is 5

*************************************************************************************************************************************

# 11. Write a program to find the common values between two arrays 
a=[1,2,3,4,5,6,7]
b=[2,9,8,5,0,7,10]
for i in range(0,len(a)):
  for j in range(0,len(b)):
    if a[i]==b[j]:
      print('duplicate value is: ',b[j])
--------------------------------------------------------------------
>>>>  duplicate value is:  2
      duplicate value is:  5
      duplicate value is:  7

*************************************************************************************************************************************

# 12. Write a method to remove duplicate elements from an array 
a=[1,2,3,4,5,3,5,7,1]
b=[]
for i in a:
  if i not in b:
    b.append(i)
print(b)
--------------------------------------------------------------------
>>>>  [1, 2, 3, 4, 5, 7]

*************************************************************************************************************************************

# 13. Write a method to find the second largest number in an array 
a=[1,2,3,4,5,3,56,51,76,7,3]
a.sort()
print(a[-2])
--------------------------------------------------------------------
>>>>  56

*************************************************************************************************************************************

# 14. Write a method to find number of even number and odd numbers in an array 
a=[10,20,30,4,5,6,7,8,9]
even=[]
odd=[]
for i in range(0,len(a)):
  if a[i]%2==0:
    even.append(a[i])
  else:
    odd.append(a[i])
print('Even numbers: ',even)
print('Odd numbers: ',odd)
-----------------------------------------------------------------------------------
>>>>  Even numbers:  [10, 20, 30, 4, 6, 8]
      Odd numbers:  [5, 7, 9]
***********************************************************************************************
# 15. Write a method to find number of even number and odd numbers in an array 
a=[10,20,30,4,5,6,7,8,9]
even=[]
odd=[]
for i in a:
  if i%2==0:
    even.append(i)
  else:
    odd.append(i)
print('Even numbers: ',even)
print('Odd numbers: ',odd)

*************************************************************************************************************************************

# 16. Write a function to get the difference of largest and smallest value
a=[20,10,4,60,4,89,7]
a.sort()
print(a[-1]-a[0])
-----------------------------------------------------------------------------------
>>>>  85

*************************************************************************************************************************************

# 17. Write a method to verify if the array contains two specified elements(12,23) 
a=[21,12,34,32,23,54,65,98]
for i in a:
  if i==12:
    print('12 exist in the list')
  if i==23:
    print('23 exist in the list')
--------------------------------------------------------------------------------------
>>>>  12 exist in the list
      23 exist in the list

*************************************************************************************************************************************
# 18. Write a program to remove the duplicate elements and return the new array 
a=[1,2,3,4,5,6,7,4,3,1]
new=[]
for i in a:
  if i not in new:
    new.append(i)
print(new)
--------------------------------------------------------------------------------------
>>>>  [1, 2, 3, 4, 5, 6, 7]

*************************************************************************************************************************************
