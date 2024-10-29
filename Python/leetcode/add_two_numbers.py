"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_l1 = int("".join([str(n) for n in l1.val]))
        sum_l2 = int("".join([str(n) for n in l2.val]))
        return [int(n) for n in str(sum_l1 + sum_l2)][::-1]


sol = Solution()

l1 = ListNode([2, 4, 3])
l2 = ListNode([5, 6, 4])
assert sol.addTwoNumbers(l1, l2) == [7, 0, 8]

l1 = ListNode([0])
l2 = ListNode([0])
assert sol.addTwoNumbers(l1, l2) == [0]

l1 = ListNode([9, 9, 9, 9, 9, 9, 9])
l2 = ListNode([9, 9, 9, 9])
assert sol.addTwoNumbers(l1, l2) == [8, 9, 9, 9, 0, 0, 0, 1]
