import sys


def main():
    """Filter words longer than the provided integer."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        length = int(sys.argv[2])

        result = list(filter(lambda word: len(word) > length,
                             [word for word in text.split()]))
        print(result)

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
