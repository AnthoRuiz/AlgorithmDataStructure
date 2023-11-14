class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # @staticmethod
    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1

        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1

        # After a new insert we have to check AVL properties are violated.
        self.handle_violation(node)



