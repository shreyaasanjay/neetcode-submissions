class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while numbers[left]+numbers[right]!=target:
            if numbers[left]+numbers[right]>target:
                right=right-1
            else:
                #we are doing left=left+1 because if it is less than target than then we know that even the smallest value with the largest value can't reach target so the smallest value cant be in the sum 
               left=left+1
        return [left+1,right+1]
