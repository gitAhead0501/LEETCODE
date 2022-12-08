#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> max_per_col(n, 0), max_per_row(n, 0);
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                max_per_row[i] = max(max_per_row[i], grid[i][j]);
                max_per_col[j] = max(max_per_col[j], grid[i][j]);
            }
        }
        int ans = 0;
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                ans += min(max_per_row[i], max_per_col[j]) - grid[i][j];
        return ans;
    }
};