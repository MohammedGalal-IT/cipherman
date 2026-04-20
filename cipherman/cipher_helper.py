from math import sqrt

class CipherHelper():

    def char_to_position(char: str) -> int:
        char = char[0].lower()
        return ord(char) - 97


    def position_to_char(position: int) -> str:
        char = chr(position + 97)
        return char
    

    def to_position_list(list: list) -> list:
        return [CipherHelper.char_to_position(char) for char in list]
    

    def to_char_list(list: list) -> list:
        return [CipherHelper.position_to_char(position) for position in list]


    def text_to_square_array(text: str) -> list: # if input is "17 17 5 21 18 21 2 2 19" it will return [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
        """Convert a string into a square array (list of lists)"""
        text_list = text.strip().split()
        for i in text_list:
            if not i.isdigit():
                raise ValueError("Key must be a string of numbers space separated")
        length = len(text_list)
        size = int(sqrt(length))
        if size * size != length:
            raise ValueError("Text length must be a perfect square.")
        
        arr = [list(text_list[i:i+size]) for i in range(0, length, size)]
        for row in arr:
            for i in range(len(row)):
                row[i] = int(row[i])
        
        return arr


    def clean_text_key(text_key: str) -> str:
        key = text_key.replace(' ', '').lower()
        key = "".join(dict.fromkeys(key)) #remove duplications
        return key
    

    def slice_text(text: str, length: int, space: bool=False) -> list:
        if not space:
            text = text.replace(' ', '').strip()
        text = text.lower()
        sliced_text = [text[i:i+length] for i in range(0, len(text), length)]

        if sliced_text[-1] != '' and len(sliced_text[-1]) < length:
            sliced_text[-1] = sliced_text[-1].ljust(length, 'x') # give an example when a the last slice is '': 
        
        return sliced_text
    

    def prepare_64bit_blocks(text: str) -> list:
        """
        Converts input text into 64-bit blocks with proper padding.
        
        Args:
            text (str): Input text string to be processed
            
        Returns:
            list: List of 64-bit blocks as strings of '0' and '1' characters
        """
        # Convert text to binary string (8 bits per character)
        binary_string = ''.join(format(ord(char), '08b') for char in text)
        
        # Calculate padding needed
        padding_needed = (64 - (len(binary_string) % 64)) % 64
        
        # If no padding needed, but text is empty, add full block of padding
        if padding_needed == 0 and len(binary_string) == 0:
            padding_needed = 64
        
        # Add padding using 'x' character (ASCII 120, binary: 01111000)
        padding_char = 'x'
        padding_bits = ''.join(format(ord(padding_char), '08b') for _ in range(padding_needed // 8))
        
        # Add the padding bits
        binary_string += padding_bits
        
        # Split into 64-bit blocks
        blocks = [binary_string[i:i+64] for i in range(0, len(binary_string), 64)]
        
        return blocks
    

    def reconstruct_text_from_64bit_blocks(blocks: list) -> str:
        """
        Reconstructs original text from 64-bit binary blocks by removing padding.
        
        Args:
            blocks (list): List of 64-bit binary strings (each exactly 64 chars of '0'/'1')
            
        Returns:
            str: Original text with 'x' padding removed
            
        Raises:
            ValueError: If blocks contain invalid binary strings or incorrect block sizes
        """
        # Validate input
        if not blocks:
            return ""
        
        for i, block in enumerate(blocks):
            if len(block) != 64:
                raise ValueError(f"Block {i} is {len(block)} bits, expected 64 bits")
            if not all(bit in '01' for bit in block):
                raise ValueError(f"Block {i} contains non-binary characters")
        
        # Join all blocks into single binary string
        full_binary = ''.join(blocks)
        
        # Convert binary to text (8 bits per character)
        reconstructed_text = ''
        for i in range(0, len(full_binary), 8):
            byte = full_binary[i:i+8]
            if len(byte) == 8:  # Ensure we have complete byte
                char_code = int(byte, 2)
                reconstructed_text += chr(char_code)
        
        # Remove trailing 'x' padding characters
        # Note: We use rstrip('x') to remove all trailing 'x' characters
        original_text = reconstructed_text.rstrip('x')
        
        return original_text


    def hex_to_bin(hex_string: str) -> str:
        """
        Ultra-fast hex to binary conversion using lookup table.
        Perfect for DES encryption where speed matters.
        
        Args:
            hex_string (str): Hexadecimal string
            
        Returns:
            str: Binary string
        """

        HEX_TO_BIN_TABLE = {
            '0': '0000', '1': '0001', '2': '0010', '3': '0011',
            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
            'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
            }
        hex_string = hex_string.lower().replace('0x', '')
        return ''.join(HEX_TO_BIN_TABLE[c] for c in hex_string)
    

if __name__ == "__main__":
    # text = "Hello World!"
    # blocks = CipherHelper.prepare_64bit_blocks(text)
    # print("64-bit blocks:", blocks)
    # reconstructed_text = CipherHelper.reconstruct_text_from_64bit_blocks(blocks)
    # print("Reconstructed text:", reconstructed_text)
    hex_string = "133457799BBCDFF1"
    binary_string = CipherHelper.hex_to_bin(hex_string)
    print(f"Hex: {hex_string} -> Binary: {binary_string}")
