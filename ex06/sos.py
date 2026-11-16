import sys


def main():
    """Convert a string of letters, digits and spaces to Morse code."""
    morse = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
        "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
        "M": "--", "N": "-.", "O": "---", "P": ".--.",
        "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
        "Y": "-.--", "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---",
        "3": "...--", "4": "....-", "5": ".....",
        "6": "-....", "7": "--...", "8": "---..",
        "9": "----.",
        " ": "/"
    }

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        text = sys.argv[1]

        assert all(
            char in morse or char in "abcdefghijklmnopqrstuvwxyz"
            for char in text
        ), "the arguments are bad"

        result = [morse[char.upper()] for char in text]
        print(" ".join(result))

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
