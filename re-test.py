#_*_ coding:UTF-8 _*_
#正则表达式学习
import re
import os
import keyword
from random import randrange,choice
from string import ascii_lowercase as lc
from time import ctime
from sys import maxsize

class ReTest:
    def test1(self):
        with open('whodata.txt','r') as f:
            for eachLine in f:
                print(re.split(r'\s+',eachLine))
    def gendata(self):
        datalist = []
        tlds = ('com','edu','net','org','gov')
        for i in range(randrange(10,30)):
            dtint = randrange(maxsize)/1000000000
            dtstr = ctime(dtint)
            llen = randrange(4,8)
            login = ''.join(choice(lc) for j in range(llen))
            dlen = randrange(llen,13)
            dom = ''.join(choice(lc) for j in range(dlen))
            datalist.append('%s::%s@%s.%s::%d-%d-%d\n'%(dtstr,login,dom,choice(tlds),dtint,llen,dlen))

        with open('redata.txt','w+') as f:
            for i in datalist:
                f.write(i)
    #课后练习
    def test1_1(self):
        #识别后续的字符串：’bat‘、'bit'、'but'、'hat'、'hit'、'hut'
        print('输入Q退出匹配模式')
        while(1):
            data = input('请输入你要匹配的字符串:')
            if data == 'Q' or data == 'q':
                break
            patt = '[bh][aiu]t'
            m = re.match(patt,data)
            if m is not None:
                print(m.group())
            else:
                print(data,'不在匹配模式中')

    def test1_2(self):
        #匹配由单个空格分割符的任意单词对，也就是姓和名。
        data = 'aaa bbb'
        patt = r'\s'
        m = re.split(patt,data)
        print(m)

    def test1_3(self):
        #匹配由单个逗号和单个空白符分割的任何单词和单个字母，如姓氏的首字母
        data = 'L jinxin'
        patt = r'[,\s]'
        m = re.split(patt,data)
        print(m)
    #匹配所有有效python标识符集合
    def test1_4(self):
        data = 'if,age,user_name_total,2nd_place,A_bb,for,$price,user-name,nn56d,章三'       
        patt1 = re.compile(r'(?<![\$!`;-])\b[^\W\d]\w*\b(?![\$!`;-])')
        m = re.findall(patt1,data)
        print(m)
        mlist = []
        for i in range(len(m)):
            if m[i] not in keyword.kwlist:
                mlist.append(m[i])
        print(mlist)
    #匹配以‘www’起始且以.com结尾的简单Web域名；例如:www://www.yahoo.com/.
    def test1_6(self):
        data = '$%R2378www://www.ya_87hoo.com/trye#$http://www.foothill.edu57ggh'
        patt = r'(?:https|www|http):\/\/www\.[\w\d]*\.(?:com|edu|net)\/?'
        m = re.findall(patt,data)
        print(m)
    #匹配所哟能够表示python整数/浮点数/复数的字符串集
    def test1_7_10(self):
        data = ['0034','0','234','18237443945382934102483473857389066786',
                   '6570000','000000','1.2','-98','-00067','.09','00.22','0.0.0','1.00987',
                   '-000.00','+0.9',
                   '1+2j','1.11-3.09j','0.000+0.12j','-0.2-8j','0098+00j','1+2']
        pattint = r'^[+-]?(0{1}|[1-9]+[0-9]*)$'
        pattfloat = r'^[+-]?(?:0{1}|[1-9]+[0-9]*)\.\d*$'
        pattcomplex = r'^[+-]?(?:0{1}|[1-9]+[0-9]*)(?:\.\d*)?[+-](?:0{1}|[1-9]+[0-9]*)(?:\.\d*)?j$'
        for i in data:
            m = re.findall(pattcomplex,i)
            if len(m) != 0:
                print(m)
    #匹配所有能够表示有效电子邮件的地址的集合
    def test1_11(self):
        data = 'lretest@qq.com'
        patt = r'^(?:(?:[^<>()[\]\\.,;:\s@\"]+(?:\.[^<>()[\]\\.,;:\s@\"]+)*)|(?:\".+\"))@(?:(?:\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(?:(?:[a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
        m = re.findall(patt,data)
        print(m)
    #匹配所有能够表示有效的网站的集合
    def test1_12(self):
        patt = r"""
        \b  # 单词边界
        (?:  # 非捕获组：协议部分（可选）
            (?:https?|ftp)://  # http://, https://, ftp://
            | www\.  # 或 www. 开头
        )? 
        (?:  # 域名部分（支持国际化域名）
            [a-zA-Z0-9]  # 首字符为字母或数字
            (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?  # 标签（长度1-63）
            (?:  # 子域名（可选）
                \.  # 点分隔符
                [a-zA-Z0-9]  # 子域名首字符
                (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?  # 子域名标签
            )*
            \.  # 顶级域前的点
            [a-zA-Z0-9-]{2,}  # 顶级域（至少2个字母）
        )
        (?::\d{1,5})?  # 端口（可选）
        (?:  # 路径/查询/锚点（可选）
            /  # 路径开始
            [^\s?#]*  # 非空白、非?非#的字符
            (?:  # 查询字符串（可选）
                \?  # 问号
                [^\s#]*  # 查询内容
            )?
            (?:  # 锚点（可选）
                \#  # 井号
                [^\s]*  # 锚点内容
            )?
        )?
        $  # 边界
        """

        # 编译正则表达式（忽略空格和注释，不区分大小写）
        regex = re.compile(patt, re.VERBOSE | re.IGNORECASE)

        # 测试用例
        test_cases = [
            "https://www.example.com",
            "http://example.com/path?query=string#section",
            "ftp://files.example.org:8080",
            "www.subdomain.example.co.uk",
            "example.com",
            "https://xn--e1afmkfd.xn--p1ai",  # 国际化域名（俄语）
            "invalid. com",  # 无效（含空格）
            "user@example.com",  # 邮箱（不应匹配）
            "example-.com",  # 无效域名
            "https://example.com/path/file.txt",
            'https://www.jyshare.com/codedemo/7623/',
            'https://www.runoob.com/regexp/regexp-example.html'
        ]

        # 提取匹配的URL
        m = [url for url in test_cases if regex.fullmatch(url)]
        print("有效网站URL:")
        for url in m:
            print(f"- {url}")
    #type():
    def test1_13(self):
        data = str(type(True))
        print(data)
        patt = r'\'(\w+)\''
        m = re.findall(patt,data)
        print(m)
    #处理日期：创建一个正则表达式来表示日历的月份
    def test1_14(self):
        data = ['1',2,13,'sdf','12fg','12','02','020','002']
        patt = r'(?:0?[1-9])|(?:1[0-2])'
        for i in data:
            if re.fullmatch(patt,str(i)):
                print(i)    
    def test1_15(self):
        data = ['4444-666666-55555','123456789012345','4444-4444-4444-4444','55555-333-4444-4444','22-4444-999999999']
        patt = r'(?:[0-9]{15,16})|(?:\d{4}-\d{6}-\d{5})|(?:\d{4}-\d{4}-\d{4}-\d{4})'
        for i in data:
            if re.fullmatch(patt,str(i)):
                print(i)
    #判断在redata.txt中一周的每一天出现的次数
    def test1_17(self):
        patt = r'^(\w{3})'
        Dict = {}
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = re.search(patt,data).group()
            if Dict.get(m) == None:
                Dict[m] = 1
            else:
                a = Dict.get(m)
                a = a + 1
                Dict[m] = a
        print(Dict)
    #通过确认整数字段中的第一个整数匹配在每个输出行起始部分的时间戳，确保在redata.txt中没有被数据损坏
    def test1_18(self):
        patt = r'\s+(\d+)\s+(?:(?:(?:0[0-9])|(?:1[0-9])|(?:2[0-3])):(?:[0-6][0-9]):(?:[0-6][0-9]))'
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = re.findall(patt,data)
            if len(m) == 0:
                print('该行数据已被损坏...')
            else:
                print(data)
    #提取每行中完整的时间戳
    def test1_19_21t23(self):
        patt = r'''
        ^
        (
        ([A-Za-z]{3})\s+ #日期:group(2)
        ([A-Za-z]{3})\s+ #月份:group(3)
        (\d+)\s+ #天数:group(4)
        ((?:(?:[0-1][0-9])|(?:2[0-3]))(?::[0-6][0-9]){2})\s+ #时间:group(5)
        (\d+) #年份:group(6)
        )'''
        #编译正则表达式
        regex = re.compile(patt,re.I | re.X)
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = regex.search(data).group(5)
            print(m)
   #提取每行中完整的电子邮件地址
    def test1_20_24to25(self):
        patt = r'''
        ::
        (?:([A-Za-z]+) #登陆名
        @
        (?:([A-Za-z]+)\.([A-Za-z]{3}))#域名和高级域名
        )'''
        regex = re.compile(patt,re.I | re.X)
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = regex.findall(data)
            print(m)
    #使用你的电子邮件地址替换每一行数据中的电子邮件地址
    def test1_26(self):
        patt = r'''([A-Za-z]+@[A-Za-z]+\.[A-Za-z]{3})'''
        em = 'ljxnlbc@163.com'
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = re.sub(patt,em,data)
            print(m)
    #从时间戳中提取月、日和年，然后以“月,日,年”的格式，每一行仅仅迭代一次
    def test1_27(self):
        patt = r'''
        ^
        (
        ([A-Za-z]{3})\s+ #日期:group(2)
        ([A-Za-z]{3})\s+ #月份:group(3)
        (\d+)\s+ #天数:group(4)
        ((?:(?:[0-1][0-9])|(?:2[0-3]))(?::[0-6][0-9]){2})\s+ #时间:group(5)
        (\d+) #年份:group(6)
        )'''
        #编译正则表达式
        regex = re.compile(patt,re.I | re.X)
        with open('redata.txt','r') as f:
            datalist = f.readlines()
        for data in datalist:
            m = regex.sub(r'\3,\4,\6',data)
            print(m)
    #匹配电话号码，但是允许可选的区号作为前缀
    def test1_28(self):
        patt = r'''^((?:(?:\d{3}-)?|\(\d{3}\))\d{3}-\d{4})$'''
        datalist = ['800-555-1212','555-1212','(800)800-555-1212','(800)555-1212']
        for data in datalist:
            m = re.findall(patt,data)
            print(m)
    


Ree = ReTest()
#Ree.gendata()
a = Ree.test1_28()
        
