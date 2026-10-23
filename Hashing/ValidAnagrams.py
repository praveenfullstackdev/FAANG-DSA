def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char,0) + 1
    for char in t:
        count_t[char] = count_t.get(char,0) + 1

    return count_s == count_t        

def is_anagram_single_dict(s: str, t: str) -> bool:
    # Early exit if lengths don't match
    if len(s) != len(t):
        return False

    # Single dictionary to balance counts
    counts = {}

    # Increment for characters in s
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    # Decrement for characters in t
    for char in t:
        # If char isn't present or count is already 0, not an anagram
        if char not in counts or counts[char] == 0:
            return False
        counts[char] -= 1

    # Every letter balanced out
    return True

def is_anagram_optimized(s:str , t:str) -> bool:
    count = [0] *26
    for a,b in zip(s,t) :
        count[ord(a) - ord("a")]+=1
        count[ord(b) - ord("a")]-=1

    return all(c==0 for c in count) 


    

def main():
    s = "rat"
    t = "tar"
    print("Is valid anagram:", is_anagram_optimized(s, t))


if __name__ == "__main__":
    main()
