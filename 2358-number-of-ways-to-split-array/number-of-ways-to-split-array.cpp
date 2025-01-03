class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int n = nums.size();
        int c = 0;
        long long ts = 0, ls = 0;
        for (int num : nums){
            ts += num;
        }
        for (int i = 0; i < n -1; i++){
            ls = ls + nums[i];
            long long rs = ts - ls;
            if (ls >= rs){
                c = c + 1;
            }
        }
        return c;
        
    }
};