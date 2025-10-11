print("Oct-11")

print("Singly LinkedList...:")

# travels /print linkedlist items

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(54)
n2=Node(5)
n3=Node(64)
n4=Node(654)

n1.next=n2
n2.next=n3
n3.next=n4


class Linkedlist:
    
    def __init__(self):
        self.head=None

    def traversal(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next


def main():
    llist=Linkedlist()
    llist.head=n1
    llist.traversal()
    
if __name__=="__main__":
    main()