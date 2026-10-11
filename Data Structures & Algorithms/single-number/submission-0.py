class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # target is the number that does not have a duplicate
        c = Counter(nums)
        for k, v in c.items():
            if v == 1:
                return k



        