class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        for query in queries:
            # Check if this query can match any dictionary word within 2 edits
            for dict_word in dictionary:
                # Count the number of positions where characters differ
                diff_count = 0
                for i in range(len(query)):
                    if query[i] != dict_word[i]:
                        diff_count += 1
                        # Early exit if we already exceed 2 edits
                        if diff_count > 2:
                            break
                
                # If within 2 edits, add to result and break
                if diff_count <= 2:
                    result.append(query)
                    break
        
        return result