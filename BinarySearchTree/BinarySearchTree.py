class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None

        # important to implement remove function
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        # we have only access to the Root Node, similar to a LinkedList.
        self.root = None

    def insert_node(self, data, node):
        # we are checking the left side
        if data < node.data:
            if node.left_node:
                # if we have a left node we keep going to find a place
                self.insert_node(data, node.left_node)
            else:
                # when left node if None (we create one)
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                # if we have a right node we keep going to find a place
                self.insert_node(data, node.right_node)
            else:
                # when right node if None (we create one)
                node.right_node = Node(data, node)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        return node.data

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        return node.data

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)

    def insert(self, data):
        # first Node in the BST
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def in_order(self):
        if self.root:
            self.traverse_in_order(self.root)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)

    print(bst.get_max(), bst.get_min())
    bst.in_order()
