class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        num_dict = {}
        final = []

        for idx in range(len(nums)):
            freq_dict[idx + 1] = []
        
        print(freq_dict)

        for val in nums:
            if (val in num_dict):
                num_dict[val] += 1
            else:
                num_dict[val] = 1
        
        for key in num_dict:
            freq_dict[num_dict[key]].append(key)
        
        count = 0
        for key in reversed(freq_dict):
            while count < k and len(freq_dict[key]) > 0:
                final.append(freq_dict[key].pop())
                count += 1
        
        return final