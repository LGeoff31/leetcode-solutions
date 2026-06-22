class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = Counter(text)
        print(a)
        # b a l l o o n
        b = [0] * 5
        for key in text:
            if key == "b":
                b[0] = a[key]
            elif key == "a":
                b[1] = a[key]
            elif key == "l":
                b[2] = a[key] // 2
            elif key == "o":
                b[3] = a[key] // 2
            elif key=="n":
                b[4] = a[key]
        print(b)
        return min(b)
