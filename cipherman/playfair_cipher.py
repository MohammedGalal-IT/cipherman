
from .cipher import Cipher
from .cipher_helper import CipherHelper


class PlayfairCipher(Cipher):

    def __init__(self, text: str='', key: str='', operation: str='', url: str=''):
        super().__init__(text, key, operation, url)


    def _encrept(self, text: str, key) -> str:
        digrams = self._create_digram(text)
        array = self._create_array(key)
        cipher = ''

        for digram in digrams:
            index1 = array.index(digram[0])
            index2 = array.index(digram[1])

            i1 = self._get_row_index(index1)
            j1 = self._get_column_index(index1)

            i2 = self._get_row_index(index2)
            j2 = self._get_column_index(index2)

            if i1 == i2:
                j1 = (j1 + 1)%5
                j2 = (j2 + 1)%5

            elif j1 == j2:
                i1 = (i1 + 1)%5
                i2 = (i2 + 1)%5

            else:
                temp = j1
                j1 = j2
                j2 = temp

            cipher += array[i1 * 5 + j1]
            cipher += array[i2 * 5 + j2]

        return cipher


    def _decrept(self, text: str, key) -> str:
        return self._encrept(text, key).lower()


    def _digram(self, text: str) -> str:
        if len(text) == 0:
            return ''
        if len(text) == 1:
            return text + 'x'
        digram = text[:2]
        rest = text[2:]
        if digram.count(digram[0]) > 1:
            digram = digram[0] + 'x'
            rest = digram[0] + rest

        return digram + self._digram(rest)


    def _create_digram(self, text: str) -> list:
        text = text.replace(' ', '').upper().strip()
        digram_text = self._digram(text).replace('i', 'j')
        digram_list = []

        for i in range(len(digram_text)):
            if i%2 != 0:
                continue
            digram_list.append(digram_text[i:i+2])

        return digram_list


    def _create_array(self, key):
        alphabets = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
        key = CipherHelper.clean_text_key(key).upper()
        for k in key:
            alphabets = alphabets.replace(k, '')

        return key + alphabets


    def _get_row_index(self, index: int) -> int:
        return index // 5


    def _get_column_index(self, index: int) -> int:
        return index % 5





