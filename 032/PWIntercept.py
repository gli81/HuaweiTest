# -*- coding: utf-8 -*-

class PWIntercept():
    def pWIntercept(self, pw: 'str') -> 'int':
        ans = 0
        for i in range(len(pw)):
            len1 = self.palindromeCenteredAt(pw, i, i)
            len2 = self.palindromeCenteredAt(pw, i, i + 1)
            length = max(len1, len2)
            if length > ans:
                ans = length
        return ans
        
    def palindromeCenteredAt(self, s: 'str', leftIndex: 'int', rightIndex: 'int') -> 'int':
        '''
        LeetCode 005
        '''
        left = leftIndex
        right = rightIndex
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 2 + 1


def main():
    test = PWIntercept()
    print(test.pWIntercept("ABBA"))
    print(test.pWIntercept("ABBBA"))

if __name__ == "__main__":
    main()

