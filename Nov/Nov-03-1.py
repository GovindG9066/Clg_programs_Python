class queue:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.items)
    
    def mypop(self):
        if self.is_empty():
            print("Queue is already empty")
        else:
            self.items.pop(0)

if __name__=="__main__":
    q=queue()

    q.push(10)
    q.push(20)
    q.push(30)
    q.push(40)
    q.push(50)

    q.display()

    q.mypop()

    q.display()