class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        # går gjennom hash map og tar elementer har verdier deres som er større enn 1
        for key, value in c.items():
            # lagrer keys med verdier
            buckets[value].append(key)

        liste = list()
        for frek in range(len(buckets)-1, 0 , -1):
            for i in buckets[frek]:
                if k == 0:
                    break
                else:
                    liste.append(i)
                    k -= 1

        return liste

           
  
            




        