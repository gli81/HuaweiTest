# -*- coding: utf-8 -*-

class DeleteNode():
    def __init__(self, val: 'int', nextVal: 'DeleteNode'):
        self.val = val
        self.nextVal = nextVal

    def setNext(self, nextVal: 'DeleteNode', _val: "int" = 0, val_bool: "bool" = False) -> "None":
        if val_bool:
            current = self
            while current.val != _val:
                current = current.nextVal
            nextVal.nextVal = current.nextVal
            current.nextVal = nextVal
        else:
            self.nextVal = nextVal
    
    def deleteNode(self, _val: "int") -> "None":
        current = self
        while current.nextVal.val != _val:
            current = current.nextVal
        current.nextVal = current.nextVal.nextVal

    def __str__(self) -> "str":
        ans = str(self.val)
        current = self
        while current.nextVal != None:
            ans = ans + " -> " + str(current.nextVal.val)
            current = current.nextVal
        return ans

def main():
    # test = DeleteNode()
    # print(test.deleteNode())
    line = [5, 2, 3, 2, 4, 3, 5, 2, 1, 4, 3]
    n = line.pop(0)
    to_be_del = line.pop()
    head = DeleteNode(line.pop(0), None)
    print(n, to_be_del, line, head)
    for i in range(len(line) - 1):
        if i % 2 == 0:
            head.setNext(DeleteNode(line[i], None), line[i + 1], True)
            print(head)
    head.deleteNode(to_be_del)
    print(head)




if __name__ == "__main__":
    main()