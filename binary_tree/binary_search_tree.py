class ListNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # create the new node
        new_node = ListNode(data)
        # check if root is empty
        if self.root is None:
            # if root is empty, make the root equal to new node
            self.root = new_node
            return
        # create a temp node equal to the root
        temp = self.root
        # Loop over the nodes. If data is smaller than the node, go left, otherwise go right.
        while temp:
            # If data is equal to the node return False
            if temp.data == data:
                return False
            # If data is smaller than the node, check if it is None.
            # If None, make it equal to new node, else go left.
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            # If data is bigger than the node, check if it is None.
            # If None, make it equal to new node, else go right.
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def contain(self, data):
        # create a temp node equal to the root
        temp = self.root
        # loop over the nodes
        while temp:
            # if data is equal to the node, return true
            if temp.data == data:
                return True
            # if data is smaller than the node, go left. Otherwise go right.
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        # return False if no node is equal to the data
        return False

    @staticmethod
    def min_value_node(cur_node):
        # minimum node is the node the bottom left of the tree.
        # So go left until it is None.
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node

    # Tree traversal
    def BFS(self):
        # initiate a list for result and one for the queue
        results = []
        queue = []
        # check if root is empty
        if self.root is None:
            return results
        # append the root to the queue
        queue.append(self.root)
        # loop until there is a node in the queue
        while queue:
            # remove the first element
            new_node = queue.pop(0)
            # add its value to the results
            results.append(new_node.data)
            # if left node is not none, add that to the queue
            if new_node.left is not None:
                queue.append(new_node.left)
            # if the right node is not None, add that to the queue as well
            if new_node.right is not None:
                queue.append(new_node.right)
        # return the results list
        return results

    def DFS_preorder(self):
        results = []
        if self.root is None:
            return None
        def preorder(root):
            results.append(root.data)
            if root.left is not None:
                preorder(root.left)
            if root.right is not None:
                preorder(root.right)
        preorder(self.root)
        return results

    def DFS_postorder(self):
        results = []
        if self.root is None:
            return None
        def postorder(root):
            if root.left is not None:
                postorder(root.left)
            if root.right is not None:
                postorder(root.right)
            results.append(root.data)
        postorder(self.root)
        return results

    def DFS_inorder(self):
        if self.root is None:
            return None
        results=[]
        def inorder(root):
            if root.left is not None:
                inorder(root.left)
            results.append(root.data)
            if root.right is not None:
                inorder(root.right)
        inorder(self.root)
        return results


""" Example tree
          3
        1   4
      0   2
"""

my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(0)
my_tree.insert(4)
my_tree.insert(2)

print('value at the root is:', my_tree.root.data)
print('value at the left of root is:', my_tree.root.left.data)
print('value at the right of root is:',my_tree.root.right.data)

print('value at the left of left of root is:',my_tree.root.left.left.data)

print('contain value 5:', my_tree.contain(5))
print('min value in tree', my_tree.min_value_node(my_tree.root).data)

print('Depth first search:', my_tree.BFS())
print('DFS inorder:', my_tree.DFS_inorder())
print('DFS preorder:', my_tree.DFS_preorder())
print('DFS postorder:', my_tree.DFS_postorder())








