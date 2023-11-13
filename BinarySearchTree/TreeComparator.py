from BinarySearchTree import BinarySearchTree


class TreeComparator:
    def compare(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.data != root2.data:
            return False

        return self.compare(root1.left_node, root2.left_node) and self.compare(root1.right_node, root2.right_node)


if __name__ == '__main__':
    bst1 = BinarySearchTree()
    bst1.insert(20)
    bst1.insert(3)
    bst1.insert(-8)
    bst1.insert(5)

    bst2 = BinarySearchTree()
    bst2.insert(20)
    bst2.insert(3)
    bst2.insert(-8)
    bst2.insert(5)

    t_comparator = TreeComparator()
    print(t_comparator.compare(bst1.root, bst2.root))

    print()
