# This problem was recently asked by Microsoft:

# Given a string, find the length of the longest substring without repeating characters.

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    left_pos = 0
    right_pos = 0
    char_dict = {s[0]: 0}
    found_repeat = False
    while right_pos < len(s) - 1 and not found_repeat:
    	right_pos += 1
    	if char_dict.get(s[right_pos]) == None:
    		char_dict[s[right_pos]] = right_pos
    	else:
    		found_repeat = True

    substr_len = right_pos - left_pos
    if found_repeat:
    	# run function on substring without first instance of repeating character
    	new_pos = char_dict[s[right_pos]] + 1
    	new_s = s[new_pos:]
    	return max(substr_len,
    			   self.lengthOfLongestSubstring(new_s))

    return substr_len

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
