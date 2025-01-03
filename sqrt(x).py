class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = x ** (0.5)
        n = round(res)
        return int(res)
    