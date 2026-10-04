class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seek=set()
        for num in nums:
            if num in seek:
                return True
            seek.add(num)
        return False
        