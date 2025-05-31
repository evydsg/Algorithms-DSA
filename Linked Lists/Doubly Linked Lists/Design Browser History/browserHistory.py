class ListNode:
    def __init__(self, url):
        self.url = url
        self.nxt = None
        self.prv = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        if self.current is None:
            self.current = ListNode(url)
            return
        else:
            current_website = ListNode(url)
            self.current.nxt = current_website
            current_website.prv = self.current
            self.current = current_website
            return
            
    def back(self, steps: int) -> str:
        count = 0

        while count < steps and self.current.prv:
            if count == steps:
                return current.val
            
            count += 1
            self.current = self.current.prv
        
        return self.current.url
        
    def forward(self, steps: int) -> str:
        count = 0

        while count < steps and self.current.nxt:
            if count == steps:
                return self.current.url
            
            count += 1
            self.current = self.current.nxt
        
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)