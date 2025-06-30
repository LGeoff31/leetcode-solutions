class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        for (int i = 0; i < nums.size(); i++) {
            hashmap[nums[i]]++;
        }
        int res = 0;
        for (auto&[key,value] : hashmap) {
            if (hashmap.count(key+1)) {
                res = max(res, hashmap[key] + hashmap[key+1]);
            }
            if (hashmap.count(key-1)) {
                res = max(res, hashmap[key] + hashmap[key-1]);
            }
        }
        return res;
    }
};