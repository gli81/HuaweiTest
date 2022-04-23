# -*- coding: utf-8 -*-

class StrEncode():
    def encode(self, og: 'str') -> 'str':
        ans = ''
        for char in og:
            if ord(char) in range(97, 122):
                ans += chr(ord(char) - 31)
            elif char == 'z':
                ans += 'A'
            elif ord(char) in range(65, 90):
                ans += chr(ord(char) + 33)
            elif char == 'Z':
                ans += 'a'
            elif ord(char) in range(48, 57):
                ans += chr(ord(char) + 1)
            elif char == '9':
                ans += '0'
        return ans

    def decode(self, encoded: 'str') -> 'str':
        ans = ''
        for char in encoded:
            if ord(char) in range(66, 91):
                ans += chr(ord(char) + 31)
            elif char == 'A':
                ans += 'z'
            elif ord(char) in range(98, 123):
                ans += chr(ord(char) - 33)
            elif char == 'a':
                ans += 'Z'
            elif ord(char) in range(49, 58):
                ans += chr(ord(char) - 1)
            elif char == '0':
                ans += '9'
        return ans

def main():
    test = StrEncode()
    print(test.encode("abcdefgz0129"))
    print(test.decode("BCDEFGHA1230"))
    print(test.encode("2OA92AptLq5G1lW8564qC4nKMjv8C"))
    print(test.decode("B5WWIj56vu72GzRja7j5"))

if __name__ == "__main__":
    main()