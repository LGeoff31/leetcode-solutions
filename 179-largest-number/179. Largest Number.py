class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        array = list(map(str, nums))
        
        array.sort(key=lambda x: x*10, reverse=True)
        print(array)
        if array[0] == "0":
            return "0"
        
        largest = ''.join(array)
        
        return largest