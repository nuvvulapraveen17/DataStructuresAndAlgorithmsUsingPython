class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def len(self):
        if(self.head == None):
            print("length is: ", 0)
        else:
            print("length is: ", self.length)
    
    def push(self, data):
        #create a newnode
        newnode = Node(data)
        self.length += 1
        #empty queue
        if(self.head == None):
            self.head = self.tail = newnode
        else:
            #now make our last node points to newnode
            self.tail.next = newnode
            self.tail = newnode
    
    def pop(self):
        if(self.head == None and self.tail == None):
            return None
        
        else:
            popednode = self.head
            if(self.head == self.tail):
                self.head = self.tail = self.head.next
            else:
                self.head = self.head.next
            popednode.next = None
            self.length -= 1
            return popednode.data
    
    def peek(self):
        if(self.tail == None):
            return None
        else:
            return self.tail.data
    
    def display(self):
        iternode = self.head
        if(self.head == None):
            print("Queue is empty")
        else:
            # we will loop till we reach None
            while(iternode != None):
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            print("None")
    
if __name__== '__main__':
    q = Queue()
    q.push(10)
    q.push(20)
    q.len()
    q.push(2)
    q.push(12)
    q.len()
    q.push(0)
    q.display()
    q.len()
    q.pop()
    q.len()
    q.pop()
    q.push(30)
    q.push(40)
    q.display()
    q.len()
    q.push(50)
    q.pop()