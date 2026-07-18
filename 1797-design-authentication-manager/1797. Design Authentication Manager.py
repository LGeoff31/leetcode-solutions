class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token_to_expiry = {}
        self.lst = SortedList()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_to_expiry[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token_to_expiry:
            return None
        
        previous_expiry_time = self.token_to_expiry[tokenId]
        if previous_expiry_time <= currentTime:
            return

        self.token_to_expiry[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for key, value in self.token_to_expiry.items():
            if value > currentTime:
                cnt += 1
        return cnt
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)