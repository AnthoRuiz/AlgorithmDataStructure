class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        # we have to visit the right subtree
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1

        self.handle_violation(node)

    def handle_violation(self, node):

        while node is not None:
            node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
            self.violation_helper(node)
            node = node.parent

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:

            if node.left is None and node.right is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = None
                if parent is not None and parent.right == node:
                    parent.right = None

                if parent is None:
                    self.root = None

                del node

                self.handle_violation(parent)

            elif node.left is None and node.right is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.rightChild == node:
                        parent.right = node.right
                else:
                    self.root = node.right

                node.right.parent = parent
                del node

                self.handle_violation(parent)

            elif node.right is None and node.left is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node

                self.handle_violation(parent)

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)

        return node

    def violation_helper(self, node):

        balance = self.calculate_balance(node)

        # OK, we know the tree is left heavy BUT it can be left-right heavy or left-left heavy
        if balance > 1:

            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)

            # this is the right rotation on grandparent ( if left-left heavy, that's single right rotation is needed
            self.rotate_right(node)

        # OK, we know the tree is right heavy BUT it can be left-right heavy or right-right heavy
        if balance < -1:

            # right - left heavy, so we need a right rotation  before left rotation
            if self.calculate_balance(node.right) > 0:
                self.rotate_right(node.right)

            # left rotation
            self.rotate_left(node)

    def calculate_height(self, node):

        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):

        if node is None:
            return 0

        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)

        l = ''
        r = ''
        p = ''

        if node.left is not None:
            l = node.left.data
        else:
            l = 'NULL'

        if node.right is not None:
            r = node.right.data
        else:
            r = 'NULL'

        if node.parent is not None:
            p = node.parent.data
        else:
            p = 'NULL'

        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height))

        if node.right:
            self.traverse_in_order(node.right)

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left = node.left
        t = temp_left.right

        temp_left.right = node
        node.left = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left
        temp_left.parent = temp_parent

        if temp_left.parent is not None and temp_left.parent.left == node:
            temp_left.parent.left = temp_left

        if temp_left.parent is not None and temp_left.parent.right == node:
            temp_left.parent.right = temp_left

        if node == self.root:
            self.root = temp_left

        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        temp_left.height = max(self.calculate_height(temp_left.left),
                               self.calculate_height(temp_left.right)) + 1

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right = node.right
        t = temp_right.left

        temp_right.left = node
        node.right = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right
        temp_right.parent = temp_parent

        if temp_right.parent is not None and temp_right.parent.left == node:
            temp_right.parent.left = temp_right

        if temp_right.parent is not None and temp_right.parent.right == node:
            temp_right.parent.right = temp_right

        if node == self.root:
            self.root = temp_right

        node.height = max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
        temp_right.height = max(self.calculate_height(temp_right.left),
                                self.calculate_height(temp_right.right)) + 1


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(6)
    avl.insert(1)

    avl.remove(6)
    avl.traverse()
