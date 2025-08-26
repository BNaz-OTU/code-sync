class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        nums_freq = {}
        final = []

        for idx in range(1, len(nums) + 1):
            nums_dict[idx] = []
        
        print(nums_dict)
        
        for num in nums: 
            if (num in nums_freq):
                nums_freq[num] += 1
            else:
                nums_freq[num] = 1

        for key in nums_freq:
            nums_dict[nums_freq[key]].append(key)
        
        for key in reversed(nums_dict):
            count = 0

            while (count < len(nums_dict[key])):
                final.append(nums_dict[key][count])

                if (len(final) == k):
                    return final
                
                count += 1
        
        print(nums_dict)