class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # If the destination itself is blocked, we can never reach it
        if s[n - 1] == '1':
            return False
            
        # dp[i] will be True if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        reachable_count = 0
        
        for i in range(1, n):
            # Add the index that just entered the window [i - maxJump, i - minJump]
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
                    
            # Remove the index that just left the window
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # If the current character is '0' and there is at least one 
            # reachable index in our jumping window, then index i is reachable.
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
                
        return dp[n - 1]