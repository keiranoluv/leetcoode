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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int sz = 0;

        ListNode* cur = head;
        while(cur){
            sz++;
            cur = cur->next;
        }
        if (sz==1)
            return nullptr;
        if (n==sz)
            head = head->next;

        int i=0;
        cur = head;

        while(cur){
            if (i==(sz-1)-n){
                cur->next = cur->next->next;
            }
            i++;
            cur=cur->next;
        }

        cout<<sz;

        return head;
    }
};