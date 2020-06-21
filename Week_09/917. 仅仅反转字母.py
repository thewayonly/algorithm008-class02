class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        front, end = 0, len(S) - 1
        while front < end:
            if not S[front].isalpha():
                front += 1
            elif not S[end].isalpha():
                end -= 1
            else:
                S[front], S[end] = S[end], S[front]
                front += 1
                end -= 1
        return "".join(S)
