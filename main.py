import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, patterns):
    patterns = parse_pattern(patterns)
    char_count = 0

    for idx, pattern in enumerate(patterns):
        # search for numeric character
        if pattern == "\d":
            if input_line[char_count].isdigit() == False:
                return False
            char_count += 1
        
        # search for alphanumeric character
        elif pattern == "\w":
            if input_line[char_count].isalnum() == False:
                return False
            char_count += 1

        # search for space character
        elif pattern == "\s":
            if input_line[char_count] != " ":
                return False
            char_count += 1

        # search specific characters
        elif (pattern.startswith("/") or pattern.startswith("[")) == False:
            if pattern != input_line[char_count:char_count+len(pattern)]:
                return False
            char_count += len(pattern)
        
        # search for negative character groups e.g. [^abc]
        elif pattern.startswith("[^") and pattern.endswith("]"):
            pattern = pattern.removeprefix("[^").removesuffix("]")
            disallowed_chars = set(pattern)
            return any(char not in disallowed_chars for char in input_line)
        
        # search for positive character groups e.g. [abc]
        elif pattern.startswith("[") and pattern.endswith("]"):
            pattern = pattern.removeprefix("[").removesuffix("]")
            allowed_chars = set(pattern)
            return any(char in allowed_chars for char in input_line)
        
        # raise exception for unknown pattern input
        else:
            raise RuntimeError(f"Unhandled pattern: {pattern}")

    return True

def parse_pattern(patterns):
    patterns = patterns.replace(" ", " \s ")
    patterns = patterns.replace("\d", " \d ").replace("\w", " \w ")
    patterns = patterns.replace("[", " [").replace("]", "] ").split()
    return patterns


def main():
    
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if len(sys.argv) != 4:
        print("Program expects four arguments.")
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