from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 56 ms, faster than 64.89% of Python3 online submissions for Two Sum.
        Memory Usage: 15.5 MB, less than 14.20% of Python3 online submissions for Two Sum.
        """
        # single loop
        # pick up an element from nums
        # if it's in the remains dictionary, match found
        # if not, add remain to the dict as a new possibility

        # O(n)
        remains_dict = {}
        for i in range(len(nums)):
            if nums[i] in remains_dict:
                return [remains_dict[nums[i]], i]
            else:
                remains_dict[target - nums[i]] = i
        pass

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 4296 ms, faster than 10.33% of Python3 online submissions for Two Sum.
        Memory Usage: 15 MB, less than 46.20% of Python3 online submissions for Two Sum.
        """
        # double loop
        # sum up nums[i] + nums[(i+1)] = target?
        # < target -> i + (i++)
        # = target -> return [i, i+1]
        # > target -> i++ -> continue sum up

        # O(n^2)
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]
                addedup = first + second
                if addedup < target:
                    continue  # next j
                elif addedup == target:
                    return [i, j]

        pass
