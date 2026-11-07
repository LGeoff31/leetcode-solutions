class Solution {
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        using pii = pair<int, int>;
        using tii = tuple<long long, int, int>;

        // {weight, index}
        priority_queue<pii, vector<pii>, greater<>> available;

        // {free_time, weight, index}
        priority_queue<tii, vector<tii>, greater<>> busy;

        for (int i = 0; i < servers.size(); i++) {
            available.push({servers[i], i});
        }
        vector<int> ans(tasks.size());

        long long time = 0;
        for(int j=0; j<tasks.size(); j++) {
            time = max(time, (long long)j);
            // release all servers that have finished
            while(!busy.empty() && get<0>(busy.top()) <= time) {
                auto [freeTime, weight, index] = busy.top();
                busy.pop();
                available.push({weight, index});
            }
            if(available.empty()) {
                time = get<0>(busy.top());
                while(!busy.empty() && get<0>(busy.top()) <= time) {
                    auto [freeTime, weight, index] = busy.top();
                    busy.pop();
                    available.push({weight, index});
                }
            }
            auto [weight, index] = available.top();
            available.pop();
            ans[j] = index;
            busy.push({time + tasks[j], weight, index});
        }
        return ans;
    }
};