class Solution {
public:
    int minimumSum(int n, int k) {
        int sum = 0;
        int i = 1;
        while (n > 0) {
            if (i <= k/2) {
                sum += i;
                i++;
                n--;
            } else {
                break;
            }
        }
        i = 0;
        while (n > 0) {
            sum += k + i;
            i++; 
            n--;
        }

        return sum;
    }
};