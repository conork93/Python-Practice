#Conor Kennedy
#6/5/17

#using nest loops to create a triangle
'''
*
**
***
****
*****
'''

pyramid = ''
width = 1
for x in range(5):
  for y in range(width):
       pyramid += '*'
  pyramid += '\n'
  width +=1
print pyramid
