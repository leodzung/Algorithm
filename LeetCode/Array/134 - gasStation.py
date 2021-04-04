def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        price = [gas[i]-cost[i] for i in range(N)]
        if sum(price) < 0:
            return -1
        
        # print(price)
        
        i = 0
        curIndex = 0
        curGas = 0
        
        while True:
            print(i, curIndex, curGas)
            if curGas + price[i] < 0:
                curGas = 0
            else:
                if curGas == 0:
                    curIndex = i
                curGas += price[i]
                
            i += 1
            if i == N:
                i = 0
                
            if i == curIndex:
                return curIndex
            
        return -1
