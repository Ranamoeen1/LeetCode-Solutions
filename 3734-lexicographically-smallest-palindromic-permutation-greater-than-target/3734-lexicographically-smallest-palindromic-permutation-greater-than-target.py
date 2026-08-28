from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        counts = Counter(s)
        
        # Check if a palindromic permutation is possible
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Available counts for the first half
        half_counts = {char: count // 2 for char, count in counts.items() if count // 2 > 0}
        
        def build_full_palindrome(first_half: str) -> str:
            """Constructs the full palindrome from the first half."""
            if n % 2 == 0:
                return first_half + first_half[::-1]
            else:
                return first_half + mid_char + first_half[::-1]

        # Case 1: Try matching the entire first half of target
        can_match_prefix = True
        curr_half = []
        temp_counts = half_counts.copy()
        
        for i in range(m):
            t_char = target[i]
            if temp_counts.get(t_char, 0) > 0:
                curr_half.append(t_char)
                temp_counts[t_char] -= 1
            else:
                can_match_prefix = False
                break
        
        if can_match_prefix:
            first_half_str = "".join(curr_half)
            full_pal = build_full_palindrome(first_half_str)
            if full_pal > target:
                return full_pal

        # Case 2: Try diverging at index i (from m-1 down to 0)
        for i in range(m - 1, -1, -1):
            prefix = target[:i]
            
            # Count characters used in prefix target[:i]
            prefix_counts = Counter(prefix)
            
            # Verify if target[:i] can be formed by available half_counts
            possible = True
            rem_counts = half_counts.copy()
            for char, count in prefix_counts.items():
                if rem_counts.get(char, 0) < count:
                    possible = False
                    break
                rem_counts[char] -= count
            
            if not possible:
                continue
            
            # Try placing a character strictly greater than target[i] at position i
            target_char = target[i]
            for next_char in sorted(rem_counts.keys()):
                if next_char > target_char and rem_counts[next_char] > 0:
                    # Form the rest of the half in smallest lexicographical order
                    rem_counts[next_char] -= 1
                    tail = []
                    for c in sorted(rem_counts.keys()):
                        tail.extend([c] * rem_counts[c])
                    
                    first_half = prefix + next_char + "".join(tail)
                    return build_full_palindrome(first_half)

        return ""