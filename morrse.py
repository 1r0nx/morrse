#!/usr/bin/env python3
import argparse
import re
import sys

MORSE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}

REVERSE_MORSE_DICT = {v: k for k, v in MORSE_DICT.items()}


def encode(text):
    return " ".join(MORSE_DICT[c] for c in text.upper() if c in MORSE_DICT)


def decode(morse):
    # Séparateurs de mots : / ; ,
    word_separators = r"[\/;,]+"

    words = re.split(word_separators, morse.strip())
    decoded_words = []

    for word in words:
        letters = word.strip().split()
        decoded_letters = []

        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                decoded_letters.append(REVERSE_MORSE_DICT[letter])
            else:
                decoded_letters.append("[-] No morse code was decoded!!!!")

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


def print_global_help():
    print(
        """
MORSE – Encoder & Decoder

Usage :
  morrse enc -s "text"
  morrse dec -s "morse code"

Examples:
  morrse enc -s "text"
  morrse dec -s "- . ... -"

Possible separator:
  space   /   ;   ,

Modes:
  morrse enc
  morrse dec
"""
    )


def print_mode_help(mode):
    if mode == "enc":
        print(
            """
Encoder mode (text → morse)

Usage:
  morrse enc -s "text to encode"
"""
        )
    elif mode == "dec":
        print(
            """
Decoder mode (morse → texte)

Usage:
  morrse dec -s "morse code"

Examples:
  morrse dec -s "- . ... -"
  morrse dec -s "-/./.../-"
  morrse dec -s "-;.;...;-"
  morrse dec -s "-,.,...,-"

Possible separator:
  space   /   ;   ,
"""
        )


def main():
    # No argument → global help
    if len(sys.argv) == 1:
        print_global_help()
        sys.exit(0)

    # If "enc" or "dec" → print help acordingly
    if len(sys.argv) == 2 and sys.argv[1] in ("enc", "dec"):
        print_mode_help(sys.argv[1])
        sys.exit(0)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("mode", choices=["enc", "dec"])
    parser.add_argument("-s", "--string")

    args = parser.parse_args()

    if not args.string:
        print_mode_help(args.mode)
        sys.exit(1)

    if args.mode == "enc":
        print(encode(args.string))
    else:
        print(decode(args.string))


if __name__ == "__main__":
    main()
