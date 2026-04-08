class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        n = len(nums)
        
        # Optimization: Since XOR is not linear with multiplication,
        # we cannot easily combine. But we can use the constraint that
        # n, q <= 1000, so O(n*q) = 10^6 is actually acceptable.
        
        # However, for true optimization, note that queries are independent
        # and we can reorder them. Also, we can use bit-parallel techniques
        # or process multiple queries simultaneously using SIMD-like approach
        
        # Practical optimization: Precompute all affected indices for each query
        # and use union-find or disjoint set to skip already-processed indices
        # if queries overlap (but multiplication is not idempotent, so this doesn't work)
        
        # Best optimization: Use the fact that MOD = 10^9+7 is prime
        # Convert to exponents: represent each number as g^e where g is primitive root
        # Then multiplication becomes addition in exponent space
        # But XOR in exponent space is not simple
        
        # Given constraints, the most practical "optimization" is using 
        # numpy-style vectorization or reducing Python overhead
        
        # Micro-optimization: Use local variables, avoid attribute lookups
        mod = MOD
        arr = nums  # reference, not copy
        
        for q in queries:
            l, r, k, v = q
            # Unroll loop for small k?
            idx = l
            # Use while loop which is faster than range with step for variable step
            while idx <= r:
                arr[idx] = (arr[idx] * v) % mod
                idx += k
        
        # Compute XOR using reduce or loop unrolling
        res = 0
        for x in arr:
            res ^= x
        return res



# class Solution:
#     def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
#         MOD = 10**9 + 7
        
#         n = len(nums)
        
#         # Key insight: Use the fact that 10^9+7 is prime
#         # We can use Fermat's little theorem: a^(p-1) ≡ 1 (mod p)
#         # So multiplication by v is equivalent to adding log(v) in exponent space
        
#         # Alternative: Use prefix product with modular inverses for O(1) range product queries
#         # But the step k makes this tricky
        
#         # Best practical optimization: Block decomposition (sqrt decomposition)
#         # Divide array into blocks of size B ≈ sqrt(n)
#         # For each block, precompute lazy multipliers for each possible k
        
#         B = int(n**0.5) + 1  # block size
        
#         # For small k (k <= B), we can use difference arrays efficiently
#         # For large k (k > B), each query touches at most n/k < B elements
        
#         # Separate queries by k value
#         small_k_queries = []  # k <= B
#         large_k_queries = []  # k > B
        
#         for l, r, k, v in queries:
#             if k <= B:
#                 small_k_queries.append((l, r, k, v))
#             else:
#                 large_k_queries.append((l, r, k, v))
        
#         # For small k: use difference arrays per (k, residue) pair
#         # diff[k][residue][i] = product multiplier for index i with i%k = residue
        
#         # diff[k] is a dictionary: residue -> list of (position, cumulative_product)
#         # Actually use: for each k, maintain an array of size n for lazy propagation
        
#         multipliers = [1] * n
        
#         # Process small k queries with difference arrays
#         # For each k, we maintain diff arrays for each residue class
#         for l, r, k, v in small_k_queries:
#             # For arithmetic progression l, l+k, l+2k, ... in [l,r]
#             # Use: start at l, mark multiply by v, end at r+k mark divide by v (using inverse)
#             # But product difference array is tricky with modulo
            
#             # Instead: for small k, we can afford O(n/k) per query which is O(n/B) = O(sqrt(n))
#             # Total for small k: O(q * sqrt(n))
#             idx = l
#             while idx <= r:
#                 multipliers[idx] = (multipliers[idx] * v) % MOD
#                 idx += k
        
#         # Process large k queries: each touches at most n/k < B elements
#         # Total: O(q * B) = O(q * sqrt(n))
#         for l, r, k, v in large_k_queries:
#             idx = l
#             while idx <= r:
#                 multipliers[idx] = (multipliers[idx] * v) % MOD
#                 idx += k
        
#         # Apply multipliers and compute XOR
#         result = 0
#         for i in range(n):
#             result ^= (nums[i] * multipliers[i]) % MOD
        
#         return result


# # class Solution:
# #     def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
# #         MOD = 10**9 + 7
        
# #         # Process each query
# #         for l, r, k, v in queries:
# #             idx = l
# #             while idx <= r:
# #                 nums[idx] = (nums[idx] * v) % MOD
# #                 idx += k
        
# #         # Calculate XOR of all elements
# #         result = 0
# #         for num in nums:
# #             result ^= num
        
# #         return result