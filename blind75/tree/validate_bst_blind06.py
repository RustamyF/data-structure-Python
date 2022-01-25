"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""
# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            if node is None:
                return True
            if node.val<low or node.val>high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)




# Construct the tree for example 1

root = TreeNode(2)
a = TreeNode(1);
b = TreeNode(5)
root.left = a;
root.right = b
my_result=Solution()
print(my_result.isValidBST(root))



root = TreeNode(5)
a = TreeNode(1);
b = TreeNode(4)
c = TreeNode(3);
d = TreeNode(6)
root.left = a;
root.right = b
b.left = c;
b.right = d

my_result=Solution()
print(my_result.isValidBST(root))



