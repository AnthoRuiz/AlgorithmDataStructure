class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    class LinkedList:
        def __init__(self):
            # this is the first Node of the linked list.
            self.head = None
            self.num_of_nodes = 0

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

            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node
