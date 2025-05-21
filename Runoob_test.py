#_*_ coding:UTF-8 _*_
import cmath
import math
import random
import calendar
import datetime
import time
import re
import sys
#Python Hello World 实例
def Hello_world_test():
    print('Hello World!')
#数字求和
def Add_test():
    x = input("请输入第一个数字:")
    y = input("请输入第二个数字:")
    try:
        z = float(x)  + float(y)
    except:
        print("输入数据错误！请输入数字!")
    else:
        print("{0} + {1} = {2}\n".format(x,y,z))
#平方根
def Sqrt_test():
    f = int(input("输入的数据为实数请输入1,复数请输入2:"))
    if f == 1:
        data = input("请输入一个数字:")
    elif f == 2:
        real = input("请输入实部:")
        imag = input("请输入虚部:")
        data = complex(float(real),float(imag))#构成复数
    try:
        data1 = cmath.sqrt(float(data))#可以开复数以及负数的平方根
    except:
        print("请输入一个数字！")
    else:
        print('数据data = {0}的平方根为:{1:5f}'.format(data,data1))
#二次方程
def Qe_test():
    #ax^2+bx+c = 0
    try:
        a = float(input("请输入系数a:"))
        b = float(input("请输入系数b:"))
        c = float(input("请输入系数c:"))
    except:
        print("请输入数字！")
    #非一元二次方程a == 0的情况
    if a == 0:
        if b == 0:
            print("无解")
        elif c == 0:
            print("无穷解")
        print("方程为线性方程x = {0}".format(-c/b))
        return 0
        
    #判断b^2-4ac是等于0还是大于0还是小于0 
    
    delta = b**2 - 4*a*c
    print("delta={0:5f}".format(delta))

    if delta == 0:
        x = -b/(2*a)
        print("x有相同的实根:")
    elif delta > 0:
        x1 = (-b+math.sqrt(delta)/2*a)
        x2 = (-b-math.sqrt(delta)/2*a)
        print("有两个不相等的实根解,x1={0:5f},x2={1:5f}".format(x1,x2))
    elif delta < 0:
        x1 = (-b+cmath.sqrt(delta)/2*a)
        x2 = (-b-cmath.sqrt(delta)/2*a)
        print("有两个不相等的复数根解,x1={0:5f},x2={1:5f}".format(x1,x2))
    return 0

#三角形的面积
def Triarea_test():
    while(1):
        triangle = input("请输入三角形的三条边，如(10,6,9)")
        try:
            sides = [float(side) for side in triangle.split(',')]
            #将三条边从短到长排序
            sides.sort()    
            a = sides[0]
            b = sides[1]
            c = sides[2]
        except:
            print("请输入数字！")
        else:
            #判断三条边是否能组成一个三角形
            if a <= 0 or b <= 0 or c <=0 :
                print("请输入大于0的数字！")
            elif a + b <= c:
                print("这三条边不能组成一个三角形!")
            else:
                #计算半周长
                s = (a + b + c)/2
                #计算面积
                area = (s*(s-a) * (s-b) *(s-c)**0.5)
                print('三角形的面积为:{0:5f}'.format(area))

#圆的面积
def Roundarea_test():
    while(1):
        try:
            r = float(input("请输入圆的半径:"))
        except:
            print("请输入数字！")
        else:
            if r<0:
                print("请输入不小于0的数字！")
            else:
                area = math.pi*r**2
                print("半径为{0}的圆的面积为:{1:5f}".format(r,area))
#随机数的生成(电脑在0-100之间选择一个数字，玩家来猜测电脑选择的数字)
def Random_test():
    while(1):
        random_number = random.randint(0,100)
        count = 0
        while(1):
            count = count + 1
            play_number = int(input("请输入你要猜测的数字:"))
            if play_number > random_number:
                print('您输入的数字比电脑选择的数字大！')
            elif play_number < random_number:
                print('您输入的数字比电脑选择的数字小！')
            elif play_number == random_number:
                print('恭喜您！猜对了！电脑选择的数字为：{0},您总计猜测了{1}次'.format(random_number,count))
                break
        if input("是否要再次玩游戏?Y:再玩一次,N:退出游戏:") == 'N':
            break

#摄氏温度与华氏温度转换
def CandF_test():
    data = ''
    while(1):
        f = input("请选择你要输入摄氏温度(C)还是华氏温度(F)?:")
        try:
            if f.lower() == 'c':
                C = float(input("请输入摄氏温度:"))
                data = C * 9/5 + 32
            elif f.lower() == 'f':
                F = float(input("请输入华氏温度:"))
                data = (F - 32) * 5/9
        except:
            print("请输入数字!")
        else:
            if f.lower() == 'c':
                print('摄氏度为:{0}C->华氏度为:{1}F'.format(C,data))
            elif f.lower() == 'f':
                print('华氏度为:{0}F->摄氏度为:{1}C'.format(F,data))

#交换变量
def ChangeTrans_test():
    a = 'c'
    b = 'd'
    print('a={0},b={1}'.format(a,b))
    c = 'c'
    a = b
    b = c
    print('a={0},b={1}'.format(a,b))

#判断闰年
def LeapYear_test():
    while(1):
        try:
            year = input("请输入你想判断的年份，如果想输入多个年份请用空格分割，如:(2008 1988 2025):")
            #years = [int(y) for y in year.split(' ')]
            ye = year.split(' ')
            years = [int(y) for y in range(int(ye[0]),int(ye[1]))]
        except:
            print("请输入数字")
        else:
            for y in years:
                if y % 400 == 0:
                    print('{0}年是世纪闰年！'.format(y))
                elif y % 4 == 0 and y % 100 != 0:
                    print('{0}年是闰年'.format(y))
                #else:
                #    print('{0}年是平年'.format(y))

#判断是否为质数
def PrimeNum_test():
    while(1):
        try:
            num = int(input("请输入一个数字:"))
        except:
            print('请输入数字！')
        else:
            if num > 1:
                div = 2
                while(1):
                    if num % div == 0 and num != div:
                        print('{0}不是质数'.format(num))
                        break
                    elif num / div < div:
                        print('{0}是质数'.format(num))
                        break
                    div = div + 1
            else:
                print('不是质数')

#输出制定范围内的素数
def PrimeNumRange_test():
    prlist = []
    while(1):
        try:
            num = input("请输入需要判断是否为素数的范围，如(2 500):")
            nums = num.split(' ')
            num0 = int(nums[0])
            num1 = int(nums[1])
        except:
            print('请输入数字！')
        else:           
            for n in range(num0,num1+1):
                div = 2               
                while(1):
                    if n == 1 or n < 1 or n % div == 0 and n != div:
                        break
                    if n / div < div:  
                        prlist.append(n)       
                        break         
                    div = div + 1
                if len(prlist) == 10:
                    for i in prlist:
                        print('{0:2d}'.format(i),end = ' ')
                    print('\n')
                    prlist = []
            for i in prlist:
                print('{0:2d}'.format(i),end = ' ')
            print('\n')
#阶乘
def Factorial_Test():
    while(1):
        try:
            num = int(input('请输入你要阶乘的数据！:'))
        except:
            print('请输入整数！')
        else:
            if num < 0:
                print('复数没有阶乘')
            elif num == 0:
                print('0的阶乘为1')
            else:
                data = 1
                num1 = num
                #math.factorial(num)->math中实现阶乘的函数
                while(num1 > 1):
                    data = data * num1
                    num1 = num1 - 1
                print('{0}!的值为:{1}'.format(num,data))

#九九乘法表
def Nine_test():
    while(1):
        try:
            num = int(input('请输入你要生成的乘法表：'))
        except:
            print('请输入数字！')
        else:
            for i in range(1, num + 1):
                for j in range(1,i+1):
                    print('{0}x{1}={2}    '.format(j,i,i*j),end = ' ')
                print('\n')
                                 
#斐波那契数列（使用生成器和迭代器创建）
def Fib_test(number):
    a = 0
    b = 1
    c = 0
    n = number
    while(n > 0):
        if n == number:
            c = a
        elif n == number - 1:
            c = b
        else:
            c = a + b
            a = b
            b = c
        yield c
        n-=1

#阿姆斯特朗数
def ArmStrong_test():
    while(True):
        try:
            f = int(input('判断数字是否为阿姆斯特朗数:1,判断范围内所有阿姆斯特朗数:2:'))
            if f == 1:
                number = int(input('请输入你要判断的数字:'))
            elif f == 2:
                number = input('请输入范围使用空格隔开如:0 100:')
                number = [int(n) for n in number.split(' ')]
            else:
                print('请选择你要输入的类型！')
                continue
        except:
            print('请输入数字！')
        else:            
            if type(number) == int:
                n = len(str(number))    
                a=0
                num = str(number)
                for i in num:
                    a  = a + int(i) ** n               
                if a == number:
                    print('{0}是阿姆斯特朗数!,它的次方为:{1}'.format(number,n))
                else:
                    print('{0}不是阿姆斯特朗数!'.format(number))
            else:
                for mm in range(number[0],number[1]):
                    n = len(str(mm))
                    a=0
                    num = str(mm)
                    for i in num:
                        a  = a + int(i)** n                       
                    if a == mm:
                        print('{0}:次方为:{1}'.format(mm,n))

#最大公约数和最小公倍数
def MaxcomdivAndMixcommul_test():
    while(True):
        try:
            n = input("请输入你要计算的数字并用空格分割如:(12 15 30):")
            numberlist = [int(x) for x in n.split(' ')]
        except:
            print('请输入数字！')
        else:
            #最大公约数
            nummin = min(numberlist)
            #能整除最小数据的整数
            divlist = []
            for i in range(1,nummin + 1):
                if nummin % i == 0:
                    divlist.append(i)
            divlist.sort(reverse=True)#将得到的每个数字的约数从大到小排序       
            num = 0
            for i in divlist:           
                for j in numberlist:
                    n = j % i
                    if n != 0: 
                        flag = 1                      
                        break
                    else:
                        flag = 0
                        num = i
                if flag == 0:
                    break
            print("{0}的最大公约数为:{1}".format(numberlist,num))

            #最小公倍数
            nummax = max(numberlist)
            b = 0
            while(1):
                b = b + 1
                for i in numberlist:
                    if b * nummax % i != 0:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag == 1:
                    break
            print("{0}的最小公倍数为:{1}".format(numberlist,b * nummax))

#简单计算器
def Calculator_test():
    while(True):
        flag = 0
        exprlist = []
        oper = ['+','-','*','/','//''%','**']
        print('如已将数据全部输入完毕,请点击q')
        while(True):
            a = input('请输入数字：')
            try:
                a1 = float(a)
                exprlist.append(a)
            except:
                print('请输入数字！')
            b = input('请输入运算符:')
            if b == 'q':
                break          
            while( b not in oper):
                print('输入的运算符无效请重新输入，有效运算符为:{0}'.format(oper))
                b = input('请输入运算符:')
            exprlist.append(b)
        if exprlist[-1] in oper:
            exprlist.pop()
        #先把乘除法做了
        temp_exlist = []
        for i in range(1,len(exprlist),2):          
            o = exprlist[i]           
            if o == '*':
                data = float(exprlist[i-1]) * float(exprlist[i+1])
                temp_exlist.append(data)
            elif o == '/':
                data = float(exprlist[i-1]) / float(exprlist[i+1])
                temp_exlist.append(data)
            elif o == '//':
                data = float(exprlist[i-1]) // float(exprlist[i+1])
                temp_exlist.append(data)
            elif o == '%':
                data = float(exprlist[i-1]) % float(exprlist[i+1])   
                temp_exlist.append(data)            
            elif o == '**':
                data = float(exprlist[i-1]) ** float(exprlist[i+1])
                temp_exlist.append(data)
            else:
                if i == 1:
                    temp_exlist.append(exprlist[i-1])
                temp_exlist.append(o)
        #再做加减法
        data = 0
        for i in range(1,len(temp_exlist),2):          
            o = temp_exlist[i]
            if o == '+':
                data = float(temp_exlist[i-1]) + float(temp_exlist[i+1])
                temp_exlist[i-1] = data
                temp_exlist.pop(i)
                temp_exlist.pop(i+1)
            elif o == '-':
                data = float(temp_exlist[i-1]) - float(temp_exlist[i+1])
                temp_exlist[i-1] = data
                temp_exlist.pop(i)
                temp_exlist.pop(i+1)
        data = temp_exlist[0]
        for i in range(1,len(exprlist),2):
            if i == 1:
                print(float(exprlist[i-1]),end = ' ')
            print(exprlist[i],end=' ')
            print(float(exprlist[i+1]),end = ' ')
        print(' = {0}'.format(data))
            
#简单计算器1:(使用eval函数可以把字符串转化为表达式)
def Calculator1_test():
    oper1 = ['*','/','//''%','**']
    oper2 = ['+','-']
    while(True):
        a = input('请输入你要运算的表达式,如:1+3*4/2:')
        print('{0}={1}'.format(a,eval(a)))
#生成日历(使用日历模块:calendar)
def calendar_test():
    while(True):
        try:
            y = int(input('请输入年份:'))
        except:
            print('请输入正整数！')
        else:
             m = input('请输入月份(如果需要全年日历请直接回车):')
             if m != '':
                 try:
                    m = int(m)
                 except:
                     print('请输入正整数')
                 print(calendar.month(y,m))
             else:
                 for i in range(1,13):
                     print('-----------------------------')
                     print(calendar.month(y,i))
 
#使用递归函数生成斐波那契数列
def RecFibo(num):   
    if num <= 1:
        return num
    else:
        return (RecFibo(num-1)+RecFibo(num-2))

def RecFibo_test():
    while(True):
        a = 0
        try:
            num = int(input('输入想计算的fibo前几项:'))
        except:
            print('请输入正整数！')
        else:
            if num < 0:
                print('请输入正整数！')
                break
            for i in range(num):
                print(RecFibo(i),end = ' ')
            print('\n')

#文件IO
def Fileio_test():
    #写文件
    with open('test.txt','a',encoding='utf-8') as out_file:
        out_file.write('\n看不见我写的什么东西吗？\n哈哈哈')

    #读文件
    with open('test.txt','rt',encoding='utf-8') as in_file:
        print(in_file.read())

#计算每个月的天数:calendar
def CalMonthDay_test():
    y = 2016
    m = 12
    monthday = calendar.monthrange(y,m)
    print('{0}年{1}月:{2}天，一号是星期{3}'.format(y,m,monthday[1],monthday[0]))

#获取昨天日期
def Yesterday_test():
    today = datetime.date.today()
    print(today)
    #往前回退几天
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    print(yesterday)

#约瑟夫生者死者小游戏
def Ysflifeanddeath():
    while(True):
        try:
            kk = input('')
            a = 30#开始的总人数
            b = 9
            c = 15#余下的人
        except:
            print('请输入正整数！')
        else:
            #给30个人编号
            p = list(range(1,a+1))
            while(len(p) > c):
                print('编号{0}下船'.format(p.pop(b-1)))
                p = p + p[:b-1]
                del p[:8]

#五人分鱼
def Fivedfish():
    finish = 2
    finish1 = 2
    #方式1
    while(True):
        finish = finish1
        for i in range(6):      
            if (finish - 1)%5 != 0:               
                break
            g = (finish - 1)//5#每一个人拿的鱼
            s = finish - g - 1#每个人拿走之后剩下的鱼
            finish = s
        if i == 5:
            print('一共捕捞了{0}条鱼'.format(finish1))
            break
        finish1 = finish1 + 1

    #方式2
    fish = 1
    while(True):
        total,enough = fish,True
        for i in range(5):
            if(total - 1)%5 == 0:
                total = (total - 1)/5*4
            else:
                enough = False
                break
        if enough == True:
            print('一共捕捞了{0}条鱼'.format(finish1))
            break
        fish = fish + 1

#实现秒表功能
def Seccon_test():
    print('按下回车开始计时,按下ctrl+c停止计时。')
    while (True):
        input("")
        start_time = time.time()
        print('开始计时')

        try:
            while(True):
                elapsed_time = round(time.time() - start_time,0)
                print('计时{0}秒'.format(elapsed_time),end = '\r')
                time.sleep(1)
        except KeyboardInterrupt:
            end_time = time.time()
            total_time = round(end_time - start_time,2)
            print('计时结束,总时长为{0}秒'.format(total_time))
            break

#n个自然数的立方和
def Sumnatuarlnum_test():
    while(True):
        num = input('请输入你要计算的自然数，如:1,3,6,7:')
        try:
            numlist = [int(i) for i in num.split(',')]
        except:
            print('请输入正整数！')
        else:
            data = 0
            for i in numlist:
                if i < 0:
                    print('{0}<0不计入计算'.format(i))
                else:
                    data = data + i * i * i
            print('{0}的立方和为:{1}'.format(num,data))

#数组反转指定个数元素
def Turnnumarray_test():
    while(True):
        arr = input('请输入你要的数组,并用逗号隔开,如:1,as,566,qq:')
        n = int(input('请输入要将几个元素翻转:'))
        arrlist = [i for i in arr.split(',')]
        print('翻转前:{0}'.format(arrlist))
        while(True):
            arrlist = arrlist + arrlist[:n]
            del arrlist[:n]
            print('翻转后:{0}'.format(arrlist))
            n = int(input('请输入要将几个元素翻转:'))

#移除列表中重复的元素
def Removearrre_test():
    arr = [1,2,3,3,5,6,3,1,2,5,7,8,9,1,5]
    arry = []
    for i in arr:
        if i not in arry:
            arry.append(i)
    print(arr)
    print(arry)

#给按照键或值排序
def dictionairy():
    #声明字典
    key_value = dict()
    #初始化字典
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 

    print('按键排序:')
    #sored(key_value):返回重新排序的列表
    for i in sorted(key_value):
        print((i,key_value[i]),end = "")
    print('\n')

    print(sorted(key_value.items(),key = lambda kv:(kv[0])))

    print('按值排序:')
    print(sorted(key_value.items(),key = lambda kv:(kv[1],kv[0])))


    lis = [{ "name" : "Taobao", "age" : 100},  
            { "name" : "Runoob", "age" : 7 }, 
            { "name" : "Google", "age" : 100}, 
            { "name" : "Wiki" , "age" : 200 }]

    #通过age升序排序 
    print('列表通过age升序排序:')
    print(sorted(lis,key=lambda i:(i['age'])))

    #先按照age升序，再按name排序
    print('列表通过age和name排序:')
    print(sorted(lis,key=lambda i : (i['age'],i['name'])))

    #按age降序排序
    print('列表通过age降序排序:')
    print(sorted(lis,key=lambda i : i['age'],reverse=True))

#合并字典
def Merge_test():
    dict1 = {'a': 10, 'b': 8} 
    dict2 = {'d': 6, 'c': 4} 
    #方式一
    (dict2.update(dict1))
    print(dict2)

    #方式二
    dict3 = {**dict1,**dict2}
    print(dict3)

#二分查找法
def Binarysearch_test():
    arr = [1,4,5,7,11,2,46,9,10,22,78,34,55,32,99,0,77,
           18,6,12]
    arr1 = []
    while(len(arr1) < 31):
        arr1.append(random.randint(-100,100))
    arr = []
    for i in arr1:
        if i not in arr:
            arr.append(i)       
    arr.sort()
    x = -60
    length = len(arr)
    l1 = 0
    r1 = length - 1
    if length >= 1:
        #获取数组的中间值
        mid = int(length/2)
        #元素正好在中间位置
        while(True):
            if arr[mid] == x:
                print('数组:{0}'.format(arr))
                print('{0}在数组中的索引值为:{1}'.format(x,mid))
                break
            elif x < arr[mid]:
                l = l1
                r = mid   
                r1 = mid          
            elif x > arr[mid]:
                l = mid
                r = r1    
                l1 = mid     
            mid = int((l + r)/2)   
            if l - r == 1 or l - r == -1:
                print('该数组中没有{0}的索引'.format(x))
                break

#插入排序
def InsertionSort():
     #构造随机数组
    arr = []
    n = 10
    for i in range(n):
         while(True):
            a = random.randint(-100,100)
            if a not in arr:
                arr.append(a)
                break
    print('原始数组:{0}'.format(arr))
    for i in range(1,len(arr)):
        key = arr[i]
        j = i
        while(key < arr[j-1]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j -1
        print('第{0}次排序:{1}'.format(i,arr))

#快速排序
def Quicksort_test(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Quicksort_test(left) + mid + Quicksort_test(right)

#选择排序
def Selectionsort_test():
    arr = []
    n = 10
    for i in range(n):
         while(True):
            a = random.randint(-100,100)
            if a not in arr:
                arr.append(a)
                break
    print('原始数组:{0}'.format(arr))
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
        print('第{0}次排序:{1}'.format(i,arr))
                
#冒泡排序(先把大的数排好了再排小的)
def Bubblesort_test():
    arr = []
    n = 10
    for i in range(n):
         while(True):
            a = random.randint(-100,100)
            if a not in arr:
                arr.append(a)
                break
    print('原始数组:{0}'.format(arr))
    for i in range(len(arr)):
        flag = 0
        for j in range(1,len(arr) - i):
            if arr[j] < arr[j-1]:
                flag = 1
                arr[j],arr[j-1] = arr[j-1],arr[j]
        if flag == 0:
            break
        print('第{0}次排序:{1}'.format(i+1,arr))






if __name__=="__main__":
    #Add_test()
    #Sqrt_test()
    #Qe_test()
    #Triarea_test()
    #Roundarea_test()
    #Random_test()
    #CandF_test()
    #ChangeTrans_test()
    #LeapYear_test()
    #PrimeNum_test()
    #PrimeNumRange_test()
    #Factorial_Test()
    #Nine_test()
    #fibo = Fib_test(10)
    #while True:
        #try:
            #print(next(fibo),end = ' ')
        #except StopIteration:
            #print('\n')
            #sys.exit()
    #ArmStrong_test()
    #MaxcomdivAndMixcommul_test()
    #Calculator1_test()
    #calendar_test()
    #RecFibo_test()
    #Fileio_test()
    #CalMonthDay_test()
    #Yesterday_test()
    #Ysflifeanddeath()
    #Fivedfish()
    #Seccon_test()
    #Sumnatuarlnum_test()
    #Turnnumarray_test()
    #Removearrre_test()
    #dictionairy()
    #Merge_test()
    #Binarysearch_test()
    #InsertionSort()
    #arr = [-11,60,-99,8,-41,-12,52,2,-93,-8]
    #print(Quicksort_test(arr))
    #Selectionsort_test()
    Bubblesort_test()