class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
           # for j in range(i + 1, len(nums)):
            #    if nums[i] + nums[j] == target:
             #       return [i, j]
        
        seen = {}  # Stores value: index
    
        for i, num in enumerate(nums):
            complement = target - num
        
        # If we've seen the complement before, we found the pair
            if complement in seen:
                return [seen[complement], i]
            
        # Otherwise, store the current number and its index
            seen[num] = i     