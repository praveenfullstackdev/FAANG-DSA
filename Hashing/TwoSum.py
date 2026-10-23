def TwoSum(nums:list[int], target: int)->list[int]:
    seen = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],idx]
        seen[num] = idx    
    


def main():
    nums = [4, 9, 2, 7]
    target = 11
    print("Output:", TwoSum(nums,target))


if __name__ == "__main__":
    main()
