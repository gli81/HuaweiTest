# -*- coding: utf-8 -*-

class ValidIP:
    def validIP(self, ip: "str") -> "bool":
        seg = ip.split(".")
        if len(seg) != 4:
            return False
        for i in seg:
            if not i.isdigit():
                return False
            if int(i) > 255 or (i.startswith('0') and len(i) > 1):
                return False
        return True

def main():
    test = ValidIP()
    print(test.validIP("255.255.255.1000"))
    print(test.validIP("255.255.255.100"))

if __name__ == "__main__":
    main()