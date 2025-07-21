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

