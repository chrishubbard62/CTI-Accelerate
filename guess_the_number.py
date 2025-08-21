'''
Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n.
Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret
number exists in the provided set, or NO, if his number does not exist in the provided set. Then after
a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number.

Given the positive integer n in the first line, followed by the a sequence Beatrice's guesses, series of
numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls
for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.
'''

max = int(input())
possible = {str(i) for i in range(1, max + 1)}

guess = {}
while guess!= 'HELP':
  guess = input()
  if guess == 'HELP':
    break
  response = input()

  if response == "YES":
    possible = possible & set(guess.split())
  else:
    possible =  possible - set(guess.split())

possible = sorted(list(possible))
for num in possible:
  print(num, end=' ')
# print(possible)
# possible = {'1', '2', '3', '4', '5'} & possible
# print(possible)
# possible = possible - {'2', '4', '6', '8', '10'}
# print(possible)
