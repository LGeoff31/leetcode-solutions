class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even1, odd1, even2, odd2 = n//2, n//2, m//2, m//2
        if n%2==1:odd1+=1
        if m%2==1:odd2+=1
        return even1*odd2+odd1*even2
