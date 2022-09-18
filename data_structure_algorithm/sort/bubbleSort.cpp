#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int> &n)
{   
    int len = n.size();
    for(int i = 0; i < len; i++)
    {
        for(int j = i+1; j < len; j++)
        {
            if(n[i] > n[j])
            {
                int temp = n[j];
                n[j] = n[i];
                n[i] = temp;
            }
        }
    }
}

int main()
{
    vector<int> n = {4,1,7,3,5,9};
    bubbleSort(n);
    for (auto x : n)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}