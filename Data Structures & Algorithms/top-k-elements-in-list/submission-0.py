class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countnums = {}
        for i in range(len(nums)) :
            countnums[nums[i]] = 1 + countnums.get(nums[i], 0)
        
        # Sort the dictionary keys based on their values (frequencies) in descending order
        sorted_elements = sorted(countnums.keys(), key=lambda x: countnums[x], reverse=True)
        
        # Return the first k elements
        return sorted_elements[:k]