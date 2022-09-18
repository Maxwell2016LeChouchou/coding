#include <iostream>
using namespace std;

void QuickSort(int *a, int low, int high)
{
    if(low > high)
    {
        return;
    }
    int i = low;
    int j = high;
    int key = a[low];
    while(i < j)
    {
        while(a[j] >= key&&i<j)
        {
            j--;
        }
        a[i] = a[j];
        while(a[i] <= key&&i<j)
        {
            i++;
        }
        a[j] = a[i];
    }
    a[i] = key;
    QuickSort(a, low, i-1);
    QuickSort(a, i+1, high);
}

int main()
{
    int a[] = {2,3,1,5,8,6,4,7,9};
    int len = sizeof(a)/sizeof(a[0]);
    QuickSort(a, 0, len-1);
    for (auto x:a){
        cout << x << " ";
    }
    cout << endl;
    return 0;
}