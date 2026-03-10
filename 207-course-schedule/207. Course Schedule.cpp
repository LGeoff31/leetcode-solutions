class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, int> indegree;
        unordered_map<int, vector<int>> graph;

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
                }
            }
        }

        return taken_courses.size() == numCourses;
    }
};