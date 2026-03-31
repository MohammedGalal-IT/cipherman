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
    
    
    

if __name__ == "__main__":
    print(CipherHelper.text_to_square_array("123456789"))