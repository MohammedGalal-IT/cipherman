from pathlib import Path
from argparse import ArgumentParser

from .mono_cipher import MonoCipher
from .caesar_cipher import CaesarCipher
from .playfair_cipher import PlayfairCipher


def main():

    parser = ArgumentParser(prog='cipherman', description='Encrypt or Decrypt a plain text or a text file using Classical Encryption Techniques. Supported techniques: "1.Caesar Cipher" "2.Monoalphabetic Cipher" "3.Playfair Cipher"')

    group_one = parser.add_mutually_exclusive_group()
    group_two = parser.add_mutually_exclusive_group()

    parser.add_argument("-a", "--algorithm",
                    choices=['caesar', 'mono', 'play'],
                    help=":specify encryption / decryption algorithm. choices are: 'caesar' for Caesar Cipher, 'mono' for Monoalphabetic Cipher, 'play' for Playfair Cipher")
    group_one.add_argument("-e", "--encryption",
                   action="store_true",
                   help=":specify type of operation as encryption")
    group_one.add_argument("-d", "--decryption",
                   action="store_true",
                   help=":specify type of operation as decryption")
    group_two.add_argument("-t", "--text",
                       action="store_true",
                       help=":specify input and output target as text")
    group_two.add_argument("-f", "--file",
                       action="store_true",
                       help=":specify input and output target as file")

    args = parser.parse_args()


    def call_cmd(obj, key_type=str):
        target = "text" if args.text else "file"
        operation = "en" if args.encryption else "de"
        obj.cmd_start(target, operation, key_type)

    condition = (args.text or args.file) and (args.encryption or args.decryption)

    if args.algorithm == 'mono' and condition:
        call_cmd(MonoCipher())
    elif args.algorithm == 'caesar' and condition:
        call_cmd(CaesarCipher(), int)
    elif args.algorithm == 'play' and condition:
        call_cmd(PlayfairCipher())
    elif not condition:
        print("Worng Options !!!\n\n")
        parser.print_help()
    else:
        print("Use option --help or -h to show command info")


if __name__ == "__main__":
    main()
