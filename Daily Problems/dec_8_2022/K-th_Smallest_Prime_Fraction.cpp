#include<bits/stdc++.h>
using namespace std;


class Solution {
public:
    int helper(float check, vector<int>& arr){
        int left = 0, right = arr.size();
        while(left<right){
            int mid = left + (right-left)/2;
            if(arr[mid]==check){
                return mid;
            }
            else if(arr[mid]>check){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return right;
    }
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        float left = 0, right = 1;
        int n = arr.size();
        while(true){
            float mid = float((float(left)+float(right))/2);
            vector<int> bounds;
            for(int i=0;i<n;i++){
                bounds.emplace_back(helper(float(arr[i])/mid,arr));
            }
            int curr_sum = 0;
            for(auto b:bounds){
                if(b<n) curr_sum += (n-b);
            }
            cout<<curr_sum<<endl;
            if(curr_sum > k){
                right = mid;
            }
            else if(curr_sum < k){
                left = mid;
            }
            else{
                vector<int> ans;
                int a = 0, b = 0;
                float mx = 0;
                for(int i=0;i<bounds.size();i++){
                    if(bounds[i]<n){
                        if(float(arr[i])/float(arr[bounds[i]]) > mx){
                            mx = float(arr[i])/float(arr[bounds[i]]);
                            a = arr[bounds[i]]; b = arr[i];
                        }
                    }
                }
                return {b,a};
            }
        }
        return {};
    }
};