class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.temperatures=temperatures
        n=len(temperatures)
        result=[0]*n
        previous_day=0
        stack=[]

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                previous_day=stack.pop()
                result[previous_day]=i-previous_day
            stack.append(i)
        return result