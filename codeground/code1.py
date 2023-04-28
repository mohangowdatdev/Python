class Solution(object):
    def twoSum(self, nu, target):
        li = []
        for i in range(0, len(nu)):
            for j in range(i, len(nu)):
                if i + j == target:
                    lis.append(i)
                    lis.append(j)
                    print(lis)
                    return lis


obj = Solution()
nums = [5, 6, 7, 8, 9]
lis = obj.twoSum(nums, 13)
print(lis)
