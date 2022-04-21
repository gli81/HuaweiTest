# -*- coding: utf-8 -*-

class ErrorMark:
    def errorMark(self, records: 'list[str]') -> 'list[str]':
        error = []
        error_map = {}
        line_num = []
        for record in records:
            rec_list = record.split(' ')
            error_to_add = rec_list[0].split('\\')[-1]
            if len(error_to_add) > 16:
                error_to_add = error_to_add[-16:]
            key = error_to_add + ' ' + rec_list[1]
            if key not in error: error.append(key)
            if key in error_map:
                error_map[key] += 1
            else:
                error_map[key] = 1
        if len(error) > 8:
            error = error[-8:]
        ans = []
        for i in error:
            ans.append(i + ' ' + str(error_map[i]))
        return ans

    
    def getErrorName(self, record: 'str') -> 'str':
        pass
def main():
    test = ErrorMark()
    print(test.errorMark(["D:\\zwtymj\\xccb\\ljj\\cqzlyaszjvlsjmkwoqijggmybr 645", "E:\\je\\rzuwnjvnuz 633",\
        "C:\\km\\tgjwpb\\gy\\atl 637", "F:\\weioj\\hadd\\connsh\\rwyfvzsopsuiqjnr 647", "E:\\ns\mfwj\\wqkoki\eez 648",\
            "D:\\cfmwafhhgeyawnool 649", "E:\\czt\\opwip\\osnll\\c 637", "G:\\nt\\f 633", "F:\\fop\\ywzqaop 631", "F:\\yay\\jc\\ywzqaop 631",\
                "D:\\zwtymj\\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645"]))

if __name__ == '__main__':
    main()
