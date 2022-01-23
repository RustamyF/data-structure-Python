"""Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, t, r):
        if not t and not r:
            return True
        if t and r and t.val == r.val:
            return self.sameTree(t.left, r.left) and self.sameTree(t.right, r.right)

        return False


    def print_tree(self, root):
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop(0)
            print(node.val)

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)



# Construct the tree for example 1
root = TreeNode(3)
a = TreeNode(4);
b = TreeNode(5)
c = TreeNode(1);
d = TreeNode(2)
root.left = a;
root.right = b
a.left = c;
a.right = d

subRoot = TreeNode(4)
a = TreeNode(1);
b = TreeNode(2)
subRoot.left=a
subRoot.right=b

my_result=Solution()
print(my_result.isSubtree(root, subRoot))