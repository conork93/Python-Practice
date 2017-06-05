#Conor Kennedy
#6/5/17

#basic control flow in rock paper scissors game

from random import randint

x = ['rock', 'paper', 'scissors']
computer = x[randint(0,2)]
player = raw_input('Enter rock, paper, or scissors: ')

if(player == computer):
  print('Draw')
elif (player == 'rock'):
  if(computer == 'scissors'):
    print ('You win \ncomputer choose scissors')
  else:
    print ('You lose \ncomputer choose scissors')
elif (player == 'paper'):
  if(computer == 'rock'):
    print ('You win \ncomputer choose rock')
  else:
    print ('You lose \ncomputer choose rock')
elif (player == 'scissors'):
  if(computer == 'paper'):
    print ('You win \ncomputer choose paper')
  else:
    print ('You lose \ncomputer choose paper')
