#Binary tree is an example of using tree data structure

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# I have added another class to handle the structure and behavior while the previous class handles the data
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BinaryTree(data)
        else:
            self._insert_recursive(self.root, data)


