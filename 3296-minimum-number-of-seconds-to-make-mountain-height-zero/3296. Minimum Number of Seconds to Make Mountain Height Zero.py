class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left = 1
        right = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        minSeconds = mountainHeight

        def isValid(seconds):
            """
            worker * (n * (n+1) / 2) <= seconds
            n^2 + n - 2 * seconds / worker = 0

            n*(n+1)/2 <= seconds / worker
            n^2/2 + n/2 <= seconds/worker
            n^2 + n - 2*seconds/worker <- 0
            """
            contributions = 0
            for worker in workerTimes:
                contribution = floor((-1 + sqrt(1 - 4*(-2*seconds/worker))) / 2)
                contributions += contribution
                if contributions >= mountainHeight:
                    return True
            return False

        while left <= right:
            mid = (left + right) // 2

            # validate you can clear mountain in mid seconds
            if isValid(mid):
                minSeconds = mid
                right = mid - 1
            else:
                left = mid + 1
        return minSeconds

                