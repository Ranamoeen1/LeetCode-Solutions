class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         n = ((n >> 16) & 0xffff) | ((n & 0xffff) << 16)
#         n = ((n >> 8) & 0xff00ff) | ((n & 0xff00ff) << 8)
#         n = ((n >> 4) & 0xf0f0f0f) | ((n & 0xf0f0f0f) << 4)
#         n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2)
#         n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1)
#         return n