#include <iostream>
#include <vector>
using namespace std;

void insertSort(int a[], int n)
{
    for(int i = 1; i < n; i++)
    {
        for (int j = i; j >=1; j--)
        {
            if(a[j] < a[j-1])
            {
                int temp = a[j];
                a[j] = a[j-1];
                a[j-1] = temp;
            }
            else
            {
                break;
            }
            
        }
    }
}

int main()
{
    int a[] = {2,1,4,3,6};
    int len = sizeof(a)/sizeof(a[0]);
    insertSort(a, len);
    for(int i = 0; i < len; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;

}

// time complexity: O(n^2)