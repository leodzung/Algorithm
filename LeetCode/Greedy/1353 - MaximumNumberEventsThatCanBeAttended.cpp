class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        priority_queue <int, vector<int>, greater<int>> pq;
        // Sort the events by start day and then end day
        sort(events.begin(), events.end());
        int i = 0, ans = 0, day = 0, N = events.size();
        while(pq.size() > 0 || i < N){
            // Current day is set to the first start day
            if(pq.size() == 0){
                day = events[i][0];
            }
            // Push to heap all the event's end date with the start day smaller or equal to current day
            // Those are the one we can attend
            while(i < N && events[i][0] <= day){
                pq.push(events[i++][1]);
            }
            // Join the event with the lowest end date 
            pq.pop();
            ++ans, ++day;
            // Remove all past event from queue
            while(pq.size() > 0 and pq.top() < day){
                pq.pop();   
            }
        }
        return ans;
    }
};
