# from typing import List
# from collections import defaultdict, Counter

# class Solution:
#     def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
#         n = len(source)
#         parent = list(range(n))
        
#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])
#             return parent[x]
        
#         def union(x, y):
#             px, py = find(x), find(y)
#             if px != py:
#                 parent[px] = py
        
#         # Build connected components using allowed swaps
#         for a, b in allowedSwaps:
#             union(a, b)
        
#         # Group indices by their component root
#         components = defaultdict(list)
#         for i in range(n):
#             root = find(i)
#             components[root].append(i)
        
#         # For each component, check how many positions can match
#         hamming_distance = 0
        
#         for root, indices in components.items():
#             # Count available values from source in this component
#             source_count = Counter()
#             for idx in indices:
#                 source_count[source[idx]] += 1
            
#             # Try to match target values with source values in this component
#             for idx in indices:
#                 target_val = target[idx]
#                 if source_count[target_val] > 0:
#                     # We can match this position
#                     source_count[target_val] -= 1
#                 else:
#                     # Cannot match this position
#                     hamming_distance += 1
        
#         return hamming_distance


from typing import List
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        size = [1] * n
        
        def find(x):
            # Iterative find with path compression
            root = x
            while root != parent[root]:
                root = parent[root]
            # Path compression
            while x != root:
                nxt = parent[x]
                parent[x] = root
                x = nxt
            return root
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            # Union by size
            if size[rx] < size[ry]:
                parent[rx] = ry
                size[ry] += size[rx]
            else:
                parent[ry] = rx
                size[rx] += size[ry]
        
        # Build DSU
        for a, b in allowedSwaps:
            union(a, b)
        
        # Compress all paths
        for i in range(n):
            parent[i] = find(i)
        
        # Build component maps: root -> Counter of source values
        component_sources = defaultdict(Counter)
        
        # Single pass to populate source counters
        for i in range(n):
            component_sources[parent[i]][source[i]] += 1
        
        # Calculate Hamming distance
        distance = 0
        for i in range(n):
            root = parent[i]
            if component_sources[root][target[i]] > 0:
                component_sources[root][target[i]] -= 1
            else:
                distance += 1
        
        return distance