class Solution {
public:
    string bitRep(int n) {
        string res = "";
        while (n > 0) {
            res += to_string(n % 2);
            n/=2;
        }
        std::reverse(res.begin(), res.end());

        return res;
    }

    string reverse(string binRep) {
        string complement = "";
        for (auto c : binRep) {
            if (c == '0') complement += '1';
            else {complement += '0';}
        }
        return complement;
    }
    int binRepValue(string binRep) {
        int res = 0;
        for (int i = binRep.size() - 1; i>= 0; i--) {
            if (binRep[i] == '1') {
                res += pow(2, binRep.size() - i - 1);
            }
        }
        return res;
    }
    int bitwiseComplement(int n) {
        if (n == 0) return 1;
        string binRep = bitRep(n);
        cout << binRep << endl;
        string complement = reverse(binRep);
        cout << complement << endl;
        return binRepValue(complement);
    }
};