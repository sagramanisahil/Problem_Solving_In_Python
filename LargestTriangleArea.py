class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        length = len(points)
        area = 0

        for i in range(length):
            for j in range(i, length):
                for k in range(j, length):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = max(area, abs(0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))))

        return area
