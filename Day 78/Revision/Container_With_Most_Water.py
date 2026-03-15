def maxArea(heights):
        left = 0
        right = len(heights)-1
        area = 0

        while left < right:
            h = min(heights[left], heights[right])
            width = right - left
            area = max(area, h * width)

            if heights[left] < heights[right]:
                left+=1
            else:
                right -= 1
        return area


heights = [1,7,2,5,4,7,3,6]
print(maxArea(heights))