def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

def contains_duplicate_set_comparison(nums: list[int]) -> bool:
    # If the length of the set is different from the list, there are duplicates
    return len(nums) != len(set(nums))


def main():
    nums = [1, 2, 3, 4]
    print("Contains duplicate:", contains_duplicate_set_comparison(nums))
    print("Contains duplicate:", contains_duplicate(nums))


if __name__ == "__main__":
    main()
