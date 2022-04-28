# -*- coding: utf-8 -*-

class Cursor:
    def cursor(self, num: "int", ops: "str") -> "tuple[list[int], int]":
        cur = 1
        ce = 1
        for char in ops:
            if char == 'U':
                cur -= 1
                if ce == cur + 1:
                    ce -= 1
                    if ce == 0:
                        ce = num - 3
            else:
                cur += 1
                if ce == cur - 4:
                    ce += 1
                    if ce == num - 2:
                        ce = 1
            if cur <= 0:
                cur += num
            if cur > num:
                cur -= num
            if ce <= 0:
                ce += num
            if ce > num:
                ce -= num
        ans_list = [ce, ce + 1, ce  +2, ce + 3]
        if num <= 4:
            ans_list = [x + 1 for x in range(num)]
        return ans_list, cur

def main():
    test = Cursor()
    print(test.cursor(10, "UUUU"))
    print(test.cursor(10, "DDDDD"))
    print(test.cursor(10, "DDDDDUU"))
    print(test.cursor(4, "DDDDD"))
    print(test.cursor(8, "UDUUDDDUDUUUDDUDUDUUDUDUUDDDUUDUDDDU"))
    print(test.cursor(2, "DUDUDDUUDUDDDDUDUDDDUUDDUDDUDUDUDDDUDUDUUDDUUDDUUUDUDUUUDDUDUDDUUDUDDDDUDUDUUDUDDDDDUU"))

if __name__ == "__main__":
    main()
