#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
 
int main()
{
    // Create a vector containing integers
    vector<int> v = {7, 5, 16, 8};
 
    // Add two more integers to vector
    v.push_back(25);
    v.push_back(13);
 
    // Iterate and print values of vector
    for(int n : v) {
        // cout << n << '\n';
    }

	vector<pair<int, int>> obj(2);
    for(pair<int, int> n : obj) {
        cout << n.first << '\n';
        cout << n.second << '\n';
    }

    int m = 2;
    int k = 3;
    cout << '\n';
    vector<vector<int>> vv(m + 1, vector<int>(k + 1));
    cout << vv.size() << '\n';

    cout << '\n';
    for(vector<int> a : vv) {
        cout << a.size() << '\n';
    }

}
