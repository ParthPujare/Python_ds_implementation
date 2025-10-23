class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __repr__(self):
        if self.front == None:
            return "[]" 
        else:
            temp = self.front
            returnlst = []
            while temp:
                returnlst.append(temp.value)
                temp = temp.next
            return str(returnlst)
    
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        if self.front == None:
            self.front = Node(value)
            self.rear = self.front
        else:
            newnode = Node(value)
            self.rear.next = newnode
            self.rear = newnode
        self.size+=1

    def dequeue(self):
        if self.front == None:
            raise IndexError ("Queue is empty !")
        else:
            if self.front == self.rear:
                node = self.front
                self.front = self.rear = None
            else:
                node = self.front
                self.front = self.front.next
            self.size -= 1
            return node.value

    def peek(self):
        if self.front == None:
            raise IndexError( "Queue is empty !")
        else:
            return self.front.value

    def is_empty(self):
        return  self.front is None
    
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    print(q)
    print(len(q))
    print(q.is_empty())
    q.enqueue(30)
    print(q)
    print(len(q))
    q.dequeue()
    print(q)
    print(q.peek())
    q.dequeue()
    q.dequeue()
    print(q)
    print(q.is_empty())
    print(len(q))
    print(q.dequeue())