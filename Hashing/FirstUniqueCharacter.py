def first_unique_character(s):
    # Hash map storing {character: frequency}
    counts = {}

    # Pass 1: Count how many times each character appears
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Pass 2: Iterate over original string to guarantee correct order
    for char in s:
        if counts[char] == 1:
            return char

    # No unique character found
    return -1


def main():
    text = "swiss"
    print("The first unique character is:", first_unique_character(text))


if __name__ == "__main__":
    main()