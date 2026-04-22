# class Solution:
#     def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
#         result = []
        
#         for query in queries:
#             # Check if this query can match any dictionary word within 2 edits
#             for dict_word in dictionary:
#                 # Count the number of positions where characters differ
#                 diff_count = 0
#                 for i in range(len(query)):
#                     if query[i] != dict_word[i]:
#                         diff_count += 1
#                         # Early exit if we already exceed 2 edits
#                         if diff_count > 2:
#                             break
                
#                 # If within 2 edits, add to result and break
#                 if diff_count <= 2:
#                     result.append(query)
#                     break
        
#         return result


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        if not queries or not dictionary:
            return []
        
        word_length = len(queries[0])
        
        # Encode each dictionary word as a list of integers
        # Each position is encoded as 5 bits (since 2^5 = 32 > 26)
        # So each word becomes word_length * 5 bits
        dict_encoded = []
        
        for word in dictionary:
            encoded = 0
            for i, char in enumerate(word):
                # Each character takes 5 bits at position i*5
                encoded |= (ord(char) - ord('a')) << (i * 5)
            dict_encoded.append(encoded)
        
        result = []
        
        for query in queries:
            # Encode query word
            query_encoded = 0
            for i, char in enumerate(query):
                query_encoded |= (ord(char) - ord('a')) << (i * 5)
            
            # Check against each dictionary word
            for dict_encoded_word in dict_encoded:
                diff_count = 0
                temp = query_encoded ^ dict_encoded_word
                
                # Count how many positions differ (each 5-bit chunk)
                for i in range(word_length):
                    # Extract 5 bits at position i*5
                    if (temp >> (i * 5)) & 0x1F:  # 0x1F = 31 (5 bits all 1)
                        diff_count += 1
                        if diff_count > 2:
                            break
                
                if diff_count <= 2:
                    result.append(query)
                    break
        
        return result