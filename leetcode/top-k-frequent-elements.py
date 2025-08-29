class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        num_occurence_dict = {}
        final = []

        for idx in range(1, len(nums) + 1):
            freq_dict[idx] = []
        
        for val in nums:
            if (val in num_occurence_dict):
                num_occurence_dict[val] += 1
            else:
                num_occurence_dict[val] = 1
        
        for key in num_occurence_dict:
            freq_dict[num_occurence_dict[key]].append(key)
        
        for key in reversed(freq_dict):
            # print(count < len(freq_dict[key]))
            count = 0
            while count < len(freq_dict[key]) and k > 0:
                final.append(freq_dict[key][count])
                # print(freq_dict[key][count])
                count += 1
                k -= 1
            
            if (k == 0):
                return final

        print(num_occurence_dict)
        print(freq_dict)