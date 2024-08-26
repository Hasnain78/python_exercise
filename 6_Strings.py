# 1. Different ways creating a string
s1='string 1 '
s2="string 2 "
s3='''this
is multi line string 3 '''
s4="""this is
string 4"""
print(s1)
print(s2)
print(s3)
print(s4)
-----------------------------------------
>>>>  string 1 
      string 2 
      this 
      is multi line string 3 
      this is 
      string 4

****************************************************************************************************************************************

# 2. Concatenating two strings using + operator
s1='hi'
s2=',welcome to Python class'
print(s1+s2)
--------------------------------------------------
>>>>  hi,welcome to Python class

****************************************************************************************************************************************

# 3. Finding the length of the string
s='hi,welcome to Python class'
print(len(s))
--------------------------------------------------
>>>>  26

****************************************************************************************************************************************

# 4. Extract a string using Substring
s='hi,welcome to Python class'
s1=s[3:10]
print('extracted: ',s1)
--------------------------------------------------
>>>>  extracted:  welcome

****************************************************************************************************************************************

  # 5. Searching in strings using index()
s='hi,welcome to python class'
find=input('enter the string ')
print(s.index(find))
--------------------------------------------------
>>>>  enter the string py
      14

****************************************************************************************************************************************

  # 6. Matching a String Against a Regular Expression With matches()
import re
# re.match() search for begining values
substr='hi'
string='hi,welcome to python class'
print(re.match(substr,string))
----------------------------------------------------------------------
>>>>  <re.Match object; span=(0, 2), match='hi'>

****************************************************************************************************************************************

# 7. Comparing strings
s='python'
s1='python class'
s2=s
print(s==s1)
print(s!=s1)
print(s2!=s1)
print(s2==s)
--------------------------------
>>>>  False
      True
      True
      True

***************************************************************************************************************************************

# 8. startsWith(), endsWith()
s='hi,welcome to python class'
print(s.startswith('hi'))
print(s.endswith('hi'))
--------------------------------
>>>>  True
      False

***************************************************************************************************************************************

# 9. Trimming strings with strip()
s='s hi,welcome s to python class'
print(s.strip('s'))
print(s.strip('hi'))
print(s.strip('s hi,'))
print(s.strip('class'))
-----------------------------------
>>>>   hi,welcome s to python cla
      s hi,welcome s to python class
      welcome s to python cla
       hi,welcome s to python

**************************************************************************************************************************************

# 10. Replacing characters in strings with replace()
s='hi,welcome to java class'
print(s.replace('java','python'))
-------------------------------------------------------
>>>>  hi,welcome to python class

**************************************************************************************************************************************

# 11. Splitting strings with split()
s='hi,welcome to, python class'
print(s.split(','))
---------------------------------------
>>>>  ['hi', 'welcome to', ' python class']

**************************************************************************************************************************************

# 12. Converting integer objects to Strings 
a=10
print(a,type(a))
s=str(a)
print(s,type(s))
-----------------------------------------------
>>>>  10 <class 'int'>
      10 <class 'str'>

**************************************************************************************************************************************

# 13. Converting to uppercase and lowercase 
s='hi,welcome to'
s1='PYTHON CLASS'
print(s.upper(),s1.lower())
-----------------------------------------------
>>>>  HI,WELCOME TO python class

**************************************************************************************************************************************
