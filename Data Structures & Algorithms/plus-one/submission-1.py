class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits [-1] = digits[-1] + 1
        result = []
        ndigits = digits[::-1]

        for i in range(len(digits)-1):
            if ndigits[i]>9:
                ndigits[i]=ndigits[i]-10
                ndigits[i+1]+=1
        if ndigits[-1]==10:
            ndigits[-1]-=10
            ndigits.append(1)
        return ndigits[::-1]