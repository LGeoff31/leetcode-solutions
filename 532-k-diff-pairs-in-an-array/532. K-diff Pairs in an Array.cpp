class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int res = 0;
        int complement1 = 0, complement2 = 0;
        map<int, int> dic;
        set<pair<int, int>> visited;
        for (int i = 0; i < nums.size(); i++) {
            complement1 = nums[i] - k;
            complement2 = nums[i] + k;
            if (dic.find(complement1) != dic.end() && visited.find(make_pair(complement1, nums[i])) == visited.end()) {
                res += 1;
                visited.insert(make_pair(complement1, nums[i]));
                visited.insert(make_pair(nums[i], complement1));

                
            }
            if (dic.find(complement2) != dic.end() && visited.find(make_pair(complement2, nums[i])) == visited.end() ) {
                res += 1;
                visited.insert(make_pair(complement2, nums[i]));
                visited.insert(make_pair(nums[i], complement2));

            }
            dic[nums[i]]++;
            cout << res << endl;
        }
        return res;
    }
};