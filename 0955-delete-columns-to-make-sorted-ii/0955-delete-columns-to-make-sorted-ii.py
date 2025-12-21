class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        sorted_pairs = [False] * (n - 1)
        deletions = 0
        for j in range(m):
            column_valid = True
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][j] > strs[i+1][j]:
                    column_valid = False
                    break
            if not column_valid:
                deletions += 1
            else:
                for i in range(n - 1):
                    if not sorted_pairs[i] and strs[i][j] < strs[i+1][j]:
                        sorted_pairs[i] = True
        return deletions