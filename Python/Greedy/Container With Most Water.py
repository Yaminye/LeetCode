class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
            else:
                area = (right - left) * height[right]

            if area > max_area:
                max_area = area
            
            if height[left] < height[right]:
                prev = height[left]
                left += 1
                while left < right and height[left] <= prev:
                    left += 1
            else:
                prev = height[right]
                right -= 1
                while left < right and height[right] <= prev:
                    right -= 1
        
        return max_area
            



