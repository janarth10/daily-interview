# This problem was recently asked by Google:

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: try sorting the list using constant space

# Solution using O(n) space complexity
def sortNums(nums):
  # Fill this in.
  sorted_arr = []
  pos_of_last_one = -1
  for i in nums:
    if i == 1:
      pos_of_last_one += 1
      sorted_arr.insert(pos_of_last_one, 1)
    elif i == 2:
      sorted_arr.insert(pos_of_last_one+1, 2)
    else:
      sorted_arr.append(3)
  return sorted_arr

# Solution using O(n) space complexity
def sortNumsByCounting(nums):
  count_1 = 0
  count_2 = 0
  count_3 = 0
  for i in nums:
    if i == 1:
      count_1 += 1
    elif i == 2:
      count_2 += 1
    else:
      count_3 += 1

  sorted_arr = [1] * count_1 + [2] * count_2 + [3] * count_3
  return sorted_arr

# Solution using O(1) space complexity
def sortNumsConstantSpace(nums):
  i = 0
  count_3 = nums.count(3)
  print('count_3 = ' + str(count_3))
  while i < len(nums):
    if nums[i] == 1:
      nums.pop(i)
      nums.insert(0, 1)
      i += 1
    elif nums[i] == 3 and i < (len(nums) - count_3):
      nums.pop(i)
      nums.append(3)
    else:
      i += 1
  return nums



a = [3, 3, 2, 1, 3, 2, 1]
print(sortNumsConstantSpace(a))
print(a)
# [1, 1, 2, 2, 3, 3, 3]
