class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Output array will first store left products
        output = [1] * n

        # Step 1: Store left products
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # Step 2: Multiply with right products
        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output