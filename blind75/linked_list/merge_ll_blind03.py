"""Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        cur=ListNode(0)
        answer=cur
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        while l1:
            cur.next=l1
            l1=l1.next
            cur=cur.next
        while l2:
            cur.next=l2
            l2=l2.next
            cur=cur.next
        return answer.next

head = [1,2,4]
a=ListNode(head[0])
b=ListNode(head[1])
c=ListNode(head[2])
headA=a
a.next=b; b.next=c;

head = [1,3,4]
a=ListNode(head[0])
b=ListNode(head[1])
c=ListNode(head[2])
headB=a
a.next=b; b.next=c;
my_resul=Solution()
RESULT=my_resul.mergeTwoLists(headA, headB)
while RESULT:
    print(RESULT.val)
    RESULT=RESULT.next