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

    def traverse_pre_order(self, node):
        print(node.data)

        if node.left_node:
            self.traverse_pre_order(node.left_node)

        if node.right_node:
            self.traverse_pre_order(node.right_node)

    def traverse_post_order(self, node):
        if node.left_node:
            self.traverse_post_order(node.left_node)

        if node.right_node:
            self.traverse_post_order(node.right_node)

        print(node.data)

    def insert(self, data):
        # first Node in the BST
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def in_order(self):
        if self.root:
            self.traverse_in_order(self.root)

    def pre_order(self):
        if self.root:
            self.traverse_pre_order(self.root)

    def post_order(self):
        if self.root:
            self.traverse_post_order(self.root)


# Inorder => Left, Root, Right.
#
# Preorder => Root, Left, Right.
#
# Post order => Left, Right, Root.


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(8)
    bst.insert(12)
    bst.insert(-5)
    bst.insert(44)

    bst.remove(8)
    bst.remove(10)
    bst.remove(12)

    bst.remove(44)
    bst.remove(5)
    bst.remove(-5)

    bst.in_order()
