"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
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
    def invertTree(self, root):
        if root is None:
            return None

        temp=root.left
        root.left=root.right
        root.right=temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    def invertTree_iterative(self, root):
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if node is None:
                continue
            node.left, node.right= node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        return root

    def print_tree(self,root):
        if root is None:
            return None
        print(root.val)
        self.print_tree(root.left)
        self.print_tree(root.right)




# Construct the tree for example 1
root=TreeNode(4)
a=TreeNode(2); b=TreeNode(7)
c=TreeNode(1); d=TreeNode(3)
e=TreeNode(6); f=TreeNode(9)
root.left=a; root.right=b
a.left=c; a.right=d
b.left=e; b.right=f

my_result=Solution()

print('tree before inversion:')
my_result.print_tree(root)
# my_result.invertTree(root)
my_result.invertTree_iterative(root)

print('tree after inversion:')
my_result.print_tree(root)