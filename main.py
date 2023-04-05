class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = dict()
        for x in range(len(nums)):
            nums_dict[x] = nums[x]
        for x in nums_dict:
            print(x)
            

numbers = [2,7,11,15]
goal = 9
print(Solution.twoSum(Solution,numbers,goal))