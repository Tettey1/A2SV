class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        while l<r:
            length = min(height[l],height[r])
            area = max(area,  length*abs(l-r))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return area
