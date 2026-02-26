class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Convert string to list for easier manipulation
        # But instead of modifying, we'll process from right to left
        s_list = list(s)
        
        # Process until we have only one digit left
        while len(s_list) > 1:
            n = len(s_list)
            
            # If last digit is 0 (even) and no carry from previous operation
            if s_list[-1] == '0' and carry == 0:
                # Divide by 2 - remove last digit
                s_list.pop()
                steps += 1
            else:
                # We need to handle odd number or carry from previous operation
                if s_list[-1] == '1':
                    # Odd number, we add 1
                    carry = 1
                steps += 1
                
                # Process the carry from right to left
                i = n - 1
                while i >= 0 and carry:
                    if s_list[i] == '1':
                        s_list[i] = '0'
                        carry = 1
                    else:  # s_list[i] == '0'
                        s_list[i] = '1'
                        carry = 0
                    i -= 1
                
                # If we still have carry, we need to add a new digit at the beginning
                if carry:
                    s_list.insert(0, '1')
                    carry = 0
        
        return steps