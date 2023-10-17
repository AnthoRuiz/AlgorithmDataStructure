# LIFO: Last In First Out

class Stack:
    def __init__(self):
        self.stack = []

    # Insert item into the stack O(1)
    def push(self, data):
        self.stack.append(data)

    # Remove and Return the last item inserted O(1)
    def pop(self):
        if self.stack_size() < 1:
            return "Stack Empty"

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # return the last item inserted without removing it.
    def peek(self):
        return self.stack[-1]

    # O(1)
    def is_empty(self):
        return self.stack == []

    # O(1)
    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
    print(stack.stack_size())
