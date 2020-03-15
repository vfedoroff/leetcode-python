def twoSum(nums, target):
    if nums is None or len(nums) == 0:
        return (0,0)
    
    map = {}
    for i in range(len(nums)):
        if nums[i] in map:
            return (map[nums[i]], i)
        map[target-nums[i]] = i

def main():
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([4, 5, 1, 8], 6))
    pass
if __name__ == "__main__":
    main()