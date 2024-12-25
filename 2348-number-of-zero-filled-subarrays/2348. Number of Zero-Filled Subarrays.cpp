class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long res = 0;
        int l = 0, r = 0;
        vector<int> zeros;
        while (r < nums.size()) {
            int count = 0;
            while (r < nums.size() && nums[r] == 0) {
                r++;
                count++;
                if (r < nums.size() && nums[r] != 0) {
                    r--;
                    break;
                }
            }
            r++;
            if (count != 0) zeros.push_back(count);
        }
        for (long long num: zeros) {
            res += num * (num+1) / 2;
        }

        return res;
    }
};