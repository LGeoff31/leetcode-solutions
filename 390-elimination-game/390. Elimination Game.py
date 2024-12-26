class Solution:
    def lastRemaining(self, n: int) -> int:

        def f(start, size, skip, forward):
            # print(start, size, skip, forward)
            if size == 1:
                return start
            
            if forward:
                return f(start + skip, size // 2, skip * 2, not forward)
            else:
                if size % 2 == 0:
                    return f(start, size // 2, skip * 2, not forward)
                else:
                    return f(start + skip, size // 2, skip * 2, not forward)
        
        start, size, skip, forward = 1, n, 1, True

        while size > 1:
            if forward:
                start, size, skip, forward = start + skip, size // 2, skip * 2, not forward
            else:
                if size % 2 == 0:
                    start, size, skip, forward = start, size // 2, skip * 2, not forward
                else:
                    start, size, skip, forward = start + skip, size // 2, skip * 2, not forward

        return start
        
        # return f(1, n, 1, True)

        