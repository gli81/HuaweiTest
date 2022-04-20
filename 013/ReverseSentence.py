# -*- coding: utf-8 -*-

class ReverseSentence:
	def reverseSentence(self, sentence:'str') -> 'str':
		str_list = sentence.split()
		ans = ""
		for i in range(len(str_list)):
			ans = ans + str_list[len(str_list) - i - 1]
			if i != len(str_list) - 1:
				ans += ' '
		return ans

def main():
	test = ReverseSentence()
	print(test.reverseSentence("I am a boy"))
	print(test.reverseSentence("leetcode"))


if __name__ == '__main__':
	main()