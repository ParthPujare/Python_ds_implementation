class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __contains__(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def __repr__(self):
        temp = self.head
        return_string = ''
        while temp:
            return_string += f"{temp.value}<==>"
            temp = temp.next
        return_string+=f"None"
        return return_string

    def __len__(self):
        temp = self.head
        count = 0
        while temp:
            count +=1
            temp = temp.next
        return count

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            newnode = Node(value)
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def prepend(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insert(self, value, index):
        length = len(self)
        if index<0 or index>=length:
            print (f"Invalid Index")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == len(self):
            self.append(value)
            return
        if index < (length//2):
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            newnode = Node(value)
            newnode.prev = temp
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode
        else:
            temp = self.tail
            for i in range(length-index-1):
                temp = temp.prev
            newnode = Node(value)
            newnode.next = temp
            newnode.prev = temp.prev
            temp.prev.next = newnode
            temp.prev= newnode

    def delete(self, value):
        if self.head is None:
            return("List is empty!")
        temp = self.head
        if temp.value == value:
            self.head = temp.next
            self.head.prev = None
            return
        while temp is not None and temp.value != value:
            temp = temp.next
        if temp is None:
            print("Element not found!")
        else:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

    def pop(self, index):
        if self.head is None:
            return("Empty list!")
        length = len(self)
        if index < 0 or index>=length:
            return("Invalid index")
        if self.head is not None and self.head.next == None and index==0:
            self.head = None
            return
        if index < length // 2:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
                return
            temp = self.head
            for i in range (index):
                temp = temp.next
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
        else:
            temp = self.tail
            if index == length-1:
                self.tail = self.tail.prev
                self.tail.next = None
                return
            for i in range(length-index-1):
                temp = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
             

    def get(self, index):
        if self.head == None:
            return("Empty list !")
        length = len(self)
        if index<0 or index>=length:
            return("Invalid index !")
        if index < length // 2:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return(temp.value)
        else:
            temp = self.tail
            for i in range (length-index-1):
                temp = temp.prev
            return(temp.value)

    def display(self):
        temp = self.head
        return_string = ''
        while temp:
            return_string += f"{temp.value}<==>"
            temp = temp.next
        return_string+=f"None"
        return return_string

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.append(60)

    print(dll.display())

    dll.prepend(5)

    dll.insert(50, 5)

    print(dll.display())

    dll.delete(10)
    dll.delete(100)
    print(dll.display())

    print(30 in dll)
    print(300 in dll)
    print(len(dll))
    print(dll.get(3))

    dll.pop(1)
    print(dll.display())