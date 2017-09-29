#Conor Kennedy 
#9/29/2017

'''
on every year that is evenly divisible by 4
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400
'''

def leap(year):
  return(year % 4 == 0 and year % 100 !=0) or year % 400 == 0
      

print(leap(2020)) #leap year
print(leap(2021))
print(leap(2024)) #leap year
