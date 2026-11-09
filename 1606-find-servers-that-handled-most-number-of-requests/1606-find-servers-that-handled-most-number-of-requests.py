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