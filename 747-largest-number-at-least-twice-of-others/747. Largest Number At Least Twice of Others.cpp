class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int maxElem = ranges::max(nums);
        int idxMaxElem = find(nums.begin(), nums.end(), maxElem) - nums.begin();
        int secondMaxElem = INT_MIN;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != maxElem) {
                secondMaxElem = max(secondMaxElem, nums[i]);
            }
        }
        return maxElem >= 2*secondMaxElem ? idxMaxElem : -1;
    }
};