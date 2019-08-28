
## 注释
# 第一个注释
print ("Hello, Python!") # 第二个注释

## 行与缩进
### python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。

## 多行语句
### Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句。

## 字符串(String)
str='world'
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\nworld')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nworld')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

## 同一行显示多条语句
### Python可以在同一行中使用多条语句，语句之间使用分号(;)分割
import sys; x = 'hello'; sys.stdout.write(x + '\n')