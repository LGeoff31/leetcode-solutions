class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        """
        bunch of line graphs
        they merge when the y-diff <= distance
        can we just simulate time ?? and use a sortedlist
        we are done only if positiosn further have greater slope

        EDGE CASE, try to merge as many thigns to start with ?? from left -> right
        """
        stack = [] # (position, speed)

        for i in range(len(position) - 1, -1, -1):
            current_position, current_speed = position[i], speed[i]
            if stack:
                previous_position, previous_speed = stack[-1]
                # TWO CASE WHERE WE CAN GUARENTEE A MERGE WILL HAPPEN, SKI POVER
                if previous_position - current_position <= distance:
                    stack[-1][0] = current_position # take the smaller position
                    continue 
                if current_speed > previous_speed:
                    stack[-1][0] = current_position
                    continue 

            stack.append([current_position, current_speed])
        return len(stack)
                
            