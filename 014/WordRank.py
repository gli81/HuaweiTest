# -*- coding: utf-8 -*-

class WordRank:
    def wordRank(self, words:'list[str]') -> 'list[str]':
        return sorted(words)

def main():
    test = WordRank()
    print(test.wordRank(["cap", "to", "cat", "card", "two", "too", "up", "boat", "boot"]))

if __name__ == '__main__':
    main()