class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.result = ""
        self.count = 0
        
        def backtrack(current):
            if self.result:
                return
            
            if len(current) == n:
                self.count += 1
                if self.count == k:
                    self.result = current
                return
            
            for char in ['a', 'b', 'c']:
                if current and current[-1] == char:
                    continue
                backtrack(current + char)
        
        backtrack("")
        return self.result   