"""
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        before=None
        while head:
            After=head.next
            head.next=before
            before=head
            head=After
        return before


head = [1, 2, 3, 4, 5]
a=ListNode(head[0])
b=ListNode(head[1])
c=ListNode(head[2])
d=ListNode(head[3])
e=ListNode(head[4])
head=a
a.next=b; b.next=c; c.next=d; d.next=e
my_resul=Solution()
print(my_resul.reverseList(head).val)