from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Try finding the longest matching prefix target[:i]
        for i in range(n - 1, -1, -1):
            # Check if target[:i] can be formed using s
            prefix_counts = Counter(target[:i])
            
            # Verify if target[:i] is a valid subset of s
            if any(prefix_counts[char] > total_counts[char] for char in prefix_counts):
                continue
                
            # Available characters after matching target[:i]
            remaining_counts = total_counts - prefix_counts
            
            # Find the smallest character > target[i] available
            target_char = target[i]
            chosen_char = None
            
            for char in sorted(remaining_counts.keys()):
                if char > target_char and remaining_counts[char] > 0:
                    chosen_char = char
                    break
            
            # If a valid character exists for index i
            if chosen_char:
                remaining_counts[chosen_char] -= 1
                
                # Build the remainder of the string in sorted order
                tail = []
                for char in sorted(remaining_counts.keys()):
                    tail.append(char * remaining_counts[char])
                
                return target[:i] + chosen_char + "".join(tail)
                
        return ""