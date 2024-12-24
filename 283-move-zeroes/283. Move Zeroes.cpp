class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> lst;
        for (int num: nums) {
            if (num != 0) {
                lst.push_back(num);
            }
        }
        for (int num: nums) {
            if (num == 0) {
                lst.push_back(num);
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            nums[i] = lst[i];
        }
    }
};