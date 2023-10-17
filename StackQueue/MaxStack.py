class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    # O(1)
    def is_empty(self):
        return self.main_stack == []

    # O(1)
    def stack_size(self):
        return len(self.main_stack)

    # O(1)
    def push(self, data):
        self.main_stack.append(data)

        if self.stack_size() == 1:
            self.max_stack.append(data)
            return

        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    # O(1)
    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop()

    # Time Complex: O(1) but we use O(N) Space Complex to calculate.
    def get_max(self):
        return self.max_stack.pop()


if __name__ == '__main__':
    stack = MaxStack()
    stack.push(100)
    stack.push(2)
    stack.push(3)
    stack.push(6)
    stack.push(1)

    print(stack.pop())
    print(stack.pop())
    print(stack.get_max())
