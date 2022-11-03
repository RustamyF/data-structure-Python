"""Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head is None or head.next is None:
            return None

        left, right = head, head
        for _ in range(n):
            right = right.next

        before = head
        while right:
            before = left
            left = left.next
            right = right.next
        if left == head:
            head = head.next

        before.next = before.next.next

        return head

head = [1,2,3,4,5]
a=ListNode(head[0])
b=ListNode(head[1])
c=ListNode(head[2])
d=ListNode(head[3])
e=ListNode(head[4])
head=a
a.next=b; b.next=c;
c.next=d; d.next=e
my_resul=Solution()
RESULT=my_resul.removeNthFromEnd(head, 2)
print(RESULT)
while RESULT:
    print(RESULT.val)
    RESULT=RESULT.next