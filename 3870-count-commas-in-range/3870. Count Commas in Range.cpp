class Solution {
public:
    int countCommas(int n) {
        // every 1000 is 1
        // 10k is 1
        // 100k  is 1
        // 1M is 2
        // 1B is 3

        // dumb just brute force.
        //100,000
        if (n < 1000) return 0;
        return n - 999;
    }
};