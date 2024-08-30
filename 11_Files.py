# 1. Write a program to read text file 

file=open('H.txt','r')
d=file.read()
print(d)
file.close()
-----------------------------------------
>>>>  Hello,
      My name is Hasnain Ansari, hailing from Pratapgarh.
      I have completed Diploma in CSE.


***************************************************************************************************************************************
# 2. Write a program to write text to .txt file using  InputStream 

file1=open('Ha.txt','w')
d1='My name is Python'
file1.write(d1)
file1.close()
---------------------------------------------------------------------
>>>>  17

***************************************************************************************************************************************

# 3. Write a program to read a file stream 
  
file3=open('H.txt','r+')
d3=file3.readline(4)
print(d3)
file3.close()
---------------------------------------------
>>>>  Hell


***************************************************************************************************************************************
# 4. Write a program to read a file stream supports random access  

file4=open('H.txt','r')
d4=file4.readlines()
print(d4[1])
file4.close()
-------------------------------------------------------------------
>>>>  My name is Hasnain Ansari, hailing from Pratapgarh.

**************************************************************************************************************************************

# 5. Write a program to read a file a just to a particular index using seek()  

file5=open('H.txt','r')
file5.seek(9)
d5=file5.read()
print(d5)
file5.close()
--------------------------------------------------------------------------------
>>>>  y name is Hasnain Ansari, hailing from Pratapgarh.
      I have completed Diploma in CSE.

*************************************************************************************************************************************

# 6.  Write a program to check whether a file is having read access and write access permissions 

import os
f=open('H.txt','r')
print(os.access('H.txt',os.R_OK))
print(os.access('H.txt',os.W_OK))
f.close()
--------------------------------------------------------------------------------------------------
>>>>  True
      True

*************************************************************************************************************************************
