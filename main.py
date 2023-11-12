import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == "\d":
        return any(char.isdigit() for char in input_line)
    elif pattern == "\w":
        return any(char.isalnum() for char in input_line)
    elif pattern.startswith("[") and pattern.endswith("]"):
        pattern = pattern.removeprefix("[").removesuffix("]")
        allowed_chars = set(pattern)
        return any(char in allowed_chars for char in input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    pattern, input_line = sys.argv[2], sys.argv[3]


    if match_pattern(input_line, pattern):
        print(f"\033[32mTest Passed\033[0m")
        exit(0)
    else:
        print(f"\033[31mTest Failed\033[0m")
        exit(1)


if __name__ == "__main__":
    main()