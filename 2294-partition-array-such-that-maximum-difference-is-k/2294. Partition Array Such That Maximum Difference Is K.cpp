class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int minElem = nums[0];
        int cnt = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] - minElem > k) {
                cnt++;
                minElem = nums[i];
            }
        }
        return cnt;
    }
};