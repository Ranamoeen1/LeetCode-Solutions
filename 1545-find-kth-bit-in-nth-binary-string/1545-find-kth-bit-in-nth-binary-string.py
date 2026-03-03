class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        length = (1 << n) - 1  # 2^n - 1
        mid = (length // 2) + 1  # Middle position (1-indexed)
        
        if k == mid:
            return "1"
        elif k < mid:
            # k is in the left half
            return self.findKthBit(n - 1, k)
        else:
       
            corresponding_bit = self.findKthBit(n - 1, length - k + 1)
            return "1" if corresponding_bit == "0" else "0"