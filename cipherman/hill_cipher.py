import numpy as np
from math import sqrt
from sympy import Matrix

from .cipher import Cipher
from .cipher_helper import CipherHelper


class HillCipher(Cipher):
    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)

    def _encrept(self, text: str, key) -> str:
        key_matrix = np.array(CipherHelper.text_to_square_array(key))
        text_sliced = CipherHelper.slice_text(text, key_matrix.shape[0])
        cipher_text = ''
        for slice in text_sliced:
            text_matrix = np.array(CipherHelper.to_position_list(list(slice))) # what does reshape(1, -1) do here: it reshape the array to have 1 row and as many columns as needed, in this case it will be 1 row and 3 columns
            cipher_matrix = np.dot(text_matrix, key_matrix) % 26
            cipher_text += ''.join(CipherHelper.to_char_list(cipher_matrix.flatten().tolist())).upper()
        return cipher_text

    def _decrept(self, text: str, key) -> str:
        key_matrix = np.array(CipherHelper.text_to_square_array(key))
        key_matrix_inv = np.array(Matrix(key_matrix).inv_mod(26))  # Modular inverse using sympy
        text_sliced = CipherHelper.slice_text(text, key_matrix.shape[0])
        cipher_text = ''
        for slice in text_sliced:
            text_matrix = np.array(CipherHelper.to_position_list(list(slice))) # what does reshape(1, -1) do here: it reshape the array to have 1 row and as many columns as needed, in this case it will be 1 row and 3 columns
            cipher_matrix = np.dot(text_matrix, key_matrix_inv) % 26
            cipher_text += ''.join(CipherHelper.to_char_list(cipher_matrix.flatten().tolist())).lower()
        return cipher_text

    

    if __name__ == "__main__":
        pass