class Solution(object):
    def search(self, nums, target):
        first = 0
        last = len(nums) - 1

        while first <= last:
            mid = (first + last) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                first = mid + 1

            else:
                last = mid - 1

        return -1


obj = Solution()
print(obj.search([-1,0,3,5,9,12], 3))