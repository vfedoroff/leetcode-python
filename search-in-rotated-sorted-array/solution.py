class Solution(object):
    def findPivot(self, nums, low, high):
        if low > high:
            return -1
        if high == low:
            return low
        middle = int((high + low)/2)
        if middle < high and nums[middle] > nums[middle + 1]: 
            return middle 
        if middle > low and nums[middle] < nums[middle - 1]: 
                return (middle-1) 
        if nums[low] >= nums[middle]: 
                return findPivot(nums, low, middle-1) 
        return findPivot(nums, middle + 1, high)

    def binarySearch(self, nums, low, high, key): 
        if high < low: 
            return -1
        mid = int((low + high)/2) 
        if key == nums[mid]: 
            return mid 
        if key > nums[mid]: 
            return self.binarySearch(nums, (mid + 1), high, key)
        return self.binarySearch(nums, low, (mid -1), key)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        pivot = self.findPivot(nums, 0, n-1)
        if pivot == -1: 
            return self.binarySearch(nums, 0, n-1, target)
        if nums[pivot] == target: 
            return pivot 
        if nums[0] <= target: 
            return self.binarySearch(nums, 0, pivot-1, target)
        return self.binarySearch(nums, pivot+1, n-1, target)  

if __name__ == "__main__":
    solution = Solution()
    assert solution.search([4,5,6,7,0,1,2],0) == 4
