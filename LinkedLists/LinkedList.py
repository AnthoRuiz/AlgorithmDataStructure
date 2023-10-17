class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        # this is the first Node of the linked list.
        self.head = None
        self.num_of_nodes = 0

    def __len__(self):
        """Returns the number of value-containing nodes in this list."""
        return self.num_of_nodes

    # O(1)
    def size_of_list(self):
        return self.num_of_nodes

    # O(1)
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    # O(N)
    def traverse(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            actual_node = self.head
            count = 1

            while actual_node is not None:
                print(f"Node {count}: {actual_node}")
                count += 1
                actual_node = actual_node.next_node

    def remove_first(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            self.num_of_nodes -= 1
            self.head = self.head.next_node

    def remove_end(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            actual_node = self.head
            prev_node = None
            self.num_of_nodes -= 1

            while actual_node.next_node is not None:
                prev_node = actual_node
                actual_node = actual_node.next_node

            prev_node.next_node = actual_node.next_node

    def remove(self, data):

        # the list is empty
        if self.head is None:
            print('Linked list is empty.')

        actual_node = self.head
        previous_node = None
        self.num_of_nodes -= 1

        # search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # search miss
        if actual_node is None:
            print("Element not Found")
        else:
            # the head node is the one we want to remove
            if previous_node is None:
                self.head = actual_node.next_node
            else:
                # remove an internal node by updating the pointers
                previous_node.next_node = actual_node.next_node

    def insert_at(self, data, idx):

        if idx < 1:
            print('out of bounding')

        else:
            self.num_of_nodes += 1
            new_node = Node(data)

            if idx == 1:
                new_node.next_node = self.head
                self.head = new_node
            else:
                i = 1
                actual_node = self.head
                previous_node = None
                while actual_node is not None and i < idx:
                    previous_node = actual_node
                    actual_node = actual_node.next_node
                    i += 1

                if actual_node is not None:
                    previous_node.next_node = new_node
                    new_node.next_node = actual_node
                else:
                    previous_node.next_node = new_node

    def reverse(self):
        actual_node = self.head
        next_node = actual_node.next_node
        previous_node = None

        while next_node is not None:
            actual_node.next_node = previous_node
            previous_node = actual_node
            actual_node = next_node
            next_node = next_node.next_node

        actual_node.next_node = previous_node
        self.head = actual_node

    def get_middle_node(self):
        mid = self.num_of_nodes / 2
        i = 1
        actual_node = self.head
        while i < mid:
            actual_node = actual_node.next_node
            i += 1
        return actual_node


if __name__ == '__main__':
    linked = LinkedList()
    linked.insert_end(1)
    linked.insert_end(2)
    linked.insert_end(3)
    linked.insert_end(4)
    linked.traverse()
    print(linked.get_middle_node())
