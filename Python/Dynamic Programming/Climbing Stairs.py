class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        level = [0]*(n+1)
        level[1] , level[2] = 1 , 2
        for i in range(3,n+1):
            level[i] = level[i-1] + level[i-2]
        return level[n]
