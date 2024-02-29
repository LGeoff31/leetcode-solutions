class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dic;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (dic.find(complement) != dic.end()) {
                return {dic[complement], i};
            }
            else {
                dic[nums[i]] = i;
            }
        }   
        return {};
    }
};