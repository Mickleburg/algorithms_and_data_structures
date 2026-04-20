class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


def stack_sort(stackM: Stack) -> Stack:
    stackT = Stack()

    while not stackM.is_empty():
        el = stackM.pop()

        while not stackT.is_empty() and stackT.peek() > el:
            stackM.push(stackT.pop())

        stackT.push(el)

    while not stackT.is_empty():
        stackM.push(stackT.pop())

    return stackM


stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)

stack_sort(stack)

assert stack.data == [4, 3, 2, 1], "Тест 1 - ошибка"
assert stack.peek() == 1, "Ошибка с минимумом"

print("OK")
