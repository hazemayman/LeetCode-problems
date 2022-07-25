class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        std::vector<int>::iterator low,up;
        low = lower_bound(nums.begin() , nums.end() , target);
        up = upper_bound(nums.begin() , nums.end() , target);
        int first = low - nums.begin();
        int last = up - nums.begin()-1;
        if(low == up && (first >= nums.size() || nums[first] != target)) return {-1 , -1};
       

        return {first , last};
    }
};