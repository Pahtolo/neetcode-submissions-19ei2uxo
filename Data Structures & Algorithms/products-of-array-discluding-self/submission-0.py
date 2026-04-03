class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            temp = nums[0:i] + nums[i+1:]
            output.append(math.prod(temp))
        
        return output