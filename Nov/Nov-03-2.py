print("Queue using linked list : ")

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def push(self,new_data):
        new_node=Node(new_data)
        
        if self.rear is None:
            self.rear=self.front=new_node
            return
        self.rear.next=new_node
        self.rear=new_node
    
    def is_pop(self):
        if self.front is None:
            print("queue is empty")
        else:
            self.front=self.front.next


    def display(self):
        if self.front is None:
            print("Queue is empty")
            return
        else:
            current=self.front
            while current:
                print(current.data)
                current=current.next

if __name__=="__main__":
    q=queue()
    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    q.push(50)

    q.display()

    print("remove first item :")
    q.is_pop()

    q.display()