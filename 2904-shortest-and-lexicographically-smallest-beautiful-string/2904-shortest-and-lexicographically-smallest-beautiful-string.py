class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Find all 0-based indices where s[i] == '1'
        ones_indices = [i for i, char in enumerate(s) if char == '1']
        
        # If there are fewer than k ones, no beautiful substring exists
        if len(ones_indices) < k:
            return ""
        
        min_len = float('inf')
        ans = ""
        
        # Iterate over all possible windows of k ones
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            
            candidate = s[start : end + 1]
            cand_len = len(candidate)
            
            # If candidate is shorter, or same length but lexicographically smaller
            if cand_len < min_len:
                min_len = cand_len
                ans = candidate
            elif cand_len == min_len:
                if candidate < ans:
                    ans = candidate
                    
        return ans