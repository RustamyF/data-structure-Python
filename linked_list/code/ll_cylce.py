# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        q=set()
        temp=head
        while temp is not None:
            if temp in q:
                return True, temp.val
            q.add(temp)
            temp=temp.next
        return False
    def hasCycle2(self, head) -> bool:
        slow=head
        fast=head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True, slow.val
        return False
# test 1#
# Construct the list
a, b, c, d=ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
a.next=b;  b.next=c; c.next=d; d.next=b; head=a

result=Solution()
print(result.hasCycle(head))

# test 2#
# Construct the list
a, b=ListNode(1), ListNode(2)
a.next=b;  b.next=a; head=a
result=Solution()
print(result.hasCycle(head))

# test 3#
# Construct the list
a=ListNode(1)
head=a
result=Solution()
print(result.hasCycle(head))
