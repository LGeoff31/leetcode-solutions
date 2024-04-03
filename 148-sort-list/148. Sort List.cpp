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
    ListNode* sortList(ListNode* head) {
        if (!head || !head->next)
            return head;
        
        ListNode* dummy = new ListNode(INT_MIN);
        dummy->next = head;
        
        ListNode* prevSorted = dummy;
        ListNode* currUnsorted = head;
        
        while (currUnsorted) {
            if (currUnsorted->val >= prevSorted->val) {
                prevSorted = prevSorted->next;
                currUnsorted = currUnsorted->next;
            } else {
                ListNode* temp = dummy;
                while (temp->next->val <= currUnsorted->val) {
                    temp = temp->next;
                }
                
                prevSorted->next = currUnsorted->next;
                currUnsorted->next = temp->next;
                temp->next = currUnsorted;
                
                currUnsorted = prevSorted->next;
            }
        }
        
        ListNode* sortedList = dummy->next;
        delete dummy;
        return sortedList;
    }

};