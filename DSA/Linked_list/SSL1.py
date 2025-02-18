class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self,*data):
        node = Node(data[0])
        self.head = node

        if len(data) != 1:
            for d in data[1:]:
                self.push(d)



    def push(self,data):
        node = Node(data)
        current = self.head
        while current and current.next:
            current = current.next
        current.next = node

    def pop(self):
        current = self.head
        next = current.next
        while current and next.next:
            current = current.next
            next = current.next
        current.next = None

    def insert(self,mdata,data):
        node = Node(data)
        current = self.head
        next = current.next
        while current.data != mdata :
            current = current.next
            next = current.next

        current.next = node
        node.next = next

    def remove(self,mdata):
        current = self.head
        next = current.next
        while next.data != mdata :
            current = current.next
            next = current.next

        current.next = next.next


    def print_sl(self):
        current = self.head
        while current:
            print(current.data,"->",end="")
            current = current.next
        print("null")


sll = Sll(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)
sll.pop()
sll.print_sl()
sll.insert(10,15)
sll.print_sl()
sll.remove(15)
sll.print_sl()

