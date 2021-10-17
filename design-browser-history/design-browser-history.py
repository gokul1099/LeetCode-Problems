class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = homepage
        self.backHistory=[]
        self.frwdHistory =[]
        

    def visit(self, url: str) -> None:
        
        self.backHistory.append(self.curr)
        self.curr = url
        self.frwdHistory=[]
        return self.curr
    def back(self, steps: int) -> str:
        while(steps and len(self.backHistory)):
            self.frwdHistory.append(self.curr)
            self.curr = self.backHistory.pop()
            steps-=1
        return self.curr

    def forward(self, steps: int) -> str:
        while(steps and len(self.frwdHistory)):
            self.backHistory.append(self.curr)
            self.curr=self.frwdHistory.pop()
            steps-=1
        return self.curr    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)