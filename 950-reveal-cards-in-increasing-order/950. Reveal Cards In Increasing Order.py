class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        lst = [0] * len(deck)
        deck.sort()
        q = deque(range(len(deck)))

        for n in deck:
            i = q.popleft()
            lst[i] = n

            if q:
                q.append(q.popleft())
        return lst