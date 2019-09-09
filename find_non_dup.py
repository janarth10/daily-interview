# This problem was recently asked by Facebook:

# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Challenge: Find a way to do this using O(1) memory.

def singleNumber(nums):
  # Fill this in.
  if len(nums) == 1:
    return nums[0]

  nums.sort()
  for i in range(len(nums) - 1):
    if i == 0 and nums[i] != nums[i+1]:
      return nums[i]
    elif nums[i] != nums[i-1] and nums[i] != nums[i+1]:
      return nums[i]
  return None

print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
