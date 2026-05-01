# LC 53 - Maximum Subarray
# Difficulty: Medium
# Pattern: Kadane's Algorithm
# Time: O(n) 
# Space: O(1)

nums =[-2, 1, -3, 4, -1, 2, 1, -5, 4]

 # start with first element as both our current and best sum
 # we use nums[0] not 0 because array could be all negative
current_sum = nums[0]
max_sum = nums[0]

# start from index 1 since index 0 is already our starting point
for i in range(1, len(nums)):

# decision: extend current subarray OR restart fresh from here?
# if nums[i] alone is better than adding it to current → restart
    current_sum = max(nums[i], current_sum + nums[i])

# is this the best sum we've seen so far?
    max_sum = max(max_sum, current_sum)

print(max_sum)