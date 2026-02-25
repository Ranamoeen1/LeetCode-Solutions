class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def compare(a, b):
            # Count bits for both numbers
            bits_a = bin(a).count('1')
            bits_b = bin(b).count('1')
            
            # Compare by bit count first
            if bits_a != bits_b:
                return bits_a - bits_b
            # If bit counts are equal, compare by value
            return a - b
        
        # Sort using custom comparator
        return sorted(arr, key=functools.cmp_to_key(compare))

# class Solution:
#     def sortByBits(self, arr: List[int]) -> List[int]:


#         return sorted(arr, key=lambda x: (bin(x).count('1'), x))