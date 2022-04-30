# -*- coding: utf-8 -*-

class Zishou:
    def zishou(self, num):
        ct = 0
        for i in range(num + 1):
            if str(i) == str(i * i)[-len(str(i)):]:
                ct += 1
        return ct

def main():
    test = Zishou()
    print(test.zishou(1))
    print(test.zishou(6))

if __name__ == "__main__":
    main()