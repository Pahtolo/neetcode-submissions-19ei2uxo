class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        
        for a, b in enumerate(nums):
            A[b] = a
        for a, b in enumerate(nums):
            diff = target - b
            if diff in A and A[diff] != a:
                return [a, A[diff]]
        return []
    

        

            