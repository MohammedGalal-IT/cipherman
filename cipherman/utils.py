import glob
import os

try:
    import readline
except ImportError:
    readline = None




def clear_screen():
#    os.system('cls' if os.name == 'nt' else 'clear')
    pass


def configure_input_completion(choices=['caesar', 'mono', 'play', 'hill', 'vigenere'], path=False):
    if readline is None:
        return

    readline.set_completer_delims(' \t\n;')

    def completer(text, state):
        if path:
            word = os.path.expanduser(text)
            if os.path.isdir(word):
                word = word + os.sep

            directory = os.path.dirname(word) or '.'
            prefix = os.path.basename(word)
            try:
                entries = glob.glob(os.path.join(directory, prefix) + '*')
            except Exception:
                entries = []

            matches = []
            for entry in entries:
                if os.path.isdir(entry):
                    entry = entry + os.sep
                matches.append(entry)

            return matches[state] if state < len(matches) else None

        if choices is None:
            return None

        matches = [item for item in choices if item.startswith(text)]
        return matches[state] if state < len(matches) else None

    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')


def prefill_input_line(text):
    """
    Prefill the next input() prompt with the given string (if readline is available).
    Usage:
        prefill_input_line("default text")
        value = input("Prompt: ")
    """
    if readline is None:
        return
    try:
        readline.set_startup_hook(lambda: readline.insert_text(text))
    except Exception:
        pass