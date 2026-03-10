class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int n : nums) {
            freq[n]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        vector<int> res;
        for (auto [n, f] : freq) {
            if (minHeap.size() < k) {
                minHeap.push({f, n});
            } else {
                if (f > minHeap.top().first) {
                    minHeap.pop();
                    minHeap.push({f, n});
                }
            }
        }
        while (!minHeap.empty()) {
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res; 
    }
};