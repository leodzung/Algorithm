def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Observation: each ugly number is the muliplication of a smaller ugly number with 2, 3, or 5
        ugly = [1]
        # Index of the ugly number that will be muliplied with 2, 3, 5 respectively to generate the next number
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            # The next 3 candidates
            num2, num3, num5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
            # We only care the minimum of the 3, which is the next number
            mn = min(num2, num3, num5)
            
            # Update the index accordingly if the next number is the result of multipling with 2, 3, or 5
            if mn == num2:
                i2 += 1
            if mn == num3:
                i3 += 1
            if mn == num5:
                i5 += 1
                
            ugly.append(mn)
            n -= 1
            
        return ugly[-1]
