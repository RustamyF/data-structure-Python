"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        stack=[]
        result=[]
        stack.append(root)
        while stack:
            new=[]
            for i in range(len(stack)):
                node=stack.pop(0)
                new.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            result.append(new)
        return result


# Construct the tree for example 1
root = TreeNode(4)
a = TreeNode(9);
b = TreeNode(20)
c = TreeNode(15);
d = TreeNode(7)
root.left = a;
root.right = b
b.left = c;
b.right = d

my_result = Solution()
print(my_result.levelOrder(root))