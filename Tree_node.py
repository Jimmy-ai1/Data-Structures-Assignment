# Binary tree is an example of using tree data structure

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Added another class to handle the structure and behavior while the previous class handles the data
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTree(data)
        else:
            self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
            else:
                self._insert_recursive(node.right, data)


