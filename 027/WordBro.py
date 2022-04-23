# -*- coding: utf-8 -*-

class WordBro():
	def wordBro(self, line) -> 'list[str]':
		inp = line
		n = inp[0]
		og_word = inp[-2]
		num = inp[-1]
		words = line[1:-2]
		# words[0] = 'changed'
		# print(line)
		# print(n, words, og_word, num)
		ct = 0
		bro_words = []
		for word in words:
			if self.isWordBro(og_word, word):
				ct += 1
				bro_words.append(word)
		if num <= len(bro_words):
			return [str(ct), sorted(bro_words)[num - 1]]
		else: return [str(ct)]
	def isWordBro(self, og_word: 'str', check_word: 'str') -> 'bool':
		return sorted(og_word) == sorted(check_word) and not og_word == check_word

def main():
	test = WordBro()
	print(test.wordBro([3, "abc", "bca", "cab", "abc", 1]))



if __name__ == "__main__":
	main()