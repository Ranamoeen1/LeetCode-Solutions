# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp = [0] * (n+1)   
#         dp[1] = 1
#         dp[2] = 2

#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        (n-1) 
        two variables  one, two
        keep on updating then 
        return one
        """
        one=1
        two=1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
        