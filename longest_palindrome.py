# This problem was recently asked by Twitter:

# A palindrome is a sequence of characters that reads the same backwards and forwards.
#  Given a string, s, find the longest palindromic substring in s.

class Solution:
  def _insertStrInMiddle(self, s, to_be_inserted):
    middle = len(s) // 2 # length of palidrome is always even at this point
    return s[:middle] + to_be_inserted + s[middle:]

  def longestPalindrome(self, s):
    if len(s) <= 1:
      return s

    # Fill this in.
    left_pos = 0
    right_pos = len(s) - 1
    # mismatch = False
    palindrome = ''

    while right_pos >= left_pos:
      if left_pos == right_pos:
        palindrome = self._insertStrInMiddle(palindrome, s[left_pos])
      elif s[left_pos] == s[right_pos]:
        palindrome = self._insertStrInMiddle(palindrome, s[left_pos] + s[right_pos])
        left_pos += 1

      # traverse right pointer back until it matches left pointer
      right_pos -= 1

    other_palindrome = self.longestPalindrome(s[len(palindrome):])
    if len(other_palindrome) > len(palindrome):
      return other_palindrome

    return palindrome

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
