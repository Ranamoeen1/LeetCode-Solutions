from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        # Available servers maintained in sorted order
        available = SortedList(range(k))
        # Busy servers: min-heap of tuples (free_time, server_id)
        busy = []
        
        count = [0] * k
        
        for i in range(len(arrival)):
            t = arrival[i]
            
            # Free up servers whose load has finished by time t
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                available.add(s)
            
            if not available:
                continue # All servers are busy, drop request
                
            # Find the first available server >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            
            # If no server >= target is available, wrap around to the beginning
            if idx == len(available):
                idx = 0
            
            assigned = available[idx]
            available.remove(assigned)
            
            count[assigned] += 1
            heapq.heappush(busy, (t + load[i], assigned))
            
        max_requests = max(count) if count else 0
        return [i for i in range(k) if count[i] == max_requests]




# import heapq

# class Solution:
#     def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
#         # Segment tree of size 4*k to track available servers (1 = available, 0 = busy)
#         tree = [0] * (4 * k)
        
#         def build(node, l, r):
#             if l == r:
#                 tree[node] = 1
#                 return
#             mid = (l + r) // 2
#             build(2 * node, l, mid)
#             build(2 * node + 1, mid + 1, r)
#             tree[node] = tree[2 * node] + tree[2 * node + 1]
            
#         build(1, 0, k - 1)
        
#         def update(node, l, r, idx, val):
#             if l == r:
#                 tree[node] = val
#                 return
#             mid = (l + r) // 2
#             if idx <= mid:
#                 update(2 * node, l, mid, idx, val)
#             else:
#                 update(2 * node + 1, mid + 1, r, idx, val)
#             tree[node] = tree[2 * node] + tree[2 * node + 1]
            
#         def query(node, l, r, ql, qr):
#             if ql > r or qr < l or tree[node] == 0:
#                 return -1
#             if l == r:
#                 return l
#             mid = (l + r) // 2
#             res = query(2 * node, l, mid, ql, qr)
#             if res != -1:
#                 return res
#             return query(2 * node + 1, mid + 1, r, ql, qr)

#         busy = []
#         count = [0] * k
        
#         for i in range(len(arrival)):
#             t = arrival[i]
            
#             # Free up servers whose load has finished by time t
#             while busy and busy[0][0] <= t:
#                 _, s = heapq.heappop(busy)
#                 update(1, 0, k - 1, s, 1)
                
#             target = i % k
#             # Find first available server in [target, k - 1]
#             s = query(1, 0, k - 1, target, k - 1)
#             if s == -1:
#                 # Wrap around and search in [0, target - 1]
#                 s = query(1, 0, k - 1, 0, target - 1)
                
#             if s != -1:
#                 update(1, 0, k - 1, s, 0)
#                 count[s] += 1
#                 heapq.heappush(busy, (t + load[i], s))
                
#         max_requests = max(count) if count else 0
#         return [i for i in range(k) if count[i] == max_requests]

