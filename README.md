# Cipherman

Lightweight command-line toolkit implementing classical ciphers (Caesar, Monoalphabetic, Playfair, Hill, Vigenere) for learning and experimentation.

---

## Table of Contents
- [Cipherman](#cipherman)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Quick start](#quick-start)
  - [CLI reference](#cli-reference)
  - [Examples](#examples)
  - [Project structure](#project-structure)
  - [Version](#version)
  - [Developers](#developers)
  - [License](#license)

---

## About

`Cipherman` is a small Python package that demonstrates classical cryptographic algorithms and provides a simple CLI for encrypting/decrypting text or files. It is intended for education, prototyping, and simple use-cases.

## Features

- Caesar cipher (shift)
- Monoalphabetic substitution
- Playfair cipher
- Hill cipher (matrix-based)
- Vigenere cipher (key-based and auto-key)
- Interactive text mode and file mode

## Prerequisites

- Python 3.8+ recommended
- `pip` and optionally `pipx` if you want an isolated CLI install

If your system uses an externally-managed Python (PEP 668), use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Installation

1. Clone the repo and change into it:

```bash
git clone https://github.com/your-repo/cipherman.git
cd cipherman
```

2. Quick install (attempts pip3 then pipx):

```bash
./install.sh
```

3. Manual install (inside virtualenv if needed):

```bash
python3 -m pip install --upgrade pip
pip3 install .
```

To uninstall:

```bash
./uninstall.sh
```

## Quick start

Run the CLI and pass flags to choose algorithm, operation and I/O mode. The CLI will then prompt for the specific inputs (text, filenames, key):

```bash
cipherman -a caesar -e -t   # encrypt text with Caesar (interactive prompts)
cipherman -a hill   -d -f   # decrypt a file with Hill (interactive prompts)
```

If `cipherman` is not on your PATH after installation, run it with `python3 -m cipherman.main` from the project root (or use the `bin/cipherman` entrypoint while developing).

## CLI reference

Key flags (run `cipherman -h` for full help):

- `-a, --algorithm` : choose `caesar` | `mono` | `play` | `hill` | `vigenere` | `vigenere-auto`
- `-e, --encryption` : perform encryption
- `-d, --decryption` : perform decryption
- `-t, --text`       : use interactive text mode (prompts for text and key)
- `-f, --file`       : use file mode (prompts for input file, output file and key)

After running a command with the flags above, the CLI prompts for the inputs required by the selected algorithm (e.g., plaintext/ciphertext, key or filenames).

## Examples

Below are sample interactive flows you can follow after running the commands.

- Encrypt text with Caesar (run, then follow prompts):

```bash
cipherman -a caesar -e -t
# then enter plaintext and the integer key when prompted
```

- Decrypt text with Caesar:

```bash
cipherman -a caesar -d -t
# enter ciphertext and the integer key
```

- Encrypt a file with Caesar (prompts for input and output filenames and key):

```bash
cipherman -a caesar -e -f
# enter input filename, output filename, and integer key
```

- Encrypt text with Hill (key must form a square matrix; CLI will validate length):

```bash
cipherman -a hill -e -t
# enter plaintext and key string (length must be a perfect square)
```

- Encrypt text with Vigenere (run, then follow prompts):

```bash
cipherman -a vigenere -e -t
# then enter plaintext and the key when prompted
```

- Decrypt text with Vigenere:

```bash
cipherman -a vigenere -d -t
# enter ciphertext and the key
```

- Encrypt a file with Vigenere (prompts for input and output filenames and key):

```bash
cipherman -a vigenere -e -f
# enter input filename, output filename, and key
```

- Encrypt text with Vigenere auto-key (run, then follow prompts):

```bash
cipherman -a vigenere-auto -e -t
# then enter plaintext and the key when prompted
```

- Decrypt text with Vigenere auto-key:

```bash
cipherman -a vigenere-auto -d -t
# enter ciphertext and the key
```

- Encrypt a file with Vigenere auto-key (prompts for input and output filenames and key):

```bash
cipherman -a vigenere-auto -e -f
# enter input filename, output filename, and key
```

Notes:

- `caesar` key is an integer (shift amount).
- `hill` key length must be a perfect square (e.g., 9 → 3×3 matrix). The CLI pads plaintext as needed.
- `mono` and `play` use text keys; duplicate letters are cleaned automatically.


## Project structure

```
install.sh          # Installation script
uninstall.sh        # Uninstallation script
setup.py            # Package setup
bin/
    cipherman       # CLI entry point
cipherman/          # Package source
    __init__.py
    caesar_cipher.py
    cipher_helper.py
    cipher.py
    hill_cipher.py
    main.py
    mono_cipher.py
    playfair_cipher.py
    utils.py
```

## Version

- **Current version:** 1.2.0
- **Release date:** 2026-03-31

We use semantic versioning (MAJOR.MINOR.PATCH). Update the version in `setup.py` when releasing.

Check installed version:

```bash
cipherman --version
```

## Developers

- **Name**: Mohammed Galal
- **Email**: MohammedGalal7777@hotmail.com
- **GitHub**: https://github.com/MohammedGalal-IT

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
