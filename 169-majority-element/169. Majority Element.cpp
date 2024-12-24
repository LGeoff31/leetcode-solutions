class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> dic;
        int majority = nums.size() / 2;
        for (int num: nums) {
            dic[num]++;
            if (dic[num] > majority) return num;
        }
        return -1;
    }
};