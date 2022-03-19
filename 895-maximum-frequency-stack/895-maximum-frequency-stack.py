class FreqStack(object):

    def __init__(self):
        self.stack = {}
        self.freq = {}
        self.maxFreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(val in self.freq):
            self.freq[val] +=1
        else:
            self.freq[val]=1
        freqVal = self.freq[val]
        if(freqVal > self.maxFreq):
            self.maxFreq = freqVal
        if(freqVal in self.stack):
            self.stack[freqVal].append(val)
        else:
            self.stack[freqVal]=[val]
    def pop(self):
        """
        :rtype: int
        """
        toReturn = self.stack[self.maxFreq].pop()
        self.freq[toReturn]-=1
        if not self.stack[self.maxFreq]:
            self.maxFreq-=1
        return toReturn
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()