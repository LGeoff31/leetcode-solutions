class Solution {
public:
    int maxDistance(string moves) {
        int x=0, y=0, extra=0;
        for (char m : moves) {
            if (m == 'U') x++;
            if (m == 'D') x--;
            if (m == 'L') y--;
            if (m == 'R') y++;
            if (m == '_') extra++;
        }
        return abs(x) + abs(y) + extra;
    }
};