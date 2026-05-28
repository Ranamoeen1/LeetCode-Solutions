class TrieNode:
    def __init__(self):
        self.children = {}
        # Stores the index of the optimal word sharing this suffix path
        self.best_index = -1 

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        
        # 1. Find the global default index (shortest length, earliest occurrence)
        # This will be used at the root if a query shares no common suffix at all.
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
                
        root.best_index = global_best_idx
        
        # Helper function to determine if a new index is a better match
        def get_better_index(curr_idx, new_idx):
            if curr_idx == -1:
                return new_idx
            len_curr = len(wordsContainer[curr_idx])
            len_new = len(wordsContainer[new_idx])
            if len_new < len_curr:
                return new_idx
            elif len_new == len_curr:
                return min(curr_idx, new_idx)
            return curr_idx

        # 2. Build the Trie by inserting reversed strings from wordsContainer
        for idx, word in enumerate(wordsContainer):
            curr = root
            # Traverse from back to front
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # Precompute and update the best index at this specific node level
                curr.best_index = get_better_index(curr.best_index, idx)
                
        # 3. Process each query in wordsQuery
        ans = []
        for query in wordsQuery:
            curr = root
            # Walk down the Trie using the reversed query characters
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break # Break early if the common suffix path ends
            ans.append(curr.best_index)
            
        return ans