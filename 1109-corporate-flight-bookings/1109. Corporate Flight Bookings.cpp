class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> r(n+1, 0);
        int a, b, c;
        for (int i = 0; i < bookings.size(); i++) {
            a = bookings[i][0];
            b = bookings[i][1];
            c = bookings[i][2];
            r[a - 1] += c;
            r[b] -= c;
        }
        cout << r[1] << endl;
        int curr = 0;
        for (int i = 0; i < n; i++) {
            curr += r[i];
            r[i] = curr;
        }
        r.pop_back();
        return r;
    }
};