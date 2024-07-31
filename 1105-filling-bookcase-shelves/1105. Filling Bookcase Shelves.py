class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            max_height = 0
            curr_width = shelfWidth
            dp[i] = 1e9
            for j in range(i, len(books)):
                width, height = books[j]
                if curr_width < width:
                    break
                curr_width -= width
                max_height = max(max_height, height)
                dp[i] = min(dp[i], dp[j+1] + max_height)
        return dp[0]

        