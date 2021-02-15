def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        """
        The idea is that we can use the states of the pigs to deduce the ONLY poisonous bucket
        For the base case when we have only 1 round of testing, the pigs can have 2 states: dead or alive
        When we have more than 1 round, the pigs can have (No. of rounds + 1) states: 
        Alive, dead in round 1, dead in round 2, ..., dead in round n
        We can test maximum (No. states of each pig) ** (No. of pigs) buckets
        """
        rounds = minutesToTest//minutesToDie
        
        ans = 0
        while (rounds+1) ** ans < buckets:
            ans += 1
            
        return ans
