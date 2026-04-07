from .cipher import Cipher
from .cipher_helper import CipherHelper

class VigenereAutokeyCipher(Cipher):
    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)

    def __process_key(self, key: str, text: str) -> str:
        key = key.replace(' ', '')
        processed_key = key + text
        return processed_key

    def _encrept(self, text: str, key) -> str:
        text = text.replace(' ', '')
        key = self.__process_key(key, text)
        cipher_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                shift = CipherHelper.char_to_position(key[i % len(key)]) # very smart way to get the shift for each character in the text, it uses the index of the text and the length of the key to get the corresponding character in the key, and then it converts that character to a position (0-25) to use as a shift
                cipher_char = CipherHelper.position_to_char((CipherHelper.char_to_position(text[i]) + shift) % 26)
                cipher_text += cipher_char.upper()
                key += text[i] # autokey part, it adds the current character of the text to the key after using it for encryption
            else:
                cipher_text += text[i]
        return cipher_text + "\n\n Key used for encryption: " + key # the key used for encryption is the original key plus the text itself, but we only need to show the part of the key that was used for encryption which is the same length as the text

    def _decrept(self, text: str, key) -> str:
        text = text.replace(' ', '')
        plain_text = ''
        for i in range(len(text)):
            if text[i].isalpha():
                shift = CipherHelper.char_to_position(key[i % len(key)])
                plain_char = CipherHelper.position_to_char((CipherHelper.char_to_position(text[i]) - shift) % 26)
                plain_text += plain_char.lower()
                key += plain_char # autokey part, it adds the current decrypted character to the key after using it for decryption
            else:
                plain_text += text[i]
        return plain_text


    if __name__ == "__main__":
        pass