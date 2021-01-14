if __name__ == '__main__':
    # name = '我\n'
    # name1 = "是"
    # ss = type(name)
    # print("类型",ss)
    # print("加法",name+name1)
    # 输入和输出
    # heigth = float(input("请输入你请\"输入身高:"))
    # weigth = float(input("请输入你的体重:"))
    # zhishu = weigth/(heigth*heigth)
    # print("你的身体指数",str(zhishu))
    #
    # if zhishu<18.5:
    #     print("你的体重过轻")
    # if zhishu>=18.5 and zhishu<24.5:
    #     print("你的体重正常")
    # if zhishu>24.5 and zhishu<29.9:
    #     print("你的体重过重")
    # if zhishu >29.9:
    #     print("肥胖")

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
    ''' 
     for i in range(0, 100):
         if i % 2 == 0:
             print("偶数-->", i)
             '''
    # 打印0--100之间的奇数,并且可以被三整除
    # for i in range(0, 100):
    #     if i % 2 == 1 and i % 3 == 0:
    #         print("奇数--被三整除-->", i)
    # 乘法表
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, '*', i, '=', i * j, end='    ')  # end= 以。。。结尾
        print()
