# This problem was recently asked by AirBNB:

# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences
#   of a target element, x. Return -1 if the target is not found.

class Solution:
  def getRange(self, arr, target):
    # Fill this in.
    occurrence_pos = []
    for i in range(len(arr)):
      print(i)
      if not occurrence_pos and arr[i] == target:
        occurrence_pos.append(i)
      elif arr[i] == target and (i == len(arr) - 1 or arr[i+1] != target):
        occurrence_pos.append(i)
        break
      # works since arr is sorted
      elif occurrence_pos and arr[i] != target:
        break

    if not occurrence_pos:
      return -1
    elif len(occurrence_pos) == 1:
      occurrence_pos *= 2

    return occurrence_pos


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
