# total = 1
# for i in range(9, 0, -1):
#     total = (total + 1) * 2
# print("猴子一共摘了%d个桃子" % total)

# for i in range(1, 10):
#     eaten = (total // 2) + 1
#     print("第%d天吃了%d个桃" % (i, eaten))
#     total -= eaten


'''for i in range(10, 100):
    x = 809 * i
    z = 8 * i
    m = 9 * i
    y = 800 * i + m
    if x >= 1000 and x < 10000 and z<100 and z>=10 and m>=100 and m<1000:
        print(f"{x} = 800 * {i} + 9 * {i}")
'''
# # 获取用户输入的模式和要加密（解密）的字符串
# mode = input("请输入模式（加密或解密）：")
# text = input("请输入要{}的字符串：".format(mode))

# # 密钥固定为3，如果模式是解密，则将密钥取相反数
# key = 3
# if mode == "解密":
#     key = -key

# # 初始化结果字符串
# result = ""

# # 遍历输入的每个字符
# for char in text:
#     # 如果字符是空格，则直接将其添加到结果字符串中
#     if char == " ":
#         result += " "
#     # 如果字符是大写字母，则将其转换为ASCII码后进行加密或解密
#     # 然后再将加密或解密后的结果转换为字符并添加到结果字符串中
#     elif char.isupper():
#         result += chr((ord(char) + key - 65) % 26 + 65)
#     # 如果字符是小写字母，则同样按照上述方式进行加密或解密 
#     # ord(char)：获取字符char的ASCII码值；
#     # ord(char) + key：将ASCII码值加上或减去密钥key，得到加密或解密后的ASCII码值；
#     # (ord(char) + key - 65) % 26：对26取模，得到在26个字母中的位置；
#     # (ord(char) + key - 65) % 26 + 65：加上65，得到加密或解密后的ASCII码值在ASCII码表中的位置；
#     # chr((ord(char) + key - 65) % 26 + 65)：将加密或解密后的ASCII码值转换为字符。
#     elif char.islower():
#         result += chr((ord(char) + key - 97) % 26 + 97)
#     # 如果字符不属于字母、空格以外的字符，则直接将其添加到结果字符串中
#     else:
#         result += char

# # 根据模式输出加密或解密后的结果
# print("{}结果为：{}".format(mode, result))

x=eval(input())
if x >= 0:
    y = int(str(x)[::-1])
else:
    y = -int(str(-x)[::-1])
if y >= -2 ** 31 and y <= 2 ** 31 - 1:
    print(y)
else:
    print('0')