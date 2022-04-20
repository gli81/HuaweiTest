# -*- coding: utf-8 -*-

class LastWord:
    def lastWord(self, word: str)-> int:
        ## use rfind()
        # last_space_index = word.rfind(' ')
        return len(word) - word.rfind(' ') - 1
    def lastWord2(self, word:str) -> None:
        ## same algorithm, use stdin
        pass
        
def main():
    test: LastWord = LastWord()
    print(test.lastWord("hello nowcoder"))

if __name__ == '__main__':
    main()