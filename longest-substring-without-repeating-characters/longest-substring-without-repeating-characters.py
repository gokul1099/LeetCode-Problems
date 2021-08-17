class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_ptr,b_ptr = 0,0
        max_length=0
        hashMap={}
        while(b_ptr <len(s)):
            if(s[b_ptr] not in hashMap):
                hashMap[s[b_ptr]]=1
                max_length=max(len(hashMap),max_length)
                b_ptr+=1
            else:
                del hashMap[s[a_ptr]]
                a_ptr+=1
        return max_length            
                
        