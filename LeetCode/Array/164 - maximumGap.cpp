class Bucket {
public:
    bool used = false;
    int minval = numeric_limits<int>::max();
    int maxval = numeric_limits<int>::min();
};

class Solution {
public: 
    int maximumGap(vector<int>& nums) {
        if (nums.empty() || nums.size() < 2)
            return 0;

        int mini = *min_element(nums.begin(), nums.end()),
            maxi = *max_element(nums.begin(), nums.end());

        cout << mini << " " << maxi;

        // Min bucket size = 1
        int bucketSize = max(1, (maxi-mini)/((int)nums.size()-1));
        int bucketNum = (maxi-mini) / bucketSize + 1;

        vector<Bucket> buckets(bucketNum);

        for (auto&& num: nums) {
            int bucketIdx = (num-mini) / bucketSize;
            buckets[bucketIdx].used = true;
            buckets[bucketIdx].minval = min(buckets[bucketIdx].minval, num);
            buckets[bucketIdx].maxval = max(buckets[bucketIdx].maxval, num);
        }

        int prevBucketMax = mini, maxGap = 0;
        for (auto&& bucket: buckets) {
            // Skip if current bucket doesn't contain any number
            if (!bucket.used)
                continue;

            maxGap = max(maxGap, bucket.minval - prevBucketMax);
            prevBucketMax = bucket.maxval;
        }

        return maxGap;
    }
};
