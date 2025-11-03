class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node_element=[]
count=5
while count:
    num=int(input("Enter the number : "))
    node_element.append(num)
    count-=1

nodes=[]

for item in node_element:
    # node=Node(item)
    nodes.append(Node(item))

# nodes=[Node(item) for item in node_element]

# n1=Node(53)
# n2=Node(95)
# n3=Node(12)
# n4=Node(32)

n1.next=n2
n2.next=n3
n3.next=n4

class LinkedList:
    def __init__(self):
        self.head=None

    def traversal(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("Null")

def main():
    ll=LinkedList()
    ll.head=n1
    ll.traversal()

if __name__=="__main__":
    main()

