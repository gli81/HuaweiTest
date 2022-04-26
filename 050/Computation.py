# -*- coding: utf-8 -*-

class Computation():
    def computationEval(self, com: "str") -> "int":
        com = com.replace('{', '(')
        com = com.replace('[', '(')
        com = com.replace('}', ')')
        com = com.replace(']', ')')
        return int(eval(com))

    def computationStack(self, com: "str") -> "int":
        pare_map = {'}' : '{', ']' : '[', ')' : '('}
        stk_num = []
        stk_op = []
        i = 0
        while i < len(com):
            if com[i].isdigit():
                current = int(com[i])
                i += 1
                ## read a multi-digit number
                for j in range(i, len(com)):
                    if com[j].isdigit():
                        current = current * 10 + int(com[j])
                        i += 1
                    else:
                        break
                stk_num.append(current)
            elif com[i] in "+-*/{[(":
                if com[i] == '-' and (i == 0 or com[i - 1] in "*/{[("): ## deal with neg num
                    stk_num.append(0)
                stk_op.append(com[i])
                i += 1
            else: ## at )]}, do computation within the parenthesis
                ## two temp stacks for + - ops
                temp_stk_num = []
                temp_stk_op = []
                num = stk_num.pop()
                op = stk_op.pop()
                temp_rslt = num
                while op != pare_map[com[i]]:
                    if op in "+-":
                        temp_stk_op.append(op)
                        temp_stk_num.append(temp_rslt)
                        temp_rslt = stk_num.pop()
                    elif op == '*':
                        ## multiplication, do the comp
                        temp_rslt = stk_num.pop() * temp_rslt
                    elif op == '/':
                        temp_rslt = stk_num.pop() / temp_rslt
                    # num = stk_num.pop()
                    op = stk_op.pop()
                '''
                at the end of each while loop, need to update the operation and the num
                but at the end of loop, update op only (get rid of "([{"), so put back one num
                '''
                # stk_num.append(num)
                ## get rid of everything within the parenthesis
                ## remember the +- temp stacks
                while temp_stk_num:
                    if temp_stk_op.pop() == '+':
                        temp_rslt += temp_stk_num.pop()
                    else:
                        temp_rslt -= temp_stk_num.pop()
                ## put the computed result to stk_num
                stk_num.append(temp_rslt)
                ## move to next character
                i += 1
            print(stk_num)
            print(stk_op)
            print()
        ## end of string, possible that some comp from the beginning of the string (before any parenthesis) still at the bottom of stack
        ## do multi / division, put add / minus in temp stack
        temp_stk_num = []
        temp_stk_op = []
        temp_rslt = stk_num.pop()
        while stk_op:
            op = stk_op.pop()
            if op in "+-":
                temp_stk_op.append(op)
                temp_stk_num.append(temp_rslt)
                temp_rslt = stk_num.pop()
            elif op == '*':
                temp_rslt = stk_num.pop() * temp_rslt
            else:
                temp_rslt = stk_num.pop() / temp_rslt
        while temp_stk_num:
            if temp_stk_op.pop() == '+':
                temp_rslt += temp_stk_num.pop()
            else:
                temp_rslt -= temp_stk_num.pop()
        return temp_rslt


            # else:
            #     if com[i] in para_map:
            #         stack_rslt = []
            #         stack_op_this = []
            #         rslt = 0
            #         m = stack_num.pop()
            #         op = stack_op.pop()
            #         while op != para_map[com[i]]:
            #             if op == '*':
            #                 a = stack_num.pop()
            #                 stack_num.append(a * m)
            #             elif op == '/':
            #                 a = stack_num.pop()
            #                 stack_num.append(a / m)
            #             elif op in "+-":
            #                 stack_rslt.append(m)
            #                 stack_op_this.append(op)
            #             m = stack_num.pop()
            #             op = stack_op.pop()
            #         rslt += m
            #         while not stack_op_this:
            #             if stack_op_this.pop() == '+':
            #                 rslt += stack_rslt.pop()
            #             else:
            #                 rslt -= stack_rslt.pop()
            #         stack_num.append(rslt)
            #         i += 1
            #     elif com[i] in "+-*/":
            #         if i == 0 or (com[i - 1] not in ")]}" and not com[i - 1]):
            #             stack_num.append(0)
            #         stack_op.append(com[i])
            #         i += 1
            #     else:
            #         stack_op.append(com[i])
            #         i += 1

def main():
    test = Computation()
    print(test.computationEval("3+2*{1+2*[-4/(8-6)+7]}"))
    print(test.computationStack("3+2*{1+2*[-4/(8-6)+7]}"))

if __name__ == "__main__":
    main()
