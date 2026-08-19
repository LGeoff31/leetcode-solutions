class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_seats_by_row = defaultdict(set)
        for row, col in reservedSeats:
            reserved_seats_by_row[row].add(col)
        
        number_free_size_four_blocks = 0
        for row in reserved_seats_by_row:
            seat_ptr = 2
            reserved_seats_in_row = reserved_seats_by_row[row]
            while seat_ptr <= 6:
                if seat_ptr not in [2,4,6]:
                    seat_ptr += 1
                    continue 

                if not any(seat_ptr+i in reserved_seats_in_row for i in range(4)):
                    number_free_size_four_blocks += 1
                    seat_ptr += 4
                else:
                    seat_ptr += 1   

        return number_free_size_four_blocks + (n - len(reserved_seats_by_row)) * 2