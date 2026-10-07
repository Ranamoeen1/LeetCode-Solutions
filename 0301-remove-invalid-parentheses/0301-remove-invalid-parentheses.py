from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if isValid(current):
                result.append(current)
                found = True

            # If a valid string is found at this level, don't generate next level
            if found:
                continue

            # Generate all possible strings by removing one parenthesis
            for i in range(len(current)):
                if current[i] not in "()":
                    continue
                
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result