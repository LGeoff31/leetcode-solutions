class Solution:
    def minimumLength(self, s: str) -> int:
        """ 
        1 -> 1
        2 -> 2
        3 -> 1
        4 -> 2
        5 -> 1 
        6 -> 2


        """
        character_frequency = Counter(s)
        return sum((2 if character_frequency[c] % 2 == 0 else 1) for c in character_frequency)
