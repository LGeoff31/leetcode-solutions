class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        """
        7: 0111
        4: 0100

        7 OR 4 = 7
        7 AND 4 = 4

        [2,5,6,8], k=2

        8: 1000
        6: 0110

        8 OR 6 = 14
        8 AND 6 = 0

        [2,5,0,14]

        2 OR 5 = 7
        2 AND 5 = 0

        [7,0,0,14]

        5 OR 3 = 7
        5 AND 3 = 1

        6 OR 2 = 6
        6 AND 2 = 2

        14^2 + 7^2 = 196 + 49 = 245

        Greedy + Sorting + bitwise operations
    
    idx 7654 3210
        0101 1010

        5 numbers in total

        across all the numbers, 
        {0: 3} 
        implies 3 of the numbers have bit set at index 0

        [2,6,5,8]

        2: 0010
        6: 0110
        5: 0101
        8: 1000

        {0:0, 1:0, 2:0, 3:0}

        k=2
        BUILD 1st number: 1+2+4+8 = 15
        BUILD 2nd number: 2+4 = 6   
        BUILD 3rd number: 0



        2: 0010
        5: 0000
        6: 0100
        8: 1111

        {0:0, 1:1, 2:1, 3:1}

        4: 0100
        5: 0101
        4: 0100
        7: 0111

        dic = {0: 0, 1:0, 2:2, 3:0}, k=3
        BUILD BIGGESt 1st number: 1+2+4=7
        BUILD BIGGESt 2nd number: 1+4 = 5
        BUILD BIGGESt 3rd number: 4
        BUILD BIGGESt 4th number: 4
        """
        dic = defaultdict(int)
        for n in nums: #O(N)
            bin_rep = bin(n)[2:] 
            length = len(bin_rep)

            for i in range(len(bin_rep)): #O(32)
                if bin_rep[i] == "1":
                    dic[length - i - 1] += 1

        res = 0
        for _ in range(k): #O(K)
            biggest_num = 0
            for key in dic: #O(32)
                if dic[key] > 0:
                    biggest_num += pow(2, key, 10 ** 9 + 7) #O(log(32))
                    dic[key] -= 1

            res += pow(biggest_num, 2, 10 ** 9 + 7)

        return res % (10 ** 9 + 7)

"""
2^32 = ?

2^32 = 4^16 = 8^8 = 16

for _ in range(32): 

for _ in range(log(32)):

"""


