class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Track the latest position of each character
        # Initialize with -1 to indicate they haven't been seen yet
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for right, char in enumerate(s):
            # Update the latest index for the current character
            last_seen[char] = right
            
            # The number of valid substrings ending at 'right' is determined by 
            # the minimum index among the last seen positions of 'a', 'b', and 'c'.
            # Adding 1 because indices are 0-based.
            count += min(last_seen['a'], last_seen['b'], last_seen['c']) + 1
            
        return count