class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # frequency count
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # bucket
        bucket = [[] for _ in range(len(nums) + 1)]

        # put numbers according to frequency
        for num, count in freq.items():
            bucket[count].append(num)

        ans = []

        # highest frequency first
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
