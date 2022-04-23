class Codec:
    def __init__(self):
        self.urlHashMap = {}
        self.hash = set()
    def randomword(self,length):
        letters = string.ascii_letters + "1234567890"
        return ''.join(random.choice(letters) for i in range(length))    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if(longUrl not in self.urlHashMap.values()):
            hashVal = self.randomword(6)
            while hashVal not in self.hash:
                hashVal  = self.randomword(6)
                self.hash.add(hashVal)
            hashVal = "http://tinyurl.com/" + hashVal
            self.urlHashMap[hashVal] = longUrl
            return hashVal    
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urlHashMap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))