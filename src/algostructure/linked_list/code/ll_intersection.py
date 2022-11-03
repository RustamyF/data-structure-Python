# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB) -> ListNode:
        q=set()
        listA, listB=headA, headB
        while listA:
            q.add(listA)
            listA=listA.next
        while listB:
            if listB in q: return listB.val
            listB=listB.next

        return None



## Test 1
# list A
a, b, c, d, e=ListNode(4), ListNode(1), ListNode(8), ListNode(4), ListNode(5)
headA=a
# list B
A, B, C, D, E, F=ListNode(5), ListNode(6), ListNode(1), ListNode(8), ListNode(4), ListNode(5)
headB=A
# Connect them
a.next=b;  b.next=c; c.next=d; d.next=e
A.next=B;  B.next=C; C.next=c

result=Solution()
print(result.getIntersectionNode(headA, headB))

## Test 2
# list A
a, b, c, d, e=ListNode(1), ListNode(9), ListNode(1), ListNode(2), ListNode(4)
headA=a
# list B
A, B, C=ListNode(3), ListNode(2), ListNode(4)
headB=A
# Connect them
a.next=b;  b.next=c; c.next=d; d.next=e
A.next=d

result=Solution()
print(result.getIntersectionNode(headA, headB))

## Test 3
# list A
a, b, c=ListNode(2), ListNode(6), ListNode(4)
headA=a
# list B
A, B=ListNode(1), ListNode(5)
headB=A
# Connect them
a.next=b;  b.next=c
A.next=B

result=Solution()
print(result.getIntersectionNode(headA, headB))