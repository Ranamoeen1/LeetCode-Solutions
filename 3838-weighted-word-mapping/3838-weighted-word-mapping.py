# class Solution:
#     def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
#         result = []
        
#         for word in words:
#             # 1. Calculate the total weight of the word
#             word_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
#             # 2. Get the remainder modulo 26
#             remainder = word_weight % 26
            
#             # 3. Map to reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
#             mapped_char = chr(ord('z') - remainder)
            
#             result.append(mapped_char)
            
#         # 4. Return the final concatenated string
#         return "".join(result)
        

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Precompute a direct ASCII lookup array for weights.
        # ASCII 'a' is 97, so we create an array of size 123 to cover up to 'z' (122).
        ascii_weights = [0] * 123
        for i in range(26):
            ascii_weights[97 + i] = weights[i]
            
        # Cache the ASCII value of 'z' for faster reverse mapping math
        ord_z = 122 
        result = []
        
        for word in words:
            # Directly look up the integer weight using byte-values of characters
            word_weight = sum(ascii_weights[ord(char)] for char in word)
            
            # Map remainder directly using the cached 'z' integer value
            result.append(chr(ord_z - (word_weight % 26)))
            
        return "".join(result)