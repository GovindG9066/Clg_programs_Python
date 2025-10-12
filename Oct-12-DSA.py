print("DSA")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def traversal(self,head):
        current=head
        while current:
            print(current.data,end="->")
            current=current.next
        print("Null")

    def insert_at_beginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node


n1=Node(25)
n2=Node(50)
n3=Node(75)
n4=Node(100)

n1.next=n2
n2.next=n3
n3.next=n4

def main():
    ll=LinkedList()
    ll.head=n1
    ll.insert_at_beginning(101)
    ll.traversal(ll.head)

if __name__=="__main__":
    main()