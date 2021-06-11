class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int N = nums.size();
        
        // Prefix sum
        vector<int> psum(N+1, 0);
        for (int i=0; i<N; i++) {
            psum[i+1] = psum[i] + nums[i];
        }
        
        // dp[i][j]: result for spliting nums[:i] to j sub-arrays
        vector<vector<int>> dp(N+1, vector<int>(m+1, INT_MAX));
        dp[0][0] = 0;
        for (int i=1; i<=N; i++) {
            for (int j=1; j<=m; j++) {
                for (int k=0; k<i; k++) {
                    // Split nums[:k] to j-1 sub-arrays, the remaining is nums[k:i]
                    // sum(nums[k:i]) = psum[i] - psum[k]
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], psum[i] - psum[k]));
                }
            }
        }
        
        return dp[N][m];
    }
};
