# Python有6个序列的内置类型，但最常见的是列表和元组。
## 列表！
lst_of_random_things = [1, 3.4, 'a string', True]
print(lst_of_random_things[0])

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


## 在列表里还是不在列表里？
## 可以使用 in 和 not in 返回一个布尔值，表示某个元素是否存在于列表中，或者某个字符串是否为另一个字符串的子字符串。

print('this' in 'this is a string')
print('in' in 'this is a string')
print('isa' in 'this is a string')
print(5 not in [1, 2, 3, 4, 6])
print(5 in [1, 2, 3, 4, 6])

## 可变性和顺序
## 可以将上述列表中的 1 替换为 'one。这是因为，列表是可变的。
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)

## 不可变，以下代码不可行：
#greeting = "Hello there"
#greeting[0] = 'M'
# print(greeting)

## 有序性
### 字符串和列表都是有序的。但是，你将在后续部分看到某些数据类型是无序的。对于接下来要遇到的每种数据类型，有必要理解如何设定索引，可变吗，有序吗。了解数据结构的这些信息很有用！


## 列表方法
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)
name = "-".join(["García", "O'Kelly"])
print(name)
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

##
L1= [1,2,3,4,5]
L2= ['star','moon']
L3= [1,2,'star']
L= [L1,L2,L3]
print(max(L,key=len))
#print(max(L))

### count()方法
####统计某个元素在列表中出现的次数
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])
####利用list自带的count函数，来统计list中每个元素出现的次数。
arr = [1, 2, 3, 2, 3, 1, 4];
arr_appear = dict((a, arr.count(a)) for a in arr);#返回一个dict，这个dict的key是list本身的元素，value是出现的次数。
print(arr_appear);
