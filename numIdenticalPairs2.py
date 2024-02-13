def numIdenticalPairs(self, nums: List[int]) -> int:

      size = len(nums)

      pairs = 0

      for i in range(size):

          outer = nums[i]

          for j in range(size):

              inner = nums[j]

              if outer == inner and i < j:

                  pairs += 1
      
      return pairs
