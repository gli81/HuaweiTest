# -*- coding: utf-8 -*-

class Vote:
    def vote(self, candidate: "list[str]", v: "list[str]") -> "dict[str, int]":
        pass

def main():
    test = Vote()
    print(test.vote(['A', 'B', 'C', 'D'], ['A', 'D', 'E', "CF", 'A', "GG", 'A', 'B']))

if __name__ == "__main__":
    main()
