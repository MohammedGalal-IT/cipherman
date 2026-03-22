

class CipherHelper():

    def char_to_position(char: str) -> int:
        char = char[0].lower()
        return ord(char) - 97

    def position_to_char(position: int) -> str:
        char = chr(position + 97)
        return char

    def clean_text_key(text_key: str) -> str:
        key = text_key.replace(' ', '').lower()
        key = "".join(dict.fromkeys(key)) #remove duplications
        return key
