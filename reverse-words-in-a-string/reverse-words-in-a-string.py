class Solution:
    def reverseWords(self, s: str) -> str:
        
        arr = s.strip().split(" ")
        arr= arr[::-1]
        arr = [i for i in arr if i!=""]
        return " ".join(arr)