class MyHashSet:

    def __init__(self):
        self.size= 10
        self.hashSet = [None]*self.size
    def hashFn(self,value):
        return value%self.size
    def add(self, key: int) -> None:
        hashValue = self.hashFn(key)
        
        if self.hashSet[hashValue] == None:
            self.hashSet[hashValue]  = [key]
        else:
            self.hashSet[hashValue].append(key)
        
    def remove(self, key: int) -> None:
        hashValue = self.hashFn(key)
        if self.hashSet[hashValue]!=None:
            while key in self.hashSet[hashValue]:
                self.hashSet[hashValue].remove(key)
    def contains(self, key: int) -> bool:
        hashValue = self.hashFn(key)
        if self.hashSet[hashValue]!=None:
            return key in self.hashSet[hashValue]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)