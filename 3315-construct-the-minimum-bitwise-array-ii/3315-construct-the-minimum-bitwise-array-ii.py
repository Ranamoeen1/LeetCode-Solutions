class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            x = -1
            for r in range(num.bit_length() - 1, -1, -1):
                mask_r = 1 << r
                if num & mask_r:  
                    mask_below = (1 << r) - 1
                    if (num & mask_below) == mask_below:
                        candidate = num & ~mask_r
                        if candidate | (candidate + 1) == num:
                            x = candidate
                            break  
            result.append(x)
        
        return result