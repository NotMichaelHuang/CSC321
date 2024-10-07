# Function to flip a specific bit in a binary string
def flip_bit(binary_string, index):
    bit_list = list(binary_string)
    # Flip the bit at the given index (0 to 1 or 1 to 0)
    bit_list[index] = '1' if bit_list[index] == '0' else '0'
    return ''.join(bit_list)

# Define a base string and make it a binary string representation
base_string = "hello"  # You can use any string here
# Convert to binary representation
base_binary = ''.join(format(ord(char), '08b') for char in base_string)

# Flip a single bit (e.g., the first bit)
flipped_binary = flip_bit(base_binary, 0)

# Convert back to characters
original_string = ''.join(chr(int(base_binary[i:i+8], 2)) for i in range(0, len(base_binary), 8))
flipped_string = ''.join(chr(int(flipped_binary[i:i+8], 2)) for i in range(0, len(flipped_binary), 8))

# Print the two strings with Hamming distance of 1
print("Original String:", original_string)
print("Flipped String:", flipped_string)
