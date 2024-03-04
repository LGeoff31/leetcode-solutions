class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1   
        maxScore = 0
        score = 0

        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            else:
                if score == 0: break
                power += tokens[r]
                score -= 1
                r -= 1
            maxScore = max(maxScore, score)
        return maxScore

#[55,71,82]

power = 137
SCORE = -1
        