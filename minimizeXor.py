class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        num2_set_bits = bin(num2).count('1')
        
        # Initialize x to 0
        x = 0
        
        # Fill the bits of x in a way that minimizes x XOR num1
        for i in range(31, -1, -1):  # Iterate from the most significant bit to the least significant bit
            if num2_set_bits > 0 and (num1 & (1 << i)) != 0:
                x |= (1 << i)  # Set the i-th bit of x
                num2_set_bits -= 1
        
        # If there are still bits left to set in x, set them from the least significant bit upwards
        for i in range(32):
            if num2_set_bits == 0:
                break
            if (x & (1 << i)) == 0:
                x |= (1 << i)  # Set the i-th bit of x
                num2_set_bits -= 1
        
        return x
