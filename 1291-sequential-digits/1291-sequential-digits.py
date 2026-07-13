class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []
        
        # Determine the minimum and maximum possible lengths of the numbers
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate through all possible lengths
        for length in range(min_len, max_len + 1):
            # Slide a window of 'length' across the sample string
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    result.append(num)
                    
        return result