def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Idea: Use heap to quickly get the smallest ugly number from candidates
        # Generate candidates by multiply the number we have seen with each prime
        
        # Candidates
        nums = [(p, p, 1) for p in primes]
        # Generated numbers
        dp = [1]
        
        for _ in range(n-1):
            dp.append(nums[0][0])
            # There can be multiple identical products - need to update all of them
            while nums[0][0] == dp[-1]:
                num, p, index = heappop(nums)
                # Generate new ugly number
                # Also update the index to point to the next number to multiply
                heappush(nums, (p*dp[index], p, index+1))
                
        return dp[-1]
