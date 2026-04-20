from .cipher import Cipher
from .cipher_helper import CipherHelper

class DESCipher(Cipher):

    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)
    
    def _encrept(self, text: str, key: str) -> str:
        pass

    def _decrept(self, text: str, key: str) -> str:
        pass

    def permutation_choice_1(self, key: str) -> str:
        PC1_TABLE = [
            57, 49, 41, 33, 25, 17,  9,
            1, 58, 50, 42, 34, 26, 18,
            10,  2, 59, 51, 43, 35, 27,
            19, 11,  3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14,  6, 61, 53, 45, 37, 29,
            21, 13,  5, 28, 20, 12,  4
            ]
        key = key.replace(' ', '')
        if len(key) != 64:
            raise ValueError("Key must be 64 bits long.")
        
        new_key = ''.join(key[i-1] for i in PC1_TABLE)
        return new_key
    

        
