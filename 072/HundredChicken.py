# -*- coding: utf-8 -*-

class HundredChicken:
    def hundredChicken(self):
        for i in range(21):
            for j in range(34):
                if 5 * i + 3 * j + (100 - i - j) / 3 == 100:
                    print(f"{i} {j} {100 - i - j}")

def main():
    test = HundredChicken()
    test.hundredChicken()

if __name__ == "__main__":
    main()