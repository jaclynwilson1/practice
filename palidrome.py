class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #palindrome is a number that reads the same forwards and backwards, ex. 121 while 123 is not
        palindrome = False

        if x < 0:
            return False
        else:
            y = len(str(x))
            if y%2 == 0:
                left_side = str(x)[0:y/2]
                left_side = str(left_side)
                print(left_side)
                right_side = str(x)[y/2:y]
                right_side = str(right_side)[::-1]
                print(right_side)
            else:
                left_side = str(x)[0:y//2]
                left_side = str(left_side)
                print(left_side)
                right_side = str(x)[(y//2)+1:y]
                print(right_side)
            if right_side == left_side:
                return True
            else:
                return False