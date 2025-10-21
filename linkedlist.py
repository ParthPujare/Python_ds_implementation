class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def __repr__(self):                             ##Returns the entire list. TC ---> O(n)
        if self.head == None:
            return "[]" 
        else:
            temp = self.head
            return_string = f"[{temp.value}"
            while temp.next!=None:
                temp = temp.next
                return_string+=f"-->{temp.value}"
            return_string+=f"-->{None}]"

            return return_string

    def __contains__(self, value):                  ##Checks if the value is present in the list. TC--->O(n)
        if self.head == None:
            return(False)
        else:
            temp = self.head
            while temp != None:
                if temp.value == value:
                    return(True)
                temp= temp.next
            return(False)
    
    def __len__(self):                              ##Retruns the length of the list. TC--->O(n)
        if self.head == None:
            return(0)
        else:
            counter = 0 
            temp = self.head
            while temp.next !=None:
                temp = temp.next
                counter+=1
            return(counter+1)

    def append(self, value):                        ##Append the new node to the end of the list. TC ----> O(n)
        if self.head == None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = Node(value)


    def prepend(self, value):                       ## Adding a new node to the start of the list. TC----> O(1)
        newhead = Node(value)
        newhead.next = self.head
        self.head = newhead

    def insert(self, value, index):                 ## Adding a node at a given index . TC----> O(n)
        newnode = Node(value)
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        newnode.next = temp.next
        temp.next = newnode

    def delete(self, value):                        ##Deleting a node based on its value .TC------> O(ns)
        if self.head == None:
            print("List is already empty!")
        else:
            temp= self.head
            if temp.next == None and temp.value == value:
                self.head = None
            elif temp.value == value and temp.next != None:
                self.head = temp.next
            else:
                found = False
                while temp.next != None:
                    if temp.next.value == value:
                        if temp.next.next == None:
                            temp.next = None
                            found = True
                        else:
                            temp.next = temp.next.next
                            found = True
                    else:
                        temp = temp.next
                if not found:
                    print("Element not in list")

    def pop(self, index):                           ##Deleting a node based on its index .TC------> O(ns)
        if index not in range(len(self)):
            print("Not a  valid index!")
        else:
            if index ==0:
                self.head = self.head.next
            else:
                temp = self.head
                for i in range(index-1):
                    temp = temp.next
                
                temp.next = temp.next.next

    def get(self, index):                           ##Getting the value at a particular index. TC------> O(n)
        if index not in range(len(self)):
            print("Not a valid index!")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.value
    
    def display(self):                                ##Displaying the entire linked list. TC ----> O(n)
        if self.head == None:
            return("Empty list!")
        else:
            temp = self.head
            while temp:
                print(f"{temp.value}-->",end="")
                temp = temp.next
            print('None')

if __name__ == "__main__":
    ll = Linkedlist()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(60)

    ll.display()

    ll.prepend(5)

    ll.insert(50, 5)

    ll.display()

    ll.delete(10)
    ll.delete(100)
    ll.display()

    print(30 in ll)
    print(300 in ll)
    print(len(ll))
    print(ll.get(3))

    ll.pop(1)
    ll.display()