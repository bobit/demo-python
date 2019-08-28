
print(9/3)
print(9//3)
print(9%3)

print(10/3)
print(10//3)
print(10%3)

## 变量和赋值运算符

#  The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

mv_population = 74728
mv_area = 11.995
mv_density = mv_population / mv_area

# 现在我们重新定义 mv_population 变量：
# （注意：后续代码跟在上面三行代码后面，而非重新开始）
mv_population = 75000
print(int(mv_density))

## 整数和浮点数
### int - 表示整数值，float - 表示小数或浮点数值

x = int(4.7)  # x is now an integer 4
y = float(4)  # y is now a float of 4.0
print(x)
print(y)
print(type(x))
print(type(y))

print(.1 + .1 + .1)
print(.1 + .1 + .1 == .3)

## 错误

### 异常
### 语法错误
# Traceback
# ZeroDivisionError: division by zero
# print(5/0)

## 字符串

my_string = 'this is a string!'
my_string2 = "this is also a string!!!"
print(my_string)
print(my_string2)
#在字符串中使用 \，以包含其中一种引号：
# Fix this string!
# ford_quote = 'Whether you think you can, or you think you can't--you're right.'
# 正确
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
ford_quote = "Whether you think you can, or you think you can't--you're right."
print(ford_quote)

_python = len("python")
print(_python)

first_word = 'Hello'
second_word = 'There'
print(first_word + second_word)
print(first_word + ' ' + second_word)

print(first_word * 5)
print(len(first_word))
print(first_word[0])

## 练习：len
## 使用字符串连接和 len 函数计算某些电影明星的实际完整姓名的长度。将该长度存储在变量 name_length 中。注意，姓名不同部分之间有空格！
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + " " + middle_names + " " + family_name)
name_length2 = len(given_name) + len(middle_names) + len(family_name) + 2
print(name_length)
print(name_length2)

# print(len(835))
# 错误消息是：TypeError: object of type 'int' has no len()，len 仅适用于“序列（例如字符串、字节、元组、列表或范围）或集合（例如字典、集合或冻结集合）”。

## 类型和类型转换

### 更改变量类型
#type_change = "0" + 5
#type_change = "0" + "5"
#type_change = "0" + 5
#print(type_change)

### 练习：总销量
### 在此练习中，你需要更改输入和输出的类型，以便获得你想要的结果。

### 请使用提供的数据计算一周的总效率。请输出以下格式的字符串"This week's total sales: xxx"，其中 xxx 将是所有数字的实际总计。你需要更改输入数据的类型，以便计算总计。
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
weeks_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
total_sales = "This week's total sales: " + str(weeks_sales)
print(total_sales)

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)  #convert the type back!!
print("This week's total sales: " + weekly_sales)