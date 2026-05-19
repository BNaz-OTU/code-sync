class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0];
        });
        
        vector<vector<int>> final;
        vector<int> prev = intervals[0];

        for (int idx = 1; idx < intervals.size(); idx++) {
            vector<int> interval = intervals[idx];

            if (interval[0] <= prev[1]) {
                if (interval[1] > prev[1]) {
                    prev[1] = interval[1];
                } 
            }

            else {
                final.push_back(prev);
                prev = interval;
            }
        }

        final.push_back(prev);

        cout << final.size() << "\n";

        return final;
        
    }
};