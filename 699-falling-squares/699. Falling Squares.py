class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # Looking at current squares, if old_l < new_l < old_l + sidelength, then the square will sit on top
        # We should also keep track of heights when square is placed
        # maxHEAP to look at the squares with current largest height
        lst = SortedList()
        ans = []

        for left_x, side_length in positions:
            landed_x_axis = True
            # See if it falls on top of another
            for i in range(len(lst)-1,-1,-1):
                h,l,s = lst[i]
                if l <= left_x < l+s or left_x <= l < left_x+side_length or left_x <= l <= l+s <= left_x+side_length:
                    landed_x_axis = False
                    lst.add((h+side_length, left_x, side_length))
                    break

            if landed_x_axis:
                lst.add((side_length, left_x, side_length))

            ans.append(lst[-1][0])
        

        return ans