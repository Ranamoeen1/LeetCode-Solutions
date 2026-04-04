class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
            
        n = len(encodedText)
        cols = n // rows
        
        # Create matrix and fill with encoded text row by row
        matrix = [[' '] * cols for _ in range(rows)]
        idx = 0
        for r in range(rows):
            for c in range(cols):
                if idx < n:
                    matrix[r][c] = encodedText[idx]
                    idx += 1
        
        # Read the original text by following diagonals
        result = []
        # Start from each column in the first row
        for start_col in range(cols):
            r, c = 0, start_col
            while r < rows and c < cols:
                result.append(matrix[r][c])
                r += 1
                c += 1
        
        # Join the result and remove trailing spaces
        original = ''.join(result)
        return original.rstrip()