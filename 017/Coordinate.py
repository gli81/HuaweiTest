# -*- coding: utf-8 -*-

class Coordinate():
    def coordinate(self, cmds: 'str') -> 'str':
        cmds_list = cmds.split(';')[:-1]
        valid_cmds_list = []
        cmds_count = {'W': 0, 'A': 0, 'S': 0, 'D': 0}
        for cmd in cmds_list:
            if len(cmd) > 1 and cmd[0] in ['W', 'A', 'S', 'D'] and cmd[1:].isdigit():
                valid_cmds_list.append(cmd)
        for cmd in valid_cmds_list:
            cmds_count[cmd[0]] += int(cmd[1:])
        # print(cmds_count)
        hor = cmds_count['D'] - cmds_count['A']
        ver = cmds_count['W'] - cmds_count['S']
        return str(hor) + ',' + str(ver)


def main():
    test = Coordinate()
    print(test.coordinate("A10;S20;W10;D30;X;A1A;B10A11;;A10;"))
    print(test.coordinate("ABC;AKL;DA1;"))

if __name__ == "__main__":
    main()
