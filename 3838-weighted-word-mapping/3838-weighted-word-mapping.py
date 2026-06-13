class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # Map ASCII values directly to their weights.
        # ASCII 'a' is 97. We create a 123-element list so 'z' (122) fits perfectly.
        ascii_weights = [0] * 123
        for i, w in enumerate(weights):
            ascii_weights[97 + i] = w
            
        # Precompute the reverse alphabetical character map for all possible sums.
        # Since weight_sum can be larger than 256, we can handle a reasonable range.
        # Max weight of a word is 10 letters * 100 max weight = 1000.
        # To be safe and fast, we precompute a lookup array for up to 1001 possible weights.
        ord_z = 122
        byte_map = bytes((ord_z - (i % 26)) for i in range(1005))
        
        result = []
        for word in words:
            # 1. word.encode('ascii') turns "abcd" into [97, 98, 99, 100] instantly.
            # 2. Sum the weights by looking up those ASCII integer values directly.
            weight_sum = sum(ascii_weights[b] for b in word.encode('ascii'))
            
            # 3. Grab the final character byte instantly from our precomputed map.
            result.append(byte_map[weight_sum])
            
        # Convert the accumulated bytes back to a string all at once.
        return bytes(result).decode('ascii')



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
        

# class Solution:
#     def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
#         # Precompute a direct ASCII lookup array for weights.
#         # ASCII 'a' is 97, so we create an array of size 123 to cover up to 'z' (122).
#         ascii_weights = [0] * 123
#         for i in range(26):
#             ascii_weights[97 + i] = weights[i]
            
#         # Cache the ASCII value of 'z' for faster reverse mapping math
#         ord_z = 122 
#         result = []
        
#         for word in words:
#             # Directly look up the integer weight using byte-values of characters
#             word_weight = sum(ascii_weights[ord(char)] for char in word)
            
#             # Map remainder directly using the cached 'z' integer value
#             result.append(chr(ord_z - (word_weight % 26)))
            
#         return "".join(result)