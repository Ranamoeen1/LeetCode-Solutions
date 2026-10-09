class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_rights = 0
        
        for char in s:
            if char == '(':
                # Each '(' needs two ')'
                needed_rights += 2
                
                # If needed_rights is odd, it means we had an unpaired single ')'
                # before this '('. We must insert one ')' to complete that pair.
                if needed_rights % 2 == 1:
                    insertions += 1
                    needed_rights -= 1
            else:  # char == ')'
                needed_rights -= 1
                
                # If we encounter a ')' without a preceding '(', we need to insert a '('
                if needed_rights < 0:
                    insertions += 1
                    needed_rights += 2  # The new '(' adds 2 to needed_rights, but we consume 1 for the current ')'
                    
        return insertions + needed_rights