# -*- coding: utf-8 -*-

class DeleteNode():
    def __init__(self, val: 'int', nextVal: 'DeleteNode'):
        self.val = val
        self.nextVal = nextVal

    def setNext(self, nextVal: 'DeleteNode'):
        self.nextVal = nextVal
    
    def __str__(self):
        ans = str(self.val)
        current = self
        if current.nextVal != None:
            ans = ans + " -> " + str(current.nextVal.val)
            current = current.nextVal
        return ans

def main():
    test = DeleteNode()
    print(test.deleteNode())
    print(DeleteNode(1, DeleteNode(1, None)))

if __name__ == "__main__":
    main()