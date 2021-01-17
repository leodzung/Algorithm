class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            val, ts = self.store[key][-1]
            if val == value:
                self.store[key][-1] = (value, timestamp)
            else:
                self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        def binarySearch(value, array, start, end) -> int:
            if start >= end:
                return end if value >= array[end] else end - 1

            mid = (start + end) // 2
            if value > array[mid]:
                return binarySearch(value, array, mid + 1, end)
            elif value < array[mid]:
                return binarySearch(value, array, start, mid - 1)
            else:
                return mid

        times = [item[1] for item in self.store[key]]
        pos = binarySearch(timestamp, times, 0, len(times) - 1)
        # print(self.store[key], pos)
        return self.store[key][pos][0] if pos >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
