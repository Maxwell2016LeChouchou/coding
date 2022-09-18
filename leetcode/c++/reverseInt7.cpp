#include <iostream>
using namespace std;

int reverse(int x)
{
    int rev = 0;
    while (x != 0)
    {
        if (rev < INT_MIN/10 || rev > INT_MAX/10)
        {
            return 0;
        }
        int digit = x % 10;
        cout << "digit: " << digit << endl;
        x /= 10;
        cout << "x: " << x << endl;
        rev = rev * 10 + digit;
        cout << "rev: " << rev << endl;
        
    }
    return rev;
}

int main()
{
    int a;
    cout << " Please input a number: " << endl;
    cin >> a;
    int rev = reverse(a);
    cout << "reverse: " << rev << endl;
    return 0;
}