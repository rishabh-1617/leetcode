class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        dig=0
        for i in nums:
            temp=i
            while temp!=0:
                digit=temp%10
                dig+=digit
                temp//=10
        return abs(s-dig)
         