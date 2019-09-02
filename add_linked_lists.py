# This problem was recently asked by Microsoft:

# You are given two linked-lists representing two non-negative integers. 
#	The digits are stored in reverse order and each of their nodes contain a single digit. 
#	Add the two numbers and return it as a linked list.

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    if l1 is None and l2 is None:
    	return None

    sum = c
    if l1:
    	sum += l1.val
    	l1 = l1.next
    if l2:
    	sum += l2.val
    	l2 = l2.next

    result = ListNode(sum % 10)
    result.next = self.addTwoNumbers(l1, l2, c = sum // 10)
    return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8