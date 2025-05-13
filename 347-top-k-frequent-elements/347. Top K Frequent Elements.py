class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        flat_list = [item for arr in bucket for item in arr]
        print(bucket)
        print(flat_list)

        return flat_list[::-1][:k]