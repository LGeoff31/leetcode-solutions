/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int getLength(const ListNode* root) {
        int size = 0;;
        while (root) {
            root = root->next;
            size++;
        }
        return size;
    }
    ListNode* swapNodes(ListNode* head, int k) {
        int n = getLength(head);
        if (n == 1) return head;
        ListNode* a = nullptr;
        ListNode* b = nullptr;
        ListNode* curr = head;
        cout << n-k << endl;
        for (int i = 0; i < n; i++) {
            if (i == k-1) {
                a = curr;
            }  
            if (i == n-k) {
                cout << "reached" << endl;
                b = curr;
            }
            curr = curr->next;
        }
        int temp = a->val;
        cout << b->val << "bitch" << endl;
        a->val = b->val;
        b->val = temp;
        return head;
    }
};