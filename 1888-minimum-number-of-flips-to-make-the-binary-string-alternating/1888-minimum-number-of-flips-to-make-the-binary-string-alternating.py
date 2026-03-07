class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s
        
      
        mismatches0 = 0 
        mismatches1 = 0  
        
        for i in range(n):
            if i % 2 == 0:
                if s2[i] != '0':
                    mismatches0 += 1
                if s2[i] != '1':
                    mismatches1 += 1
            else:
                if s2[i] != '1':
                    mismatches0 += 1
                if s2[i] != '0':
                    mismatches1 += 1
        
        ans = min(mismatches0, mismatches1)
        
        for i in range(1, n):
           
            if (i-1) % 2 == 0:  
                if s2[i-1] != '0':
                    mismatches0 -= 1
                if s2[i-1] != '1':
                    mismatches1 -= 1
            else:
                if s2[i-1] != '1':
                    mismatches0 -= 1
                if s2[i-1] != '0':
                    mismatches1 -= 1
       
            if (i+n-1) % 2 == 0:
                if s2[i+n-1] != '0':
                    mismatches0 += 1
                if s2[i+n-1] != '1':
                    mismatches1 += 1
            else:
                if s2[i+n-1] != '1':
                    mismatches0 += 1
                if s2[i+n-1] != '0':
                    mismatches1 += 1
            
            ans = min(ans, mismatches0, mismatches1)
        
        return ans