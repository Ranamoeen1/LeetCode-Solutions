class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        
        # Key insight: Use the fact that 10^9+7 is prime
        # We can use Fermat's little theorem: a^(p-1) ≡ 1 (mod p)
        # So multiplication by v is equivalent to adding log(v) in exponent space
        
        # Alternative: Use prefix product with modular inverses for O(1) range product queries
        # But the step k makes this tricky
        
        # Best practical optimization: Block decomposition (sqrt decomposition)
        # Divide array into blocks of size B ≈ sqrt(n)
        # For each block, precompute lazy multipliers for each possible k
        
        B = int(n**0.5) + 1  # block size
        
        # For small k (k <= B), we can use difference arrays efficiently
        # For large k (k > B), each query touches at most n/k < B elements
        
        # Separate queries by k value
        small_k_queries = []  # k <= B
        large_k_queries = []  # k > B
        
        for l, r, k, v in queries:
            if k <= B:
                small_k_queries.append((l, r, k, v))
            else:
                large_k_queries.append((l, r, k, v))
        
        # For small k: use difference arrays per (k, residue) pair
        # diff[k][residue][i] = product multiplier for index i with i%k = residue
        
        # diff[k] is a dictionary: residue -> list of (position, cumulative_product)
        # Actually use: for each k, maintain an array of size n for lazy propagation
        
        multipliers = [1] * n
        
        # Process small k queries with difference arrays
        # For each k, we maintain diff arrays for each residue class
        for l, r, k, v in small_k_queries:
            # For arithmetic progression l, l+k, l+2k, ... in [l,r]
            # Use: start at l, mark multiply by v, end at r+k mark divide by v (using inverse)
            # But product difference array is tricky with modulo
            
            # Instead: for small k, we can afford O(n/k) per query which is O(n/B) = O(sqrt(n))
            # Total for small k: O(q * sqrt(n))
            idx = l
            while idx <= r:
                multipliers[idx] = (multipliers[idx] * v) % MOD
                idx += k
        
        # Process large k queries: each touches at most n/k < B elements
        # Total: O(q * B) = O(q * sqrt(n))
        for l, r, k, v in large_k_queries:
            idx = l
            while idx <= r:
                multipliers[idx] = (multipliers[idx] * v) % MOD
                idx += k
        
        # Apply multipliers and compute XOR
        result = 0
        for i in range(n):
            result ^= (nums[i] * multipliers[i]) % MOD
        
        return result


# class Solution:
#     def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
#         MOD = 10**9 + 7
        
#         # Process each query
#         for l, r, k, v in queries:
#             idx = l
#             while idx <= r:
#                 nums[idx] = (nums[idx] * v) % MOD
#                 idx += k
        
#         # Calculate XOR of all elements
#         result = 0
#         for num in nums:
#             result ^= num
        
#         return result