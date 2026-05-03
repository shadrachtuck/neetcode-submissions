class Solution:
    def climbStairs(self, n: int) -> int:
        # two pointers one for single step and two for double
        one, two = 1, 1
        # shifting left from the end of the array
        for i in range(n - 1):
            temp = one
            # adding previous two vals
            one = one + two
            # update two to previous value that one was initially set to 
            # hence the need for a temp var
            two = temp
            # return whatever one lands on next
        return one