from .cipher import Cipher
from .cipher_helper import CipherHelper


class VigenereCipher(Cipher):
    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)

    def _encrept(self, text: str, key) -> str:
        key = key.replace(' ', '')
        text = text.replace(' ', '')
        cipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                shift = CipherHelper.char_to_position(key[i % len(key)]) # very smart way to get the shift for each character in the text, it uses the index of the text and the length of the key to get the corresponding character in the key, and then it converts that character to a position (0-25) to use as a shift
                cipher_char = CipherHelper.position_to_char((CipherHelper.char_to_position(text[i]) + shift) % 26)
                cipher_text += cipher_char.upper()
            else:
                cipher_text += text[i]
        return cipher_text

    def _decrept(self, text: str, key) -> str:
        key = key.replace(' ', '')
        plain_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                shift = CipherHelper.char_to_position(key[i % len(key)])
                plain_char = CipherHelper.position_to_char((CipherHelper.char_to_position(text[i]) - shift) % 26)
                plain_text += plain_char.lower()
            else:
                plain_text += text[i]
        return plain_text

    if __name__ == "__main__":
        pass