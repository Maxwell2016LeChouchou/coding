#include <iostream>
#include <stack>
#include <vector>

using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr){}
    ListNode(int x): val(x), next(nullptr){}
    ListNode(int x, ListNode *next): val(x), next(next){}
};

ListNode* createList(vector<int>& nums){
    ListNode* h = new ListNode(-1);
    ListNode* t;
    t = h;

    for(int i = 0; i < nums.size(); i++){
        t->next = new ListNode(nums[i]);
        t = t->next;
    }
    return h->next;
}


void print_list(ListNode *head)
{
    while(head != nullptr){
        std::cout << head -> val << " " << std::endl;
        head = head->next;
    }
    std::cout << " " << std::endl;
}

class Solution{
    public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
        ListNode* h = new ListNode(-1);
        ListNode* t;
        t = h;
        int carry = 0;
        while (l1 != nullptr || l2 != nullptr){
            int num1 = l1 != nullptr ? l1->val : 0;
            int num2 = l2 != nullptr ? l2->val : 0;

            int sum = num1 + num2 + carry;

            carry = sum / 10;
            t -> next = new ListNode(sum % 10);

            t = t -> next;
            if(l1 != nullptr) l1 = l1 -> next;
            if(l2 != nullptr) l2 = l2 -> next;

        }
        if(carry > 0) t -> next = new ListNode(carry);
        return h -> next;
    }
};


int main(){
    Solution sol;
    vector<int> a{1, 2, 3};
    ListNode* l1 = createList(a);

    vector<int> b{4, 5, 6};
    ListNode* l2 = createList(b);

    ListNode* res = sol.addTwoNumbers(l1, l2);
    print_list(res);

    return 0;
}