class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        parsedMailId=[]
        def replaceNonchar(id):
            for i in range(len(id)):
                if(i >= len(id)):
                    return id
                if(id[i])== ".":
                    id = id[:i]+id[i+1:]
                if(id[i] == "+"):
                    id = id[:i]
            return id     
                    
        for mail in emails:
            temp = mail.split('@')
            mailId = temp[0]
            domain = temp[1]
            parsedId =  replaceNonchar(mailId) + "@"+domain
            print(parsedId)
            if(parsedId not in parsedMailId):
                parsedMailId.append(parsedId)
        return len(parsedMailId) 