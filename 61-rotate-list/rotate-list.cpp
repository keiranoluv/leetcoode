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
    ListNode* rotateRight(ListNode* head, int k) {

        if ((head == nullptr) or (head->next == nullptr) or (k==0)){
            return head;
        }
        int sz = 0;
        ListNode* cur=head;
        while (cur!=nullptr) {
            cur = cur->next;
            sz+=1;
        }
        k = k%sz;
        while (k--) {
            cur = head;
            while(cur->next->next){
                cur=cur->next; 
            }
            ListNode* tmp = cur->next;
            cur->next = nullptr;
            tmp->next = head;
            head = tmp;
        }
        return head;
    }
};