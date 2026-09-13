class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # had to define before using lol
        def get_1_coords(lst: List[List[int]]):
            coords = []
            for i in range(len(lst)):
                for j in range(len(lst[i])):
                    if lst[i][j] == 1:
                        coords.append([i, j])
                    continue
            return coords
        
        # collect all the 1s in each img as coordinates
        coords1 = get_1_coords(img1)
        coords2 = get_1_coords(img2)

        diffCounts = {}
        ref = []
        target = []
        # grab the shorter list as the ref
        if len(coords1) <= len(coords2):
            ref = coords1
            target = coords2
        else:
            ref = coords2
            target = coords1
        print(ref)
        print(target)

        # compute differences and add to hashmap
        for r in ref:
            for t in target:
                dr = t[0] - r[0]
                dc = t[1] - r[1]
                if (dr, dc) not in diffCounts.keys():
                    diffCounts[(dr, dc)] = 1
                else:
                    diffCounts[(dr, dc)] += 1
        print(diffCounts)

        # result is the max occurrences
        # return max(diffCounts.values())
        return max(diffCounts.values(), default=0)


        