class myQueue:
    def __init__(self, n):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.n = n
        self.queue = [None] * n
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.n
    
    def enqueue(self, x):
        if self.isFull():
            print("Queue Overflow")
            return
        
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.n
        self.count += 1
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None
        
        x = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front +1) % self.n
        self.count -= 1
        return x
    
    def getFront(self):
        if self.isEmpty():
            return None
        return self.queue[self.front]
    
    def getRear(self):
        if self.isEmpty():
            return None
        return self.queue[(self.rear - 1) % self.rear]
    
    def size(self):
        return self.count
    
    def display(self):
        elements = [
            self.queue[(self.front + i) % self.n]
            for i in range(self.count)
        ]
        print(elements)
        
q = myQueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(4)
q.enqueue(2)
q.enqueue(8)
q.display()
print(q.dequeue())
q.display()
print(q.getFront())
print(q.getRear())