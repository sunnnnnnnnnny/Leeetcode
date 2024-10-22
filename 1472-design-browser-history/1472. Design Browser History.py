class BrowserHistory:

    def __init__(self, homepage: str):
        # could use stack for back and queue for forward
        # the current page will be on top of stack
        # while the homepage can be either a static of the first of stack
        self.home = homepage
        self.front = []
        self.sec = []

    def visit(self, url: str) -> None:
        self.front.append(url)
        self.sec = []

    def back(self, steps: int) -> str:
        i=0
        while len(self.front)>0 and i<steps:
            pre = self.front.pop()
            self.sec.insert(0,pre)
            i+=1
        if len(self.front) == 0:
            return self.home
        return self.front[-1]

    def forward(self, steps: int) -> str:
        i=0
        while len(self.sec)>0 and i<steps:
            pre = self.sec.pop(0)
            self.front.append(pre)
            i+=1
        if len(self.front) == 0:
            return self.home
        return self.front[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)