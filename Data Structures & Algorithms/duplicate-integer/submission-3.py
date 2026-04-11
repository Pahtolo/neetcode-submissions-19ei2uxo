class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] in nums_map:
                return True
            else:
                nums_map[nums[i]] = True
        return False