class Solution {
    public String processStr(String s) {
        StringBuilder res = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (Character.isLowerCase(c)) {
                res.append(c);
            } 
            else if (c == '*') {
                if (res.length() > 0) {
                    res.deleteCharAt(res.length() - 1);
                }
            } 
            else if (c == '#') {
                String copy = res.toString();
                res.append(copy);
            } 
            else if (c == '%') {
                res.reverse();
            }
        }

        return res.toString();
    }
}