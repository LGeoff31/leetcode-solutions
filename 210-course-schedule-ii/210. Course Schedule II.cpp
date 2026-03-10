class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, int> indegree;
        unordered_map<int, vector<int>> graph;
        vector<int> ordering;

        for (auto& arr : prerequisites) {
            int course = arr[0], preq = arr[1];
            graph[preq].push_back(course);
            indegree[course]++;
        }
        cout << "reached" << endl;
        queue<int> q;
        unordered_set<int> taken_courses;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                taken_courses.insert(i);
                ordering.push_back(i);
            }
        }

        while (!q.empty()) {
            int course = q.front();
            q.pop();
            for (auto& nei : graph[course]) {
                indegree[nei]--;
                if (indegree[nei] == 0) {
                    q.push(nei);
                    taken_courses.insert(nei);
                    ordering.push_back(nei);
                }
            }
        }

        return taken_courses.size() == numCourses ? ordering : vector<int>{};
    }
};