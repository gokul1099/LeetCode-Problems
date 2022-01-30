@lru_cache(None)
def helper(i):
if i<0:
return True
for word in  wordDict:
if(i >= len(word)-1 and helper(i-len(word))):
if(s[i-len(word)+1 : i+1]  == word):
return True
return False
return helper(len(s)-1)