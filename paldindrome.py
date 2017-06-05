
# simple program to check if a word is a palindrome
# a paldindrome is a word that is the same backwards as forward

x = raw_input('Enter a word to check if its a palindrome:')
reverse = x[::-1]

if (x==reverse):
  print ('is a palindrome')
else:
  print ('is not a paldindrome')
