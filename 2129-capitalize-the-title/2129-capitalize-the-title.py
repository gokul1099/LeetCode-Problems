class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title= title.split(" ")
        for i in range(len(title)):
            if(len(title[i]) ==1 or len(title[i])==2):
                title[i] = title[i].lower()
            else:
                temp = title[i]
                temp = temp[0].upper() + temp[1:].lower()
                title[i] = temp
        return (" ".join(title))        
        