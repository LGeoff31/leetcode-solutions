class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        #1: [1,2]
        #2: if 1.) is 2, [1,2,3,4], else [1,2,3,4,5,6,7,8,9]
        #3: [1,2,3,4,5]
        #4: [1,2,3,4,5,6,7,8,9]

        time = []
        for i in permutations(arr):
            if str(i[0]) + str(i[1]) < "24" and str(i[2]) + str(i[3]) < "60": #valid
                time.append(str(i[0]) + str(i[1]) + ":" + str(i[2]) + str(i[3]))
        return max(time) if time else ""