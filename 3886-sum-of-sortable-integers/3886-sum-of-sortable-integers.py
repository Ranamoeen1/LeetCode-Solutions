class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        
        # Find all divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        total_sum = 0
        
        for k in divisors:
            valid = True
            for i in range(0, n, k):
                block = nums[i:i+k]
                target = s[i:i+k]
                
                block_str = ''.join(f',{x}' for x in block)
                target_str = ''.join(f',{x}' for x in target)
                
                if target_str not in (block_str + block_str):
                    valid = False
                    break
            
            if valid:
                total_sum += k
                
        return total_sum