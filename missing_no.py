'''
Given an array nums containing n unsorted distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints: Build a solution with O(n) time complexity and uses constant space (O(1) Space Complexity).

Note: The maximum value in the input will be n = len(input_list).
'''
def first_missing_positive_integer(nums):
  total = (len(nums)*(len(nums) + 1))//2
  sum = 0
  for num in nums:
    sum += num
  return total - sum



print(first_missing_positive_integer([0, 1, 2]))
