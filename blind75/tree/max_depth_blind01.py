"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    def maxDepthIt(self, root):
        stack=[]
        if root is not None:
            stack.append((1,root))
        depth=0
        while stack!=[]:
            curDepth,root=stack.pop()
            if root is not None:
                depth=max(depth,curDepth)
                stack.append((curDepth+1, root.left))
                stack.append((curDepth+1, root.right))
        return depth




root=TreeNode(3)
a=TreeNode(9)
b=TreeNode(20)
c=TreeNode(15)
d=TreeNode(7)
root.left=a
root.right=b
b.left=c
b.right=d

my_result=Solution()
print(my_result.maxDepth(root))
print(my_result.maxDepthIt(root))



