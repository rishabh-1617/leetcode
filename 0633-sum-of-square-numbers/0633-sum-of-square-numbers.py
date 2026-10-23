class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(c ** 0.5)

        while left <= right:

            curr = (left*left) + (right*right) # sum of squares of the two pointers
            if curr == c:
                return True
            elif curr < c:
                left += 1 # If curr is less than c, move left pointer right
            else:
                right -= 1 # If curr is greater than c, move right pointer left
        
        return False