class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> stack;
        for (auto& arr : intervals) {
            int s = arr[0], e = arr[1];
            if (stack.empty()) {
                stack.push_back({s, e});
                continue;
            }
            if (s <= stack[stack.size() - 1][1]) {
                stack[stack.size() - 1] = {stack[stack.size() - 1][0], max(stack[stack.size() - 1][1], e)};
            } else {
                stack.push_back({s, e});
            }
        }
        return stack;
    }
};