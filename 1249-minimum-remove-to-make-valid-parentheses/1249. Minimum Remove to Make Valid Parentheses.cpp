class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<char> res(s.size(), '\0');
        stack<int> stack;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ')') {
                if (stack.empty()) continue;
                int idx = stack.top();
                stack.pop();
                res[idx] = '(';
                res[i] = ')';
            } else if (s[i] == '(') {
                stack.push(i);
            } else {
                res[i] = s[i];
            }
        }
        string final_res = "";
        for (int i = 0; i < res.size(); i++) {
            if (res[i]) {
                final_res += res[i];
            }
        }
        return final_res;
    }
};