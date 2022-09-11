class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [:] replaces elements in place.  Technically nums = would be a new object
        nums[:] = sorted(set(nums))
        return len(nums)
        