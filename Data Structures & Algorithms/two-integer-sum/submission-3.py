# We will loop through the array with two pointers i and j
# to differentiate the pointers i will start at 0 and j will start
# at 1 each time we will add the two values together and if the values 
# equate to the target number, we will add those indices to a hashmap.
# number.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapNums = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapNums:
                return [mapNums[diff], i]
            mapNums[n] = i
            
            