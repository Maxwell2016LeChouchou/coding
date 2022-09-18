// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.


// Definition for singly-linked list
#include <iostream>
#include <vector>
#include <stack>

using namespace std;


struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL){}
};

// struct ListNode{
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr){}
//     ListNode(int x) : val(x), next(nullptr){}
//     ListNode(int x, ListNode *next) : val(x), next(next){}
// };

ListNode* createList(vector<int>& nums){
    ListNode* h = new ListNode(-1);
    ListNode* t;
    t=h;

    for (int i=0; i < nums.size(); i++){
        t->next=new ListNode(nums[i]);
        t=t->next;
    }
    return h->next;
}

void print_list(ListNode *head)
{
    while (head != nullptr)
    {
        std::cout << head->val << " " << std::endl;
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

        int val1, val2, sum;
        int carry=0;

        while(l1||l2){
            if(l1){
                val1=l1->val;
                l1=l1->next;
            }
            else
            {
                val1=0;
            }
            if(l2){
                val2=l2->val;
                l2=l2->next;
            }
            else
            {
                val2=0;
            }
            sum = val1+val2+carry;
            carry = sum/10;

            t->next = new ListNode(sum%10);
            t=t->next;
        }
        if(carry){
            t->next=new ListNode(carry);
        }
        return h->next;
    }
};


// class Solution{
//     public:
//     ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
//         ListNode* dummy = new ListNode(0);
//         ListNode* cur = dummy;
//         int carry = 0;
//         while(l1 != nullptr || l2 != nullptr){
//             int num1 = l1 != nullptr ? l1->val : 0;
//             int num2 = l2 != nullptr ? l2->val : 0;
//             int sum = num1 + num2 + carry;
//             carry = sum / 10;
//             cur -> next = new ListNode(sum % 10);
//             cur = cur -> next;
//             if(l1 != nullptr) l1 = l1 -> next;
//             if(l2 != nullptr) l2 = l2 -> next;
//         }
//         if(carry > 0) cur -> next = new ListNode(carry);
//         return dummy -> next;
//     }
// };


int main()
{
    Solution s;
    vector<int> a1{2,3,4,1};
    ListNode* l1 = createList(a1);

    vector<int> a2{5,6,7};
    ListNode* l2 = createList(a2);

    ListNode* res = s.addTwoNumbers(l1, l2);
    print_list(res);

    return 0;
}