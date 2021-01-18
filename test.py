if __name__ == '__main__':
    # name = '我\n'
    # name1 = "是"
    # ss = type(name)
    # print("类型",ss)
    # print("加法",name+name1)
    # 输入和输出 使用while时注意格式
    # while True:
    #     heigth = float(input("请输入你请输入身高:"))
    #     weigth = float(input("请输入你的体重:"))
    #     zhishu = weigth / (heigth * heigth)
    #     print("你的身体指数", str(zhishu))
    #     if zhishu < 18.5:
    #         print("你的体重过轻")
    #     if zhishu >= 18.5 and zhishu < 24.5:
    #         print("你的体重正常")
    #     if zhishu > 24.5 and zhishu < 29.9:
    #         print("你的体重过重")
    #     if zhishu > 29.9:
    #         print("肥胖")

    # 多重if结构
    # falg =int(input("请输入数字:"))
    # if falg == 1 :
    #    print("数字",falg)
    # elif falg == 2:
    #    print("数字",falg)
    # else :
    #     print("没有")

    # 数据类型转换
    # number = int(123.32)
    # print("浮点类型转整型-->", number)
    # print("**************************")
    # numberfloat = float(123)
    # print("整型转浮点类型-->", numberfloat)
    # print("**************************")
    # numberstr = str(123)
    # print("整数类型转字符串-->", numberstr)
    # print("**************************")
    # numberhex = hex(123)
    # print("整数类型转换为十六进制的字符串类型-->", numberhex)
    # print("**************************")
    # numberoct = oct(123)
    # print("整数类型转换为八进制的字符串-->", numberoct)

    # for循环
    # 找出0--100之间的偶数

    # for i in range(0, 100):
    #     if i % 2 == 0:
    #         print("偶数-->", i)

    # 打印0--100之间的奇数,并且可以被三整除
    # for i in range(0, 100):
    #     if i % 2 == 1 and i % 3 == 0:
    #         print("奇数--被三整除-->", i)

    # 乘法表
    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print(j, '*', i, '=', i * j, end='    ')  # end= '' 表示不换行
    #     print()

    # 三角型
    # for i in range(5):
    #     print("*" * (i + 1))

    # 循环数组
    # d = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', }
    # for i in d:
    #     print(d[i])

    # for循环
    # for i in range(1, 100, 2):
    #     print("输出一百之间,间隔两位数的数字-->", i)

    # 位运算符
    # print("2左移3位-->", 2 << 3)
    # print("2右移3位-->", 16 >> 3)
    # pwd = input("请输入密码")
    # print("原始密码", pwd)
    # key = input("请输入密钥")
    # mima = int(pwd) ^ int(key)
    # print("加密后的密码", mima)
    # print("解密后的密码", mima ^ int(key))

    # 序列,根据 索引取值
    # str = "我是你爸爸"
    # str1 = "喜极而泣"
    # str2 = "欢天喜地"
    # str3 = "你是宝贝"
    # print(str[0], str1[0], str2[0], str3[0])
    # 序列的索引是负数
    # strf = "我是你"
    # print("索引是负数-->", strf[-3])
    # 切片
    #     b = ['科比', '乔丹', '拉萨尔', '哈登', '威少', '库里', '度莱特', '威廉姆斯']
    # print(b[1:5])
    # print(b[0:5:2])
    # print(b[5])
    # 插入 %s %d  %f
    # string = 'hello'
    # print('string=%s!' % string)
    # # 当原字符串的长度小于8时,在字符串左边使用空格补充
    # print('string=%8s!' % string)
    # # %-8s意思是字符串的长度是8 当原字符串的长度小于8时,在字符串左边使用空格补充
    # print('string=%-8s!' % string)
    # # %.2s 截取字符串的前两位,如果截取的长度大于字符串的长度即是字符串身
    # print('string=%.2s' % string)
    # # %a.bs!表示先执行bs 截取字符串,然后当字字符串的长度小于7时使用空格进行补充
    # print('string=%7.2s!' % string)
    # # 精度匹配
    # print('string=%*.*s!' % (7, 2, string))
    # print()
    # print('******************************************')
    # print()
    # num = 12
    # print('num=%d' % num)
    # print('num=%3d' % num)
    # print('num=%-3d!' % num)
    # #%05d表示数字的长度为5,当长度不够时使用0向左补充
    # print('num=%05d!'%num)
    # print('num=%.5d'%num)
    # list
    List = [1000, 2000, 3000, 1, 4000, 2, 5000, 6000, 7000, 8000, 9000]

    # List.append(123)
    # print(List)
    # List.insert(2, 147)
    # print(List)
    # print(List.pop())
    # print(List)
    # del List[1]
    # print(List)
    # for i in List:
    #     print(i)
# 第一种,直接进行升序排序
# List.sort()
# print(List)d
# #冒泡排序
    s = range(len(List))[::-1]
    for i in s:
        for j in range(i):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
    print(List)
# 杨辉三角(1)
# def yang(n):  # 注意 n 是从 0 开始的
#     if n == 0:
#         return [1]
#     else:  # 据观察可知，每一行的杨辉三角数列，都可以有两个上一行的数列计算出来（需要借助[0]错位相加）
#         # 比如，第四行[1 3 3 1] 可有[0 1 2 1]和[ 1 2 1 0]相加得到
#         return [([0] + yang(n - 1))[i] + (yang(n - 1) + [0])[i] for i in range(n + 1)]
# print('yang:', yang(5))  # yang: [1, 4, 6, 4, 1]
# n = 8
# for i in range(n):
#     print(yang(i))
# 杨辉三角(2)
# n = int(input("请输入三角的大小:"))
# list1 = []
# for n in range(n):
#     row = [1]  # 第一行第一列为1
#     list1.append(row)
#     if n == 0:
#         for num in row:  # 这里主要是为输出做的格式处理
#             print(num, end=" ")
#             print()
#         continue
#     for m in range(1, n):
#         row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#     row.append(1)
#     for num in row:
#         print(num, end=" ")
#     print()

# for i in range(len(List)):
#     if List[i] == 2000:
#         List[i] = 2000000
# print(List)
# 二维列表
#     erwei = [['a1', '张三1', 100],
#              ['a2', '张三2', 200],
#              ['a3', '张三3', 300],
#              ['a4', '张三4', 400],
#              ['a5', '张三5', 500],
#              ['a6', '张三6', 600],
#              ]
# for erwei_info in erwei:
#     for i in erwei_info:
#         print(i, end=' ')
#     print()
# 元祖
# yuanzu = (10, 20, 30, 40, 50, 60, 70, 80, 90)
# print("元祖-->", yuanzu)
# print("将元组转为list-->", list(yuanzu))
# print('将liet转为元组-->',tuple(List))
# 双重循环的案列
#     end1 = 'y'
# while end1 == 'y' or end1 == 'Y':
#     name = input('请输入员工的名字:')
#     monye1 = 0
#     for i in range(1, 4):
#         monye2 = int(input('请输员工的第' + str(i) + '个月的业绩'))
#         monye1 += monye2
#     monye1 = monye1 / 3
#     print('员工' + name + ',三个月的平均业绩为:' + str(monye1) + '元')
#     end1 = input('是否继续:')

# 使用break 和 continue
# i = 0
# while i < 100:
#     print(i)
#     if i == 55:
#         break
#     i = i + 1
# print('******************')
# for i in range(1, 100):
#     if (i % 2 == 1):
#         print('已被2%尽')
#         continue
#     print(i)
# while True:
#     name =input("请输入:")
#     if(name=='sb'):
#         break

# 求出最大值与最小值
#     zuida = 0
#     zuixiao = 0
# while True:
#     num = int(input('请输入一个数字(输入0结束)'))
#     if (zuida == 0 and zuixiao == 0):
#         zuida = num
#         zuixiao = num
#     if(num !=0):
#         if (zuida > num):
#             zuixiao = num
#         else:
#             zuida = num
#     else:
#         break
# print('最大值-->' + str(zuida) + '最小值-->' + str(zuixiao))
