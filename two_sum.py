# This problem was recently asked by Facebook:

# You are given a list of numbers, and a target number k. Return whether or not there are
#   two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
#   return true since 4 + 1 = 5.

# Challenge: Try to do it in a single pass of the list.

def two_sum(list, k):
  # Fill this in.
  list.sort()
  a = 0
  b = len(list) - 1
  while a < b:
    if list[a] + list[b] < k:
      a += 1
    elif list[a] + list[b] > k:
      b -= 1
    else:
      return True
  return False

def two_sum_hash(list, k):
  dict = {}
  for num in list:
    if dict.get(k - num) is not None:
      return True
    else:
      dict[num] = num
  return False

# true
print(two_sum_hash([4,7,1,-3,2], 5))
print(two_sum_hash([4,7,3,-3,2], 5))
print(two_sum_hash([4,7,9,-2,0], 5))

# false
print(two_sum_hash([1,1,1,1], 4))
