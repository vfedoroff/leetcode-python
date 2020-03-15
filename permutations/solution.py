
def permute(nums):
    if nums is None:
        return []
    if len(nums) == 1:
        return [nums]
    output = []
    for i in range(len(nums)):
        part = nums[:i] + nums[i+1:]
        for m in permute(part):
            output.append(nums[i:i+1] + m)
    return output

if __name__ == "__main__":
    nums = [1,2,3] 
    res = permute(nums)
    print(res)