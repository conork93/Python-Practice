#Conor Kennedy
#8/7/2017

"""
FizzBuzz
Print 1 - 100 
For multiples of three, print "Fizz" 
instead of the number and "Buzz" if the number is a multiple
of five. For multiples of both three and five, the 
program will print "FizzBuzz"
"""

for i in range(1, 101):
  if i % 3 == 0:
    if i % 5 == 0:
      print "fizzbuzz"
    else:
      print "fizz"
  if i % 5 == 0:
    print "buzz"
  else:
    print i
