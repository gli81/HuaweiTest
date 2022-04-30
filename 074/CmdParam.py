# -*- coding: utf-8 -*-

class CmdParam:
    def cmdParam(self, cmd: "str"):
        # print(cmd.split("\""))
        ct = 0
        ans = []
        cmds = cmd.split("\"")
        if len(cmds) != 1:
            for c in range(len(cmds)):
                if c % 2 == 1 and cmds[c] != '':
                    ct += 1
                    ans.append(cmds[c])
                elif c % 2 == 0 and cmds[c] != '':
                    splits = cmds[c].split(" ")
                    for item in splits:
                        if item != '':
                            ct += 1
                            ans.append(item)
        else:
            splits = cmd.split(" ")
            for item in splits:
                if item != '':
                    ct += 1
                    ans.append(item)
        print(ct)
        print(ans)


def main():
    test = CmdParam()
    print("xcopy /s \"C:\\\\program files\" \"d:\\\"")
    test.cmdParam("xcopy /s \"C:\\\\program files\" \"d:\\\"")
    print("xcopy /s \"C:\\\\program files\" /s \"d:\\\"")
    test.cmdParam("xcopy /s \"C:\\\\program files\" /s \"d:\\\"")
    print("\"C:\\\\program files\" \"d:\\\"")
    test.cmdParam("\"C:\\\\program files\" \"d:\\\"")
    print("xcopy /s C:\\\\program d:\\")
    test.cmdParam("xcopy /s C:\\\\program d:\\")

if __name__ == "__main__":
    main()