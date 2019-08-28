# 开发环境 python3.0 + idea

# Missing parentheses in call to 'print'
# Python2.X和Python3.X不兼容。安装的是Python3.X，但是试图运行如下Python2.X 的代码，会报如上错误。

# print "你好世界"; # Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
# print "hello word"; # python3.0版本,需要将print后面的语句加括号
# raw_input("按下 enter 键退出，其他任意键显示...\n") # python3.0版本,用input替换了raw_input

print(max(["3","23","10","22"],key=int))
lst_of_random_things = [1, 3.4, 'a string', True]
## 你可以通过使索引减一获取最后一个元素。因此，你可以执行以下操作：
print(lst_of_random_things[len(lst_of_random_things) - 1])

## 可以使用负数从列表的末尾开始编制索引，其中 -1 表示最后一个元素，-2 表示倒数第二个元素，等等。
print(lst_of_random_things[-1])

## 列表切片
## 下限索引包含在内，上限索引排除在外
## 冒号表示从冒号左侧的起始值开始，到右侧的元素（不含）结束。
print(lst_of_random_things[1:2])
print(lst_of_random_things[1:])
print(lst_of_random_things[:2])
print(type(lst_of_random_things[1:2]))
print(type(lst_of_random_things[1:]))
print(type(lst_of_random_things[:2]))