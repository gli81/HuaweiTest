# -*- coding: utf-8 -*-

class Computation():
    def computationEval(self, com: "str") -> "int":
        com = com.replace('{', '(')
        com = com.replace('[', '(')
        com = com.replace('}', ')')
        com = com.replace(']', ')')
        return int(eval(com))

    def computationStack(self, com: "str") -> "int":
        para_map = {'{' : '}', '[' : ']', '(' : ')'}
        ops = "+-*/"
        stack_num = []
        stack_op = []
        i = 0
        while i < len(com):
            if com[i].isdigit():
                current = com[i]
                i += 1
                for j in range(i, len(com)):
                    if com[j].isdigit():
                        current = current * 10 + com[j]
                        i += 1
                    else:
                        break
                stack_num.append(current)
            else:
                if com[i] in para_map:
                    stack_rslt = []
                    stack_op_this = []
                    rslt = 0
                    m = 



def main():
    test = Computation()
    print(test.computationEval("3+2*{1+2*[-4/(8-6)+7]}"))

if __name__ == "__main__":
    main()
