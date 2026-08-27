from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Track frequency of prefix target[0...i-1]
        prefix_counts = Counter()
        
        # Try to match a prefix of length i (from n-1 down to 0)
        # where the (i)-th character is strictly greater than target[i]
        for i in range(n):
            prefix_counts[target[i]] += 1
            
        for i in range(n - 1, -1, -1):
            # target[i] was included in prefix_counts, remove it as position i will differ
            prefix_counts[target[i]] -= 1
            if prefix_counts[target[i]] == 0:
                del prefix_counts[target[i]]
                
            # Check if prefix target[0...i-1] is valid (can be formed by characters in s)
            if any(prefix_counts[c] > total_counts[c] for c in prefix_counts):
                continue
                
            # Calculate remaining available characters after forming target[0...i-1]
            rem_counts = total_counts - prefix_counts
            
            # Find the smallest character > target[i]
            target_char = target[i]
            candidate_char = None
            for ch in sorted(rem_counts.keys()):
                if ch > target_char:
                    candidate_char = ch
                    break
                    
            if candidate_char is not None:
                # Construct the result:
                # 1. Prefix target[0...i-1]
                # 2. candidate_char at position i
                # 3. Remaining characters sorted in ascending order
                rem_counts[candidate_char] -= 1
                suffix = []
                for ch in sorted(rem_counts.keys()):
                    suffix.append(ch * rem_counts[ch])
                    
                return target[:i] + candidate_char + "".join(suffix)
                
        return ""




# from collections import Counter

# class Solution:
#     def lexGreaterPermutation(self, s: str, target: str) -> str:
#         n = len(s)
#         total_counts = Counter(s)
        
#         # Try finding the longest matching prefix target[:i]
#         for i in range(n - 1, -1, -1):
#             # Check if target[:i] can be formed using s
#             prefix_counts = Counter(target[:i])
            
#             # Verify if target[:i] is a valid subset of s
#             if any(prefix_counts[char] > total_counts[char] for char in prefix_counts):
#                 continue
                
#             # Available characters after matching target[:i]
#             remaining_counts = total_counts - prefix_counts
            
#             # Find the smallest character > target[i] available
#             target_char = target[i]
#             chosen_char = None
            
#             for char in sorted(remaining_counts.keys()):
#                 if char > target_char and remaining_counts[char] > 0:
#                     chosen_char = char
#                     break
            
#             # If a valid character exists for index i
#             if chosen_char:
#                 remaining_counts[chosen_char] -= 1
                
#                 # Build the remainder of the string in sorted order
#                 tail = []
#                 for char in sorted(remaining_counts.keys()):
#                     tail.append(char * remaining_counts[char])
                
#                 return target[:i] + chosen_char + "".join(tail)
                
#         return ""