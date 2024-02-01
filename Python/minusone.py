class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = 0
        while True:
            if digits[-1] < 9:
                digits[-1] = digits[-1] + 1
            else:
                digits[-2] = 0
                x = x-1

        return digits
