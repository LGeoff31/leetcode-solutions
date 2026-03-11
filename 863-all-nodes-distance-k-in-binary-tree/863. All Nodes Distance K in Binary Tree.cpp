/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    struct KeyHash {
        size_t operator()(const TreeNode* t) const {
            return hash<int>()(t->val);
        }
    };
    void dfs(TreeNode* node, unordered_map<TreeNode*, vector<TreeNode*>, KeyHash>& graph) {
        if (node == nullptr) return;
        if (node->left) {
            graph[node].push_back(node->left);
            graph[node->left].push_back(node);
            dfs(node->left, graph);
        }
        if (node->right) {
            graph[node].push_back(node->right);
            graph[node->right].push_back(node);
            dfs(node->right, graph);
        }
    }
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        unordered_map<TreeNode*, vector<TreeNode*>, KeyHash> graph;
        dfs(root, graph);
        queue<TreeNode*> q;
        q.push(target);
        unordered_set<TreeNode*> seen;
        int steps = 0;
        vector<int> res;
        seen.insert(target);
        while (!q.empty()) {
            int q_size = q.size();
            for (int i = 0; i < q_size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (steps == k) {
                    res.push_back(node->val);
                    continue;
                }
                for (auto nei : graph[node]) {
                    if (!seen.count(nei)) {
                        seen.insert(nei);
                        q.push(nei);
                    }
                }
            }
            steps++;
        }
        return res;
    }
};