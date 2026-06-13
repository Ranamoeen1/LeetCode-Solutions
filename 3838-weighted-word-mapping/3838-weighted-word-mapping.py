class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # 1. Calculate the total weight of the word
            word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # 2. Get the remainder modulo 26
            remainder = word_weight % 26
            
            # 3. Map to reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('z') - remainder)
            
            result.append(mapped_char)
            
        # 4. Return the final concatenated string
        return "".join(result)
        
