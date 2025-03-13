import sys

def unscramble(scrambled_list):
    # Make a deep copy to avoid modifying the original
    result = [item.copy() for item in scrambled_list]
    
    # Reconstruct the original list
    # We need to work backward from the end of the scrambled list
    original_length = len(result)
    
    # Calculate how many operations were performed
    operations_count = original_length - 2
    
    # For each operation, we need to:
    # 1. Remove the appended slice from the current i-1 element
    # 2. Extract the element that was added to i-2 and reinsert it at i-1
    
    for i in range(operations_count, 0, -1):
        # Current position we're working with
        pos = original_length - i
        
        # Remove the appended slice (we ignore this since it's just debugging info)
        result[pos].pop()
        
        # The element at pos-1 has an extra value added to it
        # We need to extract that value and reinsert it at pos
        
        # The value to extract should be the first element from result[pos-1]
        extracted_value = result[pos-1].pop(0)
        
        # Insert it back at position pos
        result.insert(pos, [extracted_value])
    
    return result

def get_original_flag(scrambled_flag):
    unscrambled = unscramble(scrambled_flag)
    
    # Convert hex strings back to characters
    flag = ""
    for hex_char in unscrambled:
        # Extract the hex string from the list
        hex_str = hex_char[0]
        # Convert hex to integer and then to character
        flag += chr(int(hex_str, 16))
    
    return flag

def main():
    # Example usage with the scrambled flag
    scrambled_flag = [['0x61', '0x20'], ['0x66', '0x6c', '0x61', '0x67', '0x20', '0x61'], ['0x68', '0x61', '0x68', '0x61']]
    
    original_flag = get_original_flag(scrambled_flag)
    print("Original flag:", original_flag)

if __name__ == '__main__':
    main()