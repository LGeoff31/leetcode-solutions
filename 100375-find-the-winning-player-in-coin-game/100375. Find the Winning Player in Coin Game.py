class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        alice = True
        while x >= 0 and y >= 0:
            if alice:
                x -= 1
                y -= 4
                if x < 0 or y < 0:
                    return "Bob"
            else:
                x -= 1
                y -= 4
                if x < 0 or y < 0:
                    return 'Alice'
            alice = not alice
        
        