# Process:
# Create loop through array and a pointer that tracks
# the last value in the array and compares it to the current value
# if there is a match, return true otherwise return false and exit.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False