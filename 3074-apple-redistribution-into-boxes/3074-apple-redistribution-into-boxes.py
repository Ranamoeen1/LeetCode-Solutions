class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        current_capacity = 0
        boxes_needed = 0
        
        for cap in capacity:
            if current_capacity >= total_apples:
                break
            current_capacity += cap
            boxes_needed += 1
            
        return boxes_needed
