class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        print("POP " + str(self.queue.pop(0)))
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

    def sort_queue(self):
        queue = self.queue
        size = self.size()

        for i in range(size):
            for j in range(size - i - 1):
                if queue[j] > queue[j + 1]:
                    queue[j], queue[j + 1] = queue[j + 1], queue[j]

        return queue
        

if __name__ == "__main__":
    import random
    
    q = Queue()
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    q.enqueue(random.randint(0, 20))
    
    q.display()
    
    q.sort_queue()
    q.display()
    
    q.dequeue()
    print("After removing an element")
    q.display()
