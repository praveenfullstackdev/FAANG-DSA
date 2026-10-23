def can_construct(ransom_note: str, magazine: str) -> bool:

    if len(ransom_note) > len(magazine):
        return False
    
    counts = {}

    for char in magazine:
        counts[char] = counts.get(char, 0) + 1

    for char in ransom_note:
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    return True

def main():
    ransom_note = "aa"
    magazine = "aab"
    print("Can construct:", can_construct(ransom_note, magazine))


if __name__ == "__main__":
    main()
