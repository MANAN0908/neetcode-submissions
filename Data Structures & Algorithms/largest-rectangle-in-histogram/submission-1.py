class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i in range(len(heights)+1):
            current_height = 0 if i == len(heights) else heights[i]
            while stack and heights[stack[-1]]>current_height:
                prev=stack.pop()
                if stack:
                    width=i-stack[-1]-1
                else:
                    width=i
                area=heights[prev]*width
                maxarea=max(maxarea,area)
            stack.append(i)
        return maxarea
        