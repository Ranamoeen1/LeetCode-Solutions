class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        C = [0] * n
        seen_count = [0] * (n + 1)
        common_elements = 0
        
        for i in range(n):
            # Process element from array A
            seen_count[A[i]] += 1
            if seen_count[A[i]] == 2:
                common_elements += 1
                
            # Process element from array B
            seen_count[B[i]] += 1
            if seen_count[B[i]] == 2:
                common_elements += 1
                
            # Store the running count for the current prefix
            C[i] = common_elements
            
        return C