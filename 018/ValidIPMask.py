# -*- coding: utf-8 -*-

class ValidIPMask():
    def validIPMask(self, line: 'str') -> 'str':
        ans = ''
        ## split, get IP and mask
        [ip, mask] = line.split('~')
        try:
            ip = list(map(int, ip.split('.')))
            mask = list(map(int, mask.split('.')))
            mask_str = ''.join(list(map(self.decimal2Binary, mask)))
            # print(ip)
            # print(self.validMask(mask_str))
            ## do nothing category
            if ip[0] in [0, 127]:
                ans = ''
            elif self.validMask(mask_str):
                ## valid mask, check IP then
                ## category A
                if ip[0] in range(1, 127):
                    ans = 'A'
                elif ip[0] in range(128, 192):
                    ans = 'B'
                elif ip[0] in range(192, 224):
                    ans = 'C'
                elif ip[0] in range(224, 240):
                    ans = 'D'
                elif ip[0] in range(240, 256):
                    ans = 'E'
                if ip[0] == 10:
                    ans += " + private"
                if ip[0] == 172 and ip[1] in range(16, 32):
                    ans += " + private"
                if ip[0] == 192 and ip[1] == 168:
                    ans += " + private"
            else:
                ans = "invalid"
        except:
            ans = "invalid"
        return ans

    def decimal2Binary(self, num: 'int') -> 'str':
        ans = ''
        if num == 0: return "00000000"
        while num > 0:
            if num % 2 == 1:
                ans += '1'
            else:
                ans += '0'
            num = num // 2
        return '0' * (8-len(ans)) + ans[::-1]
    def validMask(self, mask: 'str') -> 'bool':
        if mask[0] == '0': return False
        first_zero_index = -1
        for i in range(len(mask)):
            if mask[i] == '0':
                first_zero_index = i
                break
        if first_zero_index == -1: return False
        for char in mask[first_zero_index + 1 : len(mask)]:
            if char == '1': return False
        return True

def main():
    test = ValidIPMask()
    print("===== test case 1 =====")
    print("10.70.44.68~255.254.255.0" + " result: " + test.validIPMask("10.70.44.68~255.254.255.0"))
    print("1.0.0.1~255.0.0.0" + " result: " + test.validIPMask("1.0.0.1~255.0.0.0"))
    print("192.168.0.2~255.255.255.0" + " result: " + test.validIPMask("192.168.0.2~255.255.255.0"))
    print("19..0.~255.255.255.0" + " result: " + test.validIPMask("19..0.~255.255.255.0"))
    # print(test.decimal2Binary(64))
    # print(test.decimal2Binary(66))
    # print(test.decimal2Binary(22))
    # print(test.decimal2Binary(88))
    print("===== test case 2 =====")
    print(test.validIPMask("0.201.56.50~255.255.111.255"))
    print(test.validIPMask("127.201.56.50~255.255.111.255"))
    # print(test.decimal2Binary(64 ^ 66))
    # print(test.validMask("11111111111111111111111100000000"))

if __name__ == "__main__":
    main()