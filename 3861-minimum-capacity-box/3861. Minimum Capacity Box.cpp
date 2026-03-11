class Solution {
public:
    int minimumIndex(vector<int>& capacity, int itemSize) {
        int MinCapacity = INT_MAX;
        int minIndex = -1;

        for (int i = 0; i < (int)capacity.size(); i++) {
            if (capacity[i] >= itemSize && capacity[i] < MinCapacity) {
                MinCapacity = capacity[i];
                minIndex = i;
            }
        }
        return minIndex;
    }
};