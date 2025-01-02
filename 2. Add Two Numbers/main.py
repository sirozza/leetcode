# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

def addTwoNumbers(l1, l2):
    if l1 == [0] and l2 == [0]:
        return l1
    l1.reverse(), l2.reverse()
    l1 = int(''.join(map(str, l1)))
    l2 = int(''.join(map(str, l2)))
    l3 = l1 + l2
    l3 = [int(d) for d in str(l3)]
    l3.reverse()
    return l3

l1 = [0]
l2 = [0]

print(addTwoNumbers(l1, l2))