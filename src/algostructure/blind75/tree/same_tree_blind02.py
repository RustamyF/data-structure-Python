""" Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeStack(self, p, q):
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left,q.left))
                stack.append((p.right,q.right))
            elif p or q:
                return False
        return True


q=TreeNode(1)
a=TreeNode(2)
b=TreeNode(3)
q.left=a
q.right=b

p=TreeNode(1)
a=TreeNode(2)
b=TreeNode(3)
p.left=a
p.right=b


my_result=Solution()
print(my_result.isSameTree(p,q))
print(my_result.isSameTreeStack(p,q))

