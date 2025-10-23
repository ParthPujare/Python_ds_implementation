class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):                                 ## Defining the stack 
        self.top = None
        self.size = 0
    
    def __len__(self):                                  ## Returning the size of the stack. TC ---> O(1)
        return self.size
    
    def __repr__(self):                                 ## Displaying the stack. Tc---->O(n)
        if self.is_empty():
            return "[]"
        else:
            temp = self.top
            return_list = []
            while temp:
                return_list.append(temp.value)
                temp = temp.next
            return str(return_list)

    def push(self, value):                              ## Adding element to the top of the stack. TC----> O(1)
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode
        self.size +=1

    def pop(self):                                      ## Removing and returning the top element. Tc --> O(1)
        node = self.top
        if node:
            self.top = self.top.next
            self.size -= 1
            return node.value
        else:
            return "Empty stack!"

    def peek(self):                                     ## Fetching the value of the top element. TC--> O(1)
        return self.top.value if self.top else None

    def is_empty(self):                                 ## Checking if the stack is empty. Tc --->O(1)
        return self.top is None
    
if __name__ == "__main__":
    st = Stack()

    st.push(10)
    st.push(20)
    print(st)
    st.push(30)
    print(len(st))
    print(st)
    print(st.pop())
    print(st.peek())
    st.pop()
    st.pop()
    print(st.is_empty())
    print(st.pop())
    print(len(st))