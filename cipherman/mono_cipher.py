
from .cipher import Cipher
from .cipher_helper import CipherHelper

class MonoCipher(Cipher):

    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)


    def _encrept(self, text: str, key) -> str:
        if not isinstance(key, str):
            raise TypeError("Expected a string")
        text = text.lower()
        key = CipherHelper.clean_text_key(key)
        cipher = ''

        for char in text:
            if char.isspace():
                cipher += ' '
                continue
            cipher += key[CipherHelper.char_to_position(char)]
        return cipher.upper()

    def _decrept(self, text: str, key) -> str:
        if not isinstance(key, str):
            raise TypeError("Expected a string")
        text = text.lower()
        key = CipherHelper.clean_text_key(key)
        plain = ''

        for char in text:
            if char.isspace():
                plain += ' '
                continue
            plain += CipherHelper.position_to_char(key.find(char))
        return plain.lower()


