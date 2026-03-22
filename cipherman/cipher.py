from abc import ABC, abstractmethod

from .utils import clear_screen


class Cipher(ABC):

    def __init__(self, text: str='', key=None, operation: str='', url: str=''):
        self.__text = text
        self.__key = key
        self.__operation = operation
        self.__url = url
        self.__encrepted_text = ''
        self.__decrepted_text = ''

        if operation == 'en':
            self.encrept()
        elif operation == 'de':
            self.decrept()
        else:
            self.__operation = 'No Operation Set Yet'


    def encrept(self, text=''):
        """
        the method uses self._encrept() to encrept the text and store it in self.__encrepted_text, also it change self.__operation to 'en'
        """
        if text:
            self.__text = text
        self.__encrepted_text = self._encrept(self.__text, self.__key)
        self.__operation = 'en'


    def decrept(self, text=''):
        """
        the method uses self._encrept() to encrept the text and store it in self.__encrepted_text, also it change self.__operation to 'en'
        """
        if text:
            self.__text = text
        self.__decrepted_text = self._decrept(self.__text, self.__key)
        self.__operation = 'de'


    @abstractmethod
    def _encrept(self, text: str, key) -> str:
        pass

    @abstractmethod
    def _decrept(self, text: str, key) -> str:
        pass


    def encrept_file(self, url='') -> str:
        """
        Encrept a file text and store it in a the same directory as 'old-url_encrepted.txt (or other extention)
        the method copy file content to self.__text and the call self.encrept(), after that self.__text and self.__encrepted_text are clean up
        """
        if url:
            self.__url = url
        try:
            with open(self.__url) as f:
                self.__text = f.read()
                self.encrept()

            temp = self.__url.split('.')
            new_url = temp[0] + '_encrepted.' + temp[1]

            with open(new_url, 'w') as new_f:
                new_f.write(self.__encrepted_text)
                self.__text = ''
                self.__encrepted_text = ''
            return new_url

        except FileNotFoundError as err:
            print(err)
        except Exception as err:
            print(err)
            print("erro at Cipher class")


    def decrept_file(self, url='') -> str:
        """
        decrept a file text and store it in a the same directory as 'old-url_decrepted.txt (or other extention)
        the method copy file content to self.__text and the call self.decrept(), after that self.__text and self.__decrepted_text are clean up
        """
        if url:
            self.__url = url
        try:
            with open(self.__url) as f:
                self.__text = f.read()
                self.decrept()

            temp = self.__url.split('.')
            new_url = temp[0] + '_decrepted.' + temp[1]

            with open(new_url, 'w') as new_f:
                new_f.write(self.__decrepted_text)
                self.__text = ''
                self.__decrepted_text = ''
            return new_url

        except FileNotFoundError as err:
            print(err)
        except Exception as err:
            print(err)
            print("Error at Cipher class")


    def get_encrepted_text(self):
        return self.__encrepted_text


    def get_decrepted_text(self):
        return self.__decrepted_text


    def show_status(self):
        return f'\n{"-"*25}\nstatus\n{"-"*25}\n\n- Last Operation: "{self.last_operation()}"\n\n- Last Entered Text: {self.__text}\n\n- Encrepted text Buffer: {self.__encrepted_text}\n\n- Decrepted Text Buffer: {self.__decrepted_text}\n\n- Url Buffer: {self.__url}\n\n{"-"*25}\n'


    def set_text(self, text: str) -> None:
        self.__text = text


    def get_text(self) -> str:
        return self.__text


    def set_key(self, key):
        self.__key = key


    def get_key(self):
        return self.__key


    def clear(self):
        self.__text = ''
        self.__key = None
        self.__encrepted_text = ''
        self.__decrepted_text = ''
        self.__url = ''


    def last_operation(self):
        if self.__operation == 'en':
            return "Encreption"
        elif self.__operation == 'de':
            return "Decreption"
        else:
            return self.__operation


    def cmd_start(self, target: str, operation: str, key_type=str) -> None:
        """
        a method that runs as a CLI app

        - target: str ,has only two values 'text', 'file' which represent the input and output

        - operation: str ,has also two values 'en' for encryption and 'de' for decryption
        """
        try:
            if target not in ["text", "file"]:
                raise ValueError("Expected 'text' or 'file' for the first argument (target) at cmd_start() method")
            if operation not in ["en", "de"]:
                raise ValueError("Expected 'en' or 'de' for the second argument (operation) at cmd_start() method")
            if target == "text":
                print("\n", "-"*20)
                self.__text = input("Enter Text >> ")
                key = input(f"\nEnter Key({key_type.__name__}) >> ")
                self.__key = int(key) if key_type == int else key
                text = ''
                if operation == "en":
                    self.encrept()
                    text = f"Encrypted Text: {self.get_encrepted_text()}"
                else:
                    self.decrept()
                    text = f"Decrypted Text: {self.get_decrepted_text()}"

                print("-"*20)
                print(text, "\n")

            else:
                print("\n", "-"*20)
                self.__url = input("Enter File Path >> ")
                key = input(f"\nEnter Key({key_type.__name__}) >> ")
                self.__key = int(key) if key_type == int else key
                text = ''
                if operation == "en":
                    text = f"Encrypted File Path: {self.encrept_file()}"
                else:
                    text = f"Decrypted File Path: {self.decrept_file()}"

                print("-"*20)
                print(text, "\n")


        except Exception as err:
            print(err)


