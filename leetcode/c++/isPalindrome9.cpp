#include <iostream>
using namespace std;

bool isPalindrome(int x)
{
    int rev = 0;
    if (x < 0 || x % 10 == 0 && x != 0)
    {
        return false;
    }
    while(x > rev)
    {
        int digit = x % 10;
        rev = rev * 10 + digit;
        x /= 10;
    }
    return x == rev || x == rev/10;
}

int main()
{
    int x;
    cout << "Please enter an intger" << endl;
    cin >> x; 
    bool res = isPalindrome(x);
    if (res)
    {
        cout << "true" << endl;
    }
    else
    {
        cout << "false" << endl;
    }
    return 0;
}