import re

class Solution:
    def strip(self, string):
        regex = re.compile('[^0-9a-zA-Z]')
        string = regex.sub('', string)
        return string.lower()

    def isPalindrome(self, string):
        string = self.strip(string)
        mid = int(len(string)/2)
        for index in range(mid):
            if string[index] != string[len(string) - index - 1]:
                return False
        return True

if __name__ == "__main__":
    assert Solution().isPalindrome("") == True
    assert Solution().isPalindrome("f") == True
    assert Solution().isPalindrome("foo") == False
    assert Solution().isPalindrome("race a car") == False
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True