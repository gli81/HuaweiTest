# -*- coding: utf-8 -*-

class DeleteChar():
    def deleteChar(self, line: 'str') -> 'str':
        char_map = {}
        for char in line:
            if char in char_map: char_map[char] += 1
            else: char_map[char] = 1
        min_apperance = min(char_map.values())
        ans = ""
        for char in line:
            if char_map[char] != min_apperance:
                ans += char
        return ans


def main():
    test = DeleteChar()
    print(test.deleteChar("aabcddd"))
    print(test.deleteChar("aabcddde"))

if __name__ == "__main__":
    main()