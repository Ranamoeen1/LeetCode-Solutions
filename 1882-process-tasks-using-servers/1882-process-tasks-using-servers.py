import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Min-heap for available servers: stores (weight, index)
        free_servers = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(free_servers)
        
        # Min-heap for busy servers: stores (free_time, weight, index)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j, task_time in enumerate(tasks):
            curr_time = max(curr_time, j)
            
            # If no servers are free, fast-forward time to when the next server becomes available
            if not free_servers and busy_servers:
                curr_time = max(curr_time, busy_servers[0][0])
                
            # Release all servers that finish at or before curr_time
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_t, weight, i = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, i))
                
            # Assign the task to the best available server
            weight, i = heapq.heappop(free_servers)
            ans.append(i)
            
            # Push the server into the busy heap with its new release time
            heapq.heappush(busy_servers, (curr_time + task_time, weight, i))
            
        return ans



# import heapq

# class Solution:
#     def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
#         # free_servers heap: (weight, index)
#         free_servers = [(weight, i) for i, weight in enumerate(servers)]
#         heapq.heapify(free_servers)
        
#         # busy_servers heap: (free_time, weight, index)
#         busy_servers = []
        
#         ans = []
#         curr_time = 0
        
#         for j, task_time in enumerate(tasks):
#             # Current time must be at least the task arrival time j
#             curr_time = max(curr_time, j)
            
#             # Release all servers that have finished processing by curr_time
#             while busy_servers and busy_servers[0][0] <= curr_time:
#                 free_t, weight, i = heapq.heappop(busy_servers)
#                 heapq.heappush(free_servers, (weight, i))
                
#             # If no free servers are available, jump time to when the earliest busy server finishes
#             if not free_servers:
#                 curr_time = busy_servers[0][0]
#                 while busy_servers and busy_servers[0][0] <= curr_time:
#                     free_t, weight, i = heapq.heappop(busy_servers)
#                     heapq.heappush(free_servers, (weight, i))
            
#             # Assign the best available server to the j-th task
#             weight, i = heapq.heappop(free_servers)
#             ans.append(i)
            
#             # Mark the server as busy until curr_time + task_time
#             heapq.heappush(busy_servers, (curr_time + task_time, weight, i))
            
#         return ans