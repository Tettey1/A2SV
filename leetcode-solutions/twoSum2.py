class Solution:
    def twoSum(self, numbers,target):
        left = 0
        right = len(numbers)-1
        #start from both ends and check if the numbers are less than     # or greater than the target
        while left < right:
            current_sum = numbers[left]+numbers[right]
            if current_sum >target:
                right-=1
            elif current_sum <target:
                left+=1
            else:
                return [left+1,right+1]

        return []    