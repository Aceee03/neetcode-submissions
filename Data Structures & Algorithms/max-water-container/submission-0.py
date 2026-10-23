class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        areas = []
        while i < j:
            height = min(heights[i], heights[j])
            width = j - i
            water = height * width
            areas.append(water)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max(areas)

            