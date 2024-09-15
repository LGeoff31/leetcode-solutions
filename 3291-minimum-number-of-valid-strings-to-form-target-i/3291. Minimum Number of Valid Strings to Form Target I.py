class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["#"] = word

        n = len(target)
        dp =[1e9] * (n+1)
        dp[n] = 0
        # "aabcdabc"
        [1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 1e9, 0]
        for i in range(n-1, -1, -1):
            node = trie
            for j in range(i, n):
                if target[j] in node:
                    node = node[target[j]]
                else:
                    break
                dp[i] = min(dp[i], 1 + dp[j+1])

        return dp[0] if dp[0] < 1e8 else -1