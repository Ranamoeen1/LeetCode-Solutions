from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # Allocate 2 * N nodes for an iterative segment tree
        tree_prod = [1] * (2 * n)
        # tree_cnt[i] is a list of size k storing prefix product counts modulo k
        tree_cnt = [[0] * k for _ in range(2 * n)]

        # Pre-process nums modulo k
        for i in range(n):
            v = nums[i] % k
            tree_prod[n + i] = v
            tree_cnt[n + i][v] = 1

        # Build tree bottom-up in O(N * k)
        for i in range(n - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            p_left = tree_prod[left]
            
            tree_prod[i] = (p_left * tree_prod[right]) % k
            cnt = list(tree_cnt[left])
            c_right = tree_cnt[right]
            for r in range(k):
                if c_right[r]:
                    cnt[(p_left * r) % k] += c_right[r]
            tree_cnt[i] = cnt

        def update(idx: int, val: int):
            pos = n + idx
            v = val % k
            tree_prod[pos] = v
            tree_cnt[pos] = [0] * k
            tree_cnt[pos][v] = 1

            pos //= 2
            while pos > 0:
                left = 2 * pos
                right = 2 * pos + 1
                p_left = tree_prod[left]
                
                tree_prod[pos] = (p_left * tree_prod[right]) % k
                cnt = list(tree_cnt[left])
                c_right = tree_cnt[right]
                for r in range(k):
                    if c_right[r]:
                        cnt[(p_left * r) % k] += c_right[r]
                tree_cnt[pos] = cnt
                pos //= 2

        def query_suffix(L: int) -> List[int]:
            # Range query for suffix [L, N - 1]
            left_node = L + n
            right_node = (n - 1) + n
            
            res_prod = 1
            res_cnt = [0] * k
            
            # Since query is always suffix [L, N-1], iterative bottom-up interval query
            # collects sub-blocks in strictly left-to-right order.
            right_blocks = []
            
            while left_node <= right_node:
                if left_node % 2 == 1:
                    # Combine res_cnt with tree_cnt[left_node]
                    p_left = res_prod
                    c_curr = tree_cnt[left_node]
                    for r in range(k):
                        if c_curr[r]:
                            res_cnt[(p_left * r) % k] += c_curr[r]
                    res_prod = (res_prod * tree_prod[left_node]) % k
                    left_node += 1
                
                if right_node % 2 == 0:
                    right_blocks.append(right_node)
                    right_node -= 1
                    
                left_node //= 2
                right_node //= 2

            for node in reversed(right_blocks):
                p_left = res_prod
                c_curr = tree_cnt[node]
                for r in range(k):
                    if c_curr[r]:
                        res_cnt[(p_left * r) % k] += c_curr[r]
                res_prod = (res_prod * tree_prod[node]) % k

            return res_cnt

        ans = []
        for idx, val, start, x in queries:
            update(idx, val)
            cnts = query_suffix(start)
            ans.append(cnts[x])

        return ans





# class Solution:
#     def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
#         n = len(nums)
#         if k == 1:
#             return [n - q[2] if q[3] == 0 else 0 for q in queries]

#         # Allocate flat tree structures for better cache locality and performance
#         # Tree size rounded to next power of 2
#         size = 1
#         while size < n:
#             size <<= 1
            
#         tree_prod = [1] * (2 * size)
#         # tree_cnt[node][start_rem][target_rem]
#         tree_cnt = [[[0] * k for _ in range(k)] for _ in range(2 * size)]

#         # Initialize leaves
#         for i in range(n):
#             node = size + i
#             val = nums[i] % k
#             tree_prod[node] = val
#             for r in range(k):
#                 tree_cnt[node][r][(r * val) % k] = 1

#         # Build tree bottom-up
#         for node in range(size - 1, 0, -1):
#             left = 2 * node
#             right = 2 * node + 1
            
#             p_left = tree_prod[left]
#             tree_prod[node] = (p_left * tree_prod[right]) % k
            
#             c_node = tree_cnt[node]
#             c_left = tree_cnt[left]
#             c_right = tree_cnt[right]
            
#             for r in range(k):
#                 r_after_left = (r * p_left) % k
#                 c_node_r = c_node[r]
#                 c_left_r = c_left[r]
#                 c_right_next = c_right[r_after_left]
#                 for x in range(k):
#                     c_node_r[x] = c_left_r[x] + c_right_next[x]

#         def update(idx: int, val: int):
#             val %= k
#             node = size + idx
#             tree_prod[node] = val
            
#             c_node = tree_cnt[node]
#             for r in range(k):
#                 for x in range(k):
#                     c_node[r][x] = 0
#                 c_node[r][(r * val) % k] = 1
            
#             node >>= 1
#             while node > 0:
#                 left = 2 * node
#                 right = 2 * node + 1
                
#                 p_left = tree_prod[left]
#                 tree_prod[node] = (p_left * tree_prod[right]) % k
                
#                 c_node = tree_cnt[node]
#                 c_left = tree_cnt[left]
#                 c_right = tree_cnt[right]
                
#                 for r in range(k):
#                     r_after_left = (r * p_left) % k
#                     c_node_r = c_node[r]
#                     c_left_r = c_left[r]
#                     c_right_next = c_right[r_after_left]
#                     for x in range(k):
#                         c_node_r[x] = c_left_r[x] + c_right_next[x]
                        
#                 node >>= 1

#         def query_suffix(start: int) -> List[int]:
#             # Range query for suffix [start, n - 1]
#             l = size + start
#             r = size + n - 1
            
#             left_nodes = []
#             right_nodes = []
            
#             while l <= r:
#                 if l % 2 == 1:
#                     left_nodes.append(l)
#                     l += 1
#                 if r % 2 == 0:
#                     right_nodes.append(r)
#                     r -= 1
#                 l >>= 1
#                 r >>= 1
                
#             nodes = left_nodes + right_nodes[::-1]
            
#             # Combine canonical nodes from left to right starting with initial remainder 1
#             cur_rem = 1
#             ans = [0] * k
            
#             for node in nodes:
#                 cnt_node = tree_cnt[node][cur_rem]
#                 for x in range(k):
#                     ans[x] += cnt_node[x]
#                 cur_rem = (cur_rem * tree_prod[node]) % k
                
#             return ans

#         res = []
#         for idx, val, start, target_x in queries:
#             update(idx, val)
#             ans = query_suffix(start)
#             res.append(ans[target_x])
            
#         return res