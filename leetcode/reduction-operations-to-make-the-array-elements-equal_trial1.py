class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)-1
        count = 0
        for r in range(n-1,-1,-1):
            if nums[r] != nums[r+1]:
                count += n-r
        
        return count