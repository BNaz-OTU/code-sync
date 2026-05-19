#include <algorithm>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int buy = prices[0];

        for (int idx = 1; idx < prices.size(); idx++) {
            int sell = prices[idx];

            if (buy > sell) {
                buy = sell;
                continue;
            }

            profit = std::max(profit, sell - buy);
        }

        return profit;
    }
};