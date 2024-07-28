import math
from collections import deque, defaultdict
from typing import List

class Solution:
    def canReachCorner(self, X: int, Y: int, p: List[List[int]]) -> bool:
        circles = []
        for arr in p:
            if arr not in circles:
                circles.append(arr)
        
        def circles_intersect(c1, c2):
            x1, y1, r1 = c1
            x2, y2, r2 = c2
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            return distance <= r1 + r2
        
        adj = defaultdict(list)

        for i in range(len(circles)):
            for j in range(i + 1, len(circles)):
                if circles_intersect(circles[i], circles[j]):
                    adj[tuple(circles[i])].append(circles[j])
                    adj[tuple(circles[j])].append(circles[i])

        # Left touch Down
        visited = set()
        queue = deque([])

        for x, y, r in circles:
            y_val_pos = math.sqrt(r ** 2 - x ** 2) + y if r ** 2 - x ** 2 >= 0 else -1e9
            y_val_neg = -math.sqrt(r ** 2 - x ** 2) + y if r ** 2 - x ** 2 >= 0 else -1e9
            if (y_val_pos >= 0 and y_val_neg <= Y): # Two intersections
                queue.append((x, y, r))
                visited.add((x, y, r))
            elif y_val_pos == y_val_neg and 0 <= y_val_pos <= Y:
                queue.append((x, y, r))
                visited.add((x, y, r))

        while queue:
            x, y, r = queue.popleft()
            x_val_pos = math.sqrt(r ** 2 - y ** 2) + x if r ** 2 - y ** 2 >= 0 else -1e9
            x_val_neg = -math.sqrt(r ** 2 - y ** 2) + x if r ** 2 - y ** 2 >= 0 else -1e9
            if (x_val_neg <= X and x_val_pos >= 0) and y-r <= 0 <= y+r:
                return False
            elif x_val_neg == x_val_pos and 0 <= x_val_pos <= X and y-r <= 0 <= y+r:
                return False
            
            for nei in adj[(x, y, r)]:  
                if tuple(nei) not in visited:
                    visited.add(tuple(nei))
                    queue.append(nei)

        # Left touch right
        visited = set()
        queue = deque([])

        for x, y, r in circles:
            y_val_pos = math.sqrt(r ** 2 - x ** 2) + y if r ** 2 - x ** 2 >= 0 else -1e9
            y_val_neg = -math.sqrt(r ** 2 - x ** 2) + y if r ** 2 - x ** 2 >= 0 else -1e9
            if (y_val_pos >= 0 and y_val_neg <= Y): # Two intersections
                queue.append((x, y, r))
                visited.add((x, y, r))
            elif y_val_pos == y_val_neg and 0 <= y_val_pos <= Y:
                queue.append((x, y, r))
                visited.add((x, y, r))

        while queue:
            x, y, r = queue.popleft()
            y_val_pos = math.sqrt(r ** 2 - (X-x) ** 2) + y if r ** 2 - (X-x) ** 2 >= 0 else -1e9
            y_val_neg = -math.sqrt(r ** 2 - (X-x) ** 2) + y if r ** 2 - (X-x) ** 2 >= 0 else -1e9
            if (y_val_neg <= Y and y_val_pos >= 0) and x-r <= X <= x+r:
                return False
            elif y_val_neg == y_val_pos and 0 <= y_val_pos <= Y and x-r <= X <= x+r:
                return False
            
            for nei in adj[(x, y, r)]:  
                if tuple(nei) not in visited:
                    visited.add(tuple(nei))
                    queue.append(nei)
        
        
        # Right touch Top
        visited = set()
        queue = deque([])

        for x, y, r in circles:
            y_val_pos = math.sqrt(r ** 2 - (X-x) ** 2) + y if r ** 2 - (X-x) ** 2 >= 0 else -1e9
            y_val_neg = -math.sqrt(r ** 2 - (X-x) ** 2) + y if r ** 2 - (X-x) ** 2 >= 0 else -1e9
            if (y_val_pos >= 0 and y_val_neg <= Y): # Two intersections
                queue.append((x, y, r))
                visited.add((x, y, r))
            elif y_val_pos == y_val_neg and 0 <= y_val_pos <= Y:
                queue.append((x, y, r))
                visited.add((x, y, r))
        
        while queue:
            x, y, r = queue.popleft()
            x_val_pos = math.sqrt(r ** 2 - (Y-y) ** 2) + x if r ** 2 - (Y-y) ** 2 >= 0 else -1e9
            x_val_neg = -math.sqrt(r ** 2 - (Y-y) ** 2) + x if r ** 2 - (Y-y) ** 2 >= 0 else -1e9
            if (x_val_neg <= X and x_val_pos >= 0) and y-r <= Y <= y+r:
                return False
            elif x_val_neg == x_val_pos and 0 <= x_val_pos <= X and y-r <= Y <= y+r:
                return False
            
            for nei in adj[(x, y, r)]:  
                if tuple(nei) not in visited:
                    visited.add(tuple(nei))
                    queue.append(nei)
        
        # Top touch down
        visited = set()
        queue = deque([])

        for x, y, r in circles:
            x_val_pos = math.sqrt(r ** 2 - (Y-y) ** 2) + x if r ** 2 - (Y-y) ** 2 >= 0 else -1e9
            x_val_neg = -math.sqrt(r ** 2 - (Y-y) ** 2) + x if r ** 2 - (Y-y) ** 2 >= 0 else -1e9
            if (x_val_neg <= X and x_val_pos >= 0):
                queue.append((x, y, r))
                visited.add((x, y, r))
            elif x_val_neg == x_val_pos and 0 <= x_val_pos <= X:
                queue.append((x, y, r))
                visited.add((x, y, r))
        
        while queue:
            x, y, r = queue.popleft()
            x_val_pos = math.sqrt(r ** 2 - y ** 2) + x if r ** 2 - y ** 2 >= 0 else -1e9
            x_val_neg = -math.sqrt(r ** 2 - y ** 2) + x if r ** 2 - y ** 2 >= 0 else -1e9
            print(x,y,r, x_val_pos, x_val_neg)
            if (x_val_neg <= X and x_val_pos >= 0) and y-r <= 0 <= y+r:
                return False
            elif x_val_neg == x_val_pos and 0 <= x_val_pos <= X and y-r <= 0 <= y+r:
                return False
            
            for nei in adj[(x, y, r)]:  
                if tuple(nei) not in visited:
                    visited.add(tuple(nei))
                    queue.append(nei)





        return True
