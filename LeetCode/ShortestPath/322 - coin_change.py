# BFS
  def coinChange(self, coins: List[int], amount: int) -> int:
      # To track an amount that we have seen
      seen = set()
      cq = deque()
      cq.append((amount, 0))

      while cq:
          target, num = cq.popleft()

          if target == 0:
              return num

          for coin in coins:
              # If we seen an amount, it means there was a combination with less steps(coins)
              if coin <= target and target-coin not in seen:
                  cq.append((target-coin, num+1))
                  seen.add(target-coin)

      return -1
