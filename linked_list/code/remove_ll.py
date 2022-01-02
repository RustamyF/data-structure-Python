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
    def removeNthFromEnd2(self, head, n: int):
        if head is None or head.next is None:
            return None
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        index=length-n
        before=head
        if index==0:
            head=head.next
        for _ in range(index-1):
            before=before.next
        before.next=before.next.next
        return head


## Test 1
a, b, c, d, e=ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
head=a
# Connect them
a.next=b;  b.next=c; c.next=d; d.next=e
result=Solution()
print(result.removeNthFromEnd(head,2))

## Test 2
a=ListNode(1)
head=a
# Connect them
result=Solution()
print(result.removeNthFromEnd(head,1))

## Test 3
a, b=ListNode(1), ListNode(2)
head=a
# Connect them
a.next=b
result=Solution()
print(result.removeNthFromEnd(head,1))