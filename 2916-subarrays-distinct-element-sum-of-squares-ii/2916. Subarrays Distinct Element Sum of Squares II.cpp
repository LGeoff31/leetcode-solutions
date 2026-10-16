class Solution {
    static constexpr long long MOD = 1'000'000'007LL;

    struct Node {
        long long sum = 0;
        long long sq = 0;
        long long lazy = 0;
    };

    class SegTree {
        int n;
        vector<Node> tree;

        void apply(int node, int l, int r, long long v) {
            long long len = r - l + 1;

            tree[node].sq = (
                tree[node].sq
                + 2LL * v % MOD * tree[node].sum % MOD
                + len % MOD * v % MOD * v % MOD
            ) % MOD;

            tree[node].sum = (
                tree[node].sum + len * v
            ) % MOD;

            tree[node].lazy = (
                tree[node].lazy + v
            ) % MOD;
        }

        void push(int node, int l, int r) {
            if (tree[node].lazy == 0 || l == r)
                return;

            int mid = l + (r - l) / 2;
            long long v = tree[node].lazy;

            apply(node * 2, l, mid, v);
            apply(node * 2 + 1, mid + 1, r, v);

            tree[node].lazy = 0;
        }

        void update(int node, int l, int r,
                    int ql, int qr) {
            if (ql <= l && r <= qr) {
                apply(node, l, r, 1);
                return;
            }

            push(node, l, r);

            int mid = l + (r - l) / 2;

            if (ql <= mid)
                update(node * 2, l, mid, ql, qr);

            if (qr > mid)
                update(node * 2 + 1, mid + 1, r, ql, qr);

            tree[node].sum = (
                tree[node * 2].sum +
                tree[node * 2 + 1].sum
            ) % MOD;

            tree[node].sq = (
                tree[node * 2].sq +
                tree[node * 2 + 1].sq
            ) % MOD;
        }

    public:
        SegTree(int n) : n(n), tree(4 * n) {}

        void update(int l, int r) {
            if (l <= r)
                update(1, 0, n - 1, l, r);
        }

        long long getSquares() {
            return tree[1].sq;
        }
    };

public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();

        SegTree st(n);
        unordered_map<int, int> last;

        long long ans = 0;

        for (int r = 0; r < n; r++) {
            int x = nums[r];

            int l = last.count(x) ? last[x] + 1 : 0;

            st.update(l, r);

            last[x] = r;

            ans = (ans + st.getSquares()) % MOD;
        }

        return (int)ans;
    }
};