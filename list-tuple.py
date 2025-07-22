'''
Given a list of numbers, determine and print the number of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered because they don't have two neighbors.
'''
def count_nums(num_list):
  count = 0
  for i in range(1, len(num_list) - 1):
    if num_list[i-1] < num_list[i] and num_list[i + 1] < num_list[i]:
      count += 1
  return count

def count_nums_list_comp(num_list):
  return (len([i for i in range(1, len(num_list) - 1) if num_list[i] > num_list[i - 1] and num_list[i] > num_list[i + 1]]))

#print(count_nums([5, 2, 5, 1, 5,]))

'''
Remove the duplicates from a list.

Matching:
This problem is similar to many search algorithms I have written in the past. The best solution always uses on for loop and harness's the efficiency
of a dictionary, hashmap, or set. Unfortunately we are not allowed to use these to solve so the best solution will be to use two lists.

Plan:
Declare a result list
for integer in list:
   if integer not in result:
      append integer to result
return result

Evaluate:
The worst case scenario for this problem is O(n)^2 because we will be iterating two lists every time we try to add an element to our result.
'''

def remove_duplicates(a_list):
  distinct_elements = []
  for integer in a_list:
    if integer not in distinct_elements:
      distinct_elements.append(integer)
  return distinct_elements

# print(remove_duplicates([1,1,1,1,1,5,3,6,7,7,8,9,6,21,5,8]))

'''
Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, find the maximal element and print
its row number and column number. If there are many maximal elements in different rows, report the one with smaller row number. If there are many
maximal elements in the same row, report the one with smaller column number.
'''

def find_max(nums):
  max = int(nums[0][0])
  max_row = 0
  max_column = 0
  for i in range(len(nums)):
    for j in range(len(nums[i])):
      if int(nums[i][j]) > max:
        max = int(nums[i][j])
        max_row = i
        max_column = j
  return [max_row, max_column]

# size = input()
# size_list = size.split()
# outer = []
# for i in range(int(size_list[0])):
#    current = input().split()
#    outer.append(current)

# max = find_max(outer)
# print(max[0], max[1])
'''
It is possible to place 8 queens on an 8×8 chessboard so that no two queens threaten each other. Thus, it requires that no two queens share the same row, column, or diagonal.

Given a placement of 8 queens on the chessboard. If there is a pair of queens that violates this rule, print YES, otherwise print NO. The input consists of eight
coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chessboard with rows and columns numbered from 1 to 8.
'''
def check_queens_chessboard(x, y):
  for i in range(len(x)):
    for j in range(i + 1, 8):
      if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i]-y[j]):
        return 'YES'
  return 'NO'

# x = []
# y = []
# for inputs in range(8):
#     a_list = [int(s) for s in input().split()] # Use list comprehension to get input data
#     x.append(a_list[0])
#     y.append(a_list[1])

# print(check_queens_chessboard(x, y))

# print(check_queens_chessboard(x, y))
'''
DO MORE RESEARCH ON XOR ... This algorithm finds the number with an odd count
'''


def odd_occurences_of_number(nums):
  result = 0

  for num in nums:
    print(result)
    result ^= num
  return result

# print(odd_occurences_of_number( [-2, 4, 1, 4, -2, 4, 1]))

