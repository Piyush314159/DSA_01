class myStack:
    def __init__(self, n):
        self.top = -1
        self.n = n
        self.stack = [None] * n

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1

    def push(self, x):
        if self.isFull():
            print("Stack Overflow")
            return

        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
            return None

        x = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return x

    def peek(self):
        if self.isEmpty():
            return None

        return self.stack[self.top]
    
    def size(self):
        return self.top + 1

    def display(self):
        print(self.stack[:self.top+1])
    
s = myStack(4)
s.push(4)
s.push(3)
s.push(5)
s.push(6)

s.display()
print(s.peek())