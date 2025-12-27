class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ready_rooms = [i for i in range(n)] 
        busy_rooms = [] 
        count = [0] * n
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heappop(busy_rooms)
                heappush(ready_rooms, room_idx)
            if ready_rooms:
                room_idx = heappop(ready_rooms)
                heappush(busy_rooms, (end, room_idx))
            else:
                earliest_end, room_idx = heappop(busy_rooms)
                new_end = earliest_end + (end - start)
                heappush(busy_rooms, (new_end, room_idx))
            count[room_idx] += 1
        max_meetings = 0
        best_room = 0
        for i in range(n):
            if count[i] > max_meetings:
                max_meetings = count[i]
                best_room = i
        return best_room

