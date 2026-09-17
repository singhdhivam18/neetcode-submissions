class Solution:
    def maxArea(self, heights: List[int]) -> int:
        self.heights=heights
        left=0
        right=len(heights)-1
        max_amt=0
        while left<right:#we need two bars 
            width=right-left
            height=min(heights[right],heights[left])
            area=width*height
            max_amt=max(max_amt,area)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_amt
        