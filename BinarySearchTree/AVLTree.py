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

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

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

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left)
        elif data > node.data:
            self.remove_node(data, node.right)
        else:
            # we have the node we want to remove
            # case1: if the node is a leaf
            if node.left is None and node.right is None:
                print(f'Removing a leaf node: {node.data}')
                parent = node.parent

                if parent and parent.left == node:
                    parent.left = None
                elif parent and parent.right == node:
                    parent.right = None
                elif parent is None:
                    self.root = None

                del node
                # After a new delete we have to check AVL properties are violated.
                self.handle_violation(parent)

            # case2: if the node has a single child
            elif node.left is None and node.right:
                print("removing a node with a single right child")
                parent = node.parent

                if parent:
                    if parent.left == node:
                        parent.left = node.right
                    elif parent.righ == node:
                        parent.right = node.right
                else:
                    self.root = node.right

                node.right.parent = parent
                del node
                # After a new delete we have to check AVL properties are violated.
                self.handle_violation(parent)

            elif node.right is None and node.left:
                print("removing a node with a single left child")
                parent = node.parent

                if parent:
                    if parent.left == node:
                        parent.left = node.left
                    elif parent.righ == node:
                        parent.right = node.left
                else:
                    self.root = node.left

                node.left.parent = parent
                del node
                # After a new delete we have to check AVL properties are violated.
                self.handle_violation(parent)

            # case3: if the node has 2 children
            else:
                print("Removing node with two children")
                predecessor = self.get_predecessor(node.left)
                tmp = predecessor.data
                predecessor.data = node.data
                node.data = tmp
                self.remove_node(data, predecessor)


