# -*- coding: utf-8 -*-

import string

class StrEncode():
    def strEncode(self, key: 'str', line: 'str') -> 'str':
        ## build the two encode dictionaries
        lower_dict = []
        for char in key:
            if char.isalpha() and char.lower() not in lower_dict:
                lower_dict.append(char.lower())
        for char in string.ascii_lowercase:
            if char not in lower_dict:
                lower_dict.append(char)
        lower_dict = ''.join(lower_dict)
        # print(lower_dict)
        ## build the encoded string
        ans = ''
        for char in line:
            if char.islower():
                ans += lower_dict[ord(char) - 97]
            elif char.isupper():
                ans += lower_dict[ord(char.lower()) - 97].upper()
            else:
                ans += char
        return ans
def main():
    test = StrEncode()
    print(test.strEncode("nihao", "ni"))
    print(test.strEncode("TRAILBLAZERS", "Attack AT DAWN"))

if __name__ == "__main__":
    main()
