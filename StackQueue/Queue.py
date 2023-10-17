# FIFO: First In First Out

class Queue:
    def __init__(self):
        self.queue = []

    # O(1)
    def is_empty(self):
        return self.queue == []

    # O(1)
    def queue_size(self):
        return len(self.queue)

    # O(1)
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) because we need to remove the first item of the array, so we need to move all the items to the left.
    # We can solve this using doubly linked list
    def dequeue(self):
        if self.queue_size() < 1:
            return "Queue Empty"

        data = self.queue[0]
        del self.queue[0]
        return data

    # O(1)
    def peek(self):
        return self.queue[0]


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.peek())
    print(queue.queue_size())
    print(queue.dequeue())
    print(queue.peek())
