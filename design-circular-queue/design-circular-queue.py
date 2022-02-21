class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.size = k
        self.head = -1
        self.tail = -1
        

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        elif(self.tail ==-1):
            self.head+=1
            self.tail+=1
            self.queue[self.tail] = value
        else:
            self.tail = (self.tail+1)%self.size
            self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        elif(self.head==self.tail):
            self.head=-1
            self.tail=-1
        else:
            self.head = (self.head+1)%self.size
        return True
        

    def Front(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if(self.isEmpty()):
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
       
        return self.head==-1 and self.tail == -1

    def isFull(self) -> bool:
        if((self.tail+1)%self.size == self.head):
            return True
        return False
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()