class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.len = 0
    def length(self):
        if(self.head == None):
            print("length is: ", 0)
        else:
            print("length is: ", self.len)

    def isempty(self):
        if (self.head == None):
            return True
        else:
            return False
    
    def push(self, data):
        # check weather stack is empty
        self.len += 1
        if (self.head == None):
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    def pop(self):
        # check weather it is empty or not
        if (self.head == None):
            return None
        else:
            # we have to remove node from head of LL
            self.len -= 1
            popedNode = self.head
            self.head = self.head.next
            popedNode.next = None
            return popedNode.data
    def peek(self):
        if (self.head == None):
            return None
        else:
            return self.head.data
    def display(self):
        iternode = self.head
        if (self.head == None):
            print("Stack is Empty")
        else:
            # we will loop till we reach None
            while(iternode != None):
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            print("None")
            return
if __name__ == "__main__":
    MyStack = Stack()
    MyStack.push(11)
    MyStack.length()
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
    MyStack.length()
    MyStack.push(14)
    MyStack.push(4)
    MyStack.push(9)
    MyStack.display()
    MyStack.length()
    print("\nTop element is ",MyStack.peek())
    # Delete top elements of stack
    MyStack.pop()
    MyStack.length()
    MyStack.pop()
    # Display stack elements
    MyStack.display()
    MyStack.length()
    # Print top element of stack
    print("\nTop element is ", MyStack.peek())
