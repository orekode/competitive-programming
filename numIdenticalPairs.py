def numIdenticalPairs(self, nums: List[int]) -> int:

    pair_count = 0
    checked = []

    for i in nums:
        count = nums.count(i)
        if count > 1 and checked.count(i) <= 0:
            pair_count += math.factorial(count) / (math.factorial(2) * math.factorial(count - 2))
            checked.append(i)

    return int(pair_count)
