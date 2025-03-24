class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res = 0
        end = 0

        for meeting in meetings:
            if meeting[0] > end:
                res += meeting[0] - end - 1
            end = max(end, meeting[1])

        if days > end:
            res += days - end
        return res