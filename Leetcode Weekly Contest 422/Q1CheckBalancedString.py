class Solution:
    def isBalanced(self, num: str) -> bool:
        oddSum, evenSum = 0, 0
        for i in range(len(num)):
            if i%2 == 0:
                evenSum += int(num[i])
            else:
                oddSum += int(num[i])
        return True if evenSum == oddSum else False