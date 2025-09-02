class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        a = set(friends)
        res = []
        for n in order:
            if n in a: res.append(n)
        return res