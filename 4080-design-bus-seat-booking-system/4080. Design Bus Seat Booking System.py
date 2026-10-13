class BusBooking:
    def __init__(self, n: int):
        """
        {
            0: {A, B, C, D}
        }
        """
        self.n = n
        self.rows = defaultdict(set)
        self.total_time = 0
        self.total = 0
        self.mapping = {} # D1: 1
    
    def is_blocked_window_seat(self, letter, row):
        if letter == 'A' and 'B' in self.rows[row]:
            return True 
        if letter == "D" and "C" in self.rows[row]:
            return True
        return False

    def toggle(self, seat: str) -> None:
        letter, row = seat[0], int(seat[1:])

        if letter in self.rows[row]:
            self.total_time -= self.mapping[seat] 
            del self.mapping[seat]     
            self.rows[row].remove(letter)
            self.total -= 1
            return
        
        # Turning a seat on
        if self.is_blocked_window_seat(letter, row):
            self.mapping[seat] = 3
            self.total_time += 3
        else:
            self.mapping[seat] = 1
            self.total_time += 1
        self.total += 1
        self.rows[row].add(letter)

    def getTotalTime(self) -> int:
        return self.total_time
        
    def getMinTime(self) -> int:
        return self.total


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()