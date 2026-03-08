class Solution {
public:
    string integerToBinary(int number, int n) {
        string binaryRep = bitset<32>(number).to_string();
        return binaryRep.substr(binaryRep.size() - n);
    }
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums[0].size();
        int maxVal = (1 << (n)) - 1;
        for (int i = 0; i <= maxVal; i++) {
            string s = integerToBinary(i, n);
            if (find(nums.begin(), nums.end(), s) == nums.end()) {
                return s;
            }
        }
        return "";
    }
};