class Solution {
public:
    void printLst(vector<int> lst) {
        for (int num : lst) {
            cout << num << endl;
        }
    }
    int findLonelyPixel(vector<vector<char>>& picture) {
        // O(rc * (r+c))
        // Precomputation -> O(rc)
        vector<int> columnsLst;
        vector<int> rowsLst;
        int rows = picture.size(), cols = picture[0].size();
        // fill out columnsLst
        for (int c = 0; c < cols; c++) {
            int count = 0;
            for (int r = 0; r < rows; r++) {
                if (picture[r][c] == 'B') count++;
            }
            columnsLst.push_back(count);
        }
        for (int r = 0; r < rows; r++) {
            int count = 0;
            for (int c = 0; c < cols; c++) {
                if (picture[r][c] == 'B') count++;
            }
            rowsLst.push_back(count);
        }
        int res = 0;
        for (int r=0;r<rows;r++){
            for(int c=0;c<cols;c++){
                if (picture[r][c] == 'B') {
                    if (columnsLst[c] == 1 && rowsLst[r] == 1) {
                        res++;
                    }
                }
            }
        }
        printLst(columnsLst);
        return res;
    }
};