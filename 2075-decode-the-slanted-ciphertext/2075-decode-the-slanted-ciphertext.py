class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
            
        n = len(encodedText)
        cols = n // rows
        
        result = []
        
        # Read diagonals starting from each column in first row
        for start_col in range(cols):
            # For diagonal starting at column start_col, read until we hit matrix boundaries
            k = 0
            while True:
                # Calculate position in encoded text: row = k, col = start_col + k
                # encodedText position = row * cols + col
                pos = k * cols + (start_col + k)
                if pos >= n or (start_col + k) >= cols:
                    break
                result.append(encodedText[pos])
                k += 1
        
        # Join and remove trailing spaces
        return ''.join(result).rstrip()


# class Solution:
#     def decodeCiphertext(self, encodedText: str, rows: int) -> str:
#         if rows == 1:
#             return encodedText
            
#         n = len(encodedText)
#         cols = n // rows
        
#         # Create matrix and fill with encoded text row by row
#         matrix = [[' '] * cols for _ in range(rows)]
#         idx = 0
#         for r in range(rows):
#             for c in range(cols):
#                 if idx < n:
#                     matrix[r][c] = encodedText[idx]
#                     idx += 1
        
#         # Read the original text by following diagonals
#         result = []
#         # Start from each column in the first row
#         for start_col in range(cols):
#             r, c = 0, start_col
#             while r < rows and c < cols:
#                 result.append(matrix[r][c])
#                 r += 1
#                 c += 1
        
#         # Join the result and remove trailing spaces
#         original = ''.join(result)
#         return original.rstrip()