class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0

    def __len__(self):
        """Returns the number of value-containing nodes in this list."""
        return self.num_of_nodes

    def traverse_forward(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            actual_node = self.head
            count = 1

            while actual_node is not None:
                print(f"Node {count}: {actual_node}")
                count += 1
                actual_node = actual_node.next_node

    def traverse_backward(self):
        if self.head is None:
            print('Linked list is empty.')
        else:
            actual_node = self.tail
            count = 1

            while actual_node is not None:
                print(f"Node {count}: {actual_node}")
                count += 1
                actual_node = actual_node.prev_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = new_node

        self.num_of_nodes += 1

    def insert_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

        self.num_of_nodes += 1


if __name__ == '__main__':
    doubly_linked = DoublyLinkedList()
    doubly_linked.insert_start(1)
    doubly_linked.insert_start(2)
    doubly_linked.insert_start(3)
    doubly_linked.insert_start(4)
    doubly_linked.traverse_forward()
    doubly_linked.traverse_backward()
