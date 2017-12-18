# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: CSVFileReadingWriting.py
@time: 2017/12/18 21:03
@项目名称:operating
"""
import csv
class READINGCSV:
    def __init__(self,_data):
        self._data = _data # 需要操作的csv文件

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type :" , exc_type)
        print("exc_val :" , exc_val)
        print("exc_tb :" , exc_tb)

    def csv_read(self):
        """
            通过文档的分隔符以及引用字符来读取数据
            delimiter分隔符：将字符串中带有该属性的内容进行分割
            quotechar引用字符来区分同一个字典，并且不返回quotechar的内容
        :return:
        """
        handle = open(self._data, newline='')
        spamreader = csv.reader(handle, delimiter=' ',
                                quotechar="|")
        """
                with open(self._data, newline='') as csvfile:
            spamre = csv.reader(csvfile, delimiter=' ',
                                    quotechar="|")
        """
        return spamreader


    def dict_read(self):
        handle = open(self._data, newline='')
        spamreader = csv.DictReader(handle)
        return spamreader
        """
                with open('names.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                print(row['first_name'], row['last_name'])
        """

    def sni_read(self):
        handle = open(self._data, newline='')
        dialect = csv.Sniffer().sniff(handle.read(1024))
        # 首次读取时，从第N个字符开始
        handle.seek(0)
        reader = csv.reader(handle, dialect)
        return reader
        """
                with open('example.csv', newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            # 首次读取时，从第N个字符开始
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            for row in reader:
                print(row)
        """


class WRITINGCSV:
    def __init__(self,_file,_data,):
        self._file = _file # 需要操作的csv文件
        self._data = _data # 需要输入的内容

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type :" , exc_type)
        print("exc_val :" , exc_val)
        print("exc_tb :" , exc_tb)

    def csv_writh(self):
        with open(self._file, 'w', newline='') as csvfile:
            # 传入的内容必须是字典。。
            # 没输入完字典内的一个value时就有一个delimiter
            # 每输完一个字典之后就有一个引用字符
            # quoting:分割符以及引用字符的写入方式
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|',
                                    quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerows(self._data)




    def dict_writh(self,fieldnames):
        # 一对一形式的写入。
        # fieldnames标题名
        #　writer.writerow写入数据。并以键值对的关系写入
        #  长度和内容要对齐
        with open(self._file,'w',newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames)
            writer.writeheader()
            writer.writerow(self._data)


    def sniff_wtite(self):
        with open(self._file, 'w', newline='') as csvfile:
            csvfile.write("66")

if __name__ == '__main__':
    import os
    report_path = os.path.join(os.getcwd(), "example.csv")
    print(report_path)
    dictq = {"你好吗？？","不好。。","为什么？","没钱."}
    with WRITINGCSV(report_path,dictq) as csvfile:
        spamreader = csvfile.sniff_wtite()