class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*
        int (32 bits) -> -2e9 - 2e9
        long long (64 bits) -> -9e18 - 9e18
        double -> floating point
        float -> less precision

        length(array) = array.length
        length(string) = string.size()
        array<str,5>
        pair<int, int>
        unordered_map<K,V>
        map<K,V>
        unordered_set<T>, set<T>
        queue<T>
        deque<T>
        stack<T>
        priority_queue<T>
        INT_MIN
        INT_MAX
        size_t -> unsighted
        */
        int min_stock = INT_MAX;
        int max_profit = 0;
        for (auto p : prices) {
            max_profit = max(max_profit, p - min_stock);
            min_stock = min(min_stock, p);
        }
        return max_profit;
    }
};