class Solution(object):
    def is_palin(self, s):
        print(s)
        if len(s) % 2 != 0:  # odd
            for i in range(0,int(len(s) / 2)):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        else:
            for i in range(0,int(len(s) / 2)):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True

    def longestPalindrome(self, s):
        le = len(s)
        if le == 0:
            return 0
        elif le == 1:
            return 1
        for l in range(le, 0, -1):
            for sub_c in range(0, le - l + 1):
                if self.is_palin(s[sub_c:sub_c + l]):
                    return s[sub_c:sub_c + l]


