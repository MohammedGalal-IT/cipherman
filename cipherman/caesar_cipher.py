
from .cipher import Cipher
from .cipher_helper import CipherHelper


class CaesarCipher(Cipher):

    def __init__(self, text: str='', key: int=-999, operation: str='', url: str=''):
        super().__init__(text, key, operation, url)


    def _encrept(self, text: str, key) -> str:
        if not isinstance(key, int):
            raise TypeError("Expected (int) for key (Caesar cipher)")
        text = text.lower()
        cipher = ''

        for char in text:
            if char.isspace():
                cipher += ' '
                continue
            cipher += CipherHelper.position_to_char((CipherHelper.char_to_position(char) + key)%26)
        return cipher.upper()

    def _decrept(self, text: str, key) -> str:
        if not isinstance(key, int):
            raise TypeError("Expected (int) for key (Caesar cipher)")
        text = text.lower()
        cipher = ''

        for char in text:
            if char.isspace():
                cipher += ' '
                continue
            cipher += CipherHelper.position_to_char((CipherHelper.char_to_position(char) - key)%26)
        return cipher.lower()
