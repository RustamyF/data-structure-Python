

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self,):
        self.result=[]
    def preorder(self,root):
        if root is None:
            return None
        self.result.append(root.val)
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)
    def preorder_iter(self,root):
        if root is None:
            return None
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            self.result.append(node.val)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

    def inorder(self,root):
        if root is None:
            return None
        if root.left is not None:
            self.inorder(root.left)
        self.result.append(root.val)
        if root.right is not None:
            self.inorder(root.right)
    def inorder_ite(self,root):
        if root is None:
            return None
        stack=[]
        stack.append(root)
        curr=root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            self.result.append(curr.val)
            if curr.right:
                curr=curr.right



    def postorder(self, root):
        if root is None:
            return None
        if root.left is not None:
            self.inorder(root.left)
        if root.right is not None:
            self.inorder(root.right)
        self.result.append(root.val)
    def levelorder(self,root):
        stack=[]
        stack.append(root)
        while stack:
            new=[]
            for i in range(len(stack)):
                node = stack.pop(0)
                new.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            self.result.append(new)


""" 
       3
     /   \
   1       4
 /  \
5     2
"""
root = TreeNode(3)
a = TreeNode(1); b = TreeNode(4)
c = TreeNode(2); d = TreeNode(5)
root.left = a; root.right = b
a.right=c; a.left=d

# pre_order
my_result=Solution()
my_result.preorder(root)
print('pre order list:',my_result.result)

# in order
my_result=Solution()
my_result.inorder(root)
print('in order list:',my_result.result)

# post order
my_result=Solution()
my_result.postorder(root)
print('post order list:',my_result.result)

# level order
my_result=Solution()
my_result.levelorder(root)
print('level order list:',my_result.result)