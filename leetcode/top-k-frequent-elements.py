class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        num_count_dict = {}
        final = []

        for idx in range(1, len(nums) + 1):
            freq_dict[idx] = []
        
        for val in nums:
            if (val in num_count_dict):
                num_count_dict[val] += 1
            else:
                num_count_dict[val] = 1
        
        for key in num_count_dict:
            freq_dict[num_count_dict[key]].append(key)
        
        for key in reversed(freq_dict):
            count = 0
            while (k > 0 and count < len(freq_dict[key])):
                final.append(freq_dict[key][count])
                count += 1
                k -= 1
            
            if (k == 0):
                return final

        print(num_count_dict)
        print(freq_dict)