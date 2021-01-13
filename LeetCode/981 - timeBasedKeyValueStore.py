class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Map for keys and values
        self.kmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If this is the first time we see the key, initiate the values as an array of tuple (timestamp, value)
        if key not in self.kmap:
            self.kmap[key] = [(timestamp, value)]
            
        else:
            # Check if value is the same as last added value
            ts, val = self.kmap[key][-1]
            
            # If it is the same as the last added value, just modify the last timestamp to the current timestamp
            if val == value:
                self.kmap[key][-1] = (timestamp, val)
            
            # Else, add the new (timestamp, value) tuple
            else:
                self.kmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # print(self.kmap[key][::-1])
        
        # Reverse the array to start from the latest timestamp
        for (ts, val) in self.kmap[key][::-1]:
            
            # Found the timestamp, return value
            if ts <= timestamp:
                return val
            
        # If there is no timestamp (thus, no value), return ""
        return ""
