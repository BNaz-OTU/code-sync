class Solution:
    def minDeletions(self, s: str) -> int:

        # WRONG
        
        dict_freq = {}
        dict_easy = {}
        count = 0

        # Determine frequency of characters
        for char in s:
            if (char in dict_freq):
                dict_freq[char] += 1
            else:
                dict_freq[char] = 1

        # Setup a dictionary for frequency 
        for idx in range(1, len(s) + 1):
            dict_easy[idx] = []

        # Map the frequency to the character
        for key in dict_freq:
            dict_easy[dict_freq[key]].append(key)

        print(dict_easy)
        for key in range(len(s), 0, -1):
            if (len(dict_easy[key]) >= 2 and key == 1):
                print('here')
                count += len(dict_easy[key]) - 1

            elif (len(dict_easy[key]) >= 2):
                # print('here')
                # dict_easy[key] += dict_easy[key][:1]
                dict_easy[key - 1] += dict_easy[key][1:len(dict_easy[key])]
                count += len(dict_easy[key]) - 1
                dict_easy[key] = dict_easy[key][:1]
            print(dict_easy)
        
        return count
        
        print(dict_freq)
        print(dict_easy[3][1:len(dict_easy[3])])