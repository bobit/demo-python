## 字典和恒等运算符
### 字典是可变数据类型，其中存储的是唯一键到值的映射。

### 字典的键可以是任何不可变类型，例如整数或元组，而不仅仅是字符串。
str_elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(str_elements["helium"])

int_elements = {1: 11, 2: 22, 3: 33}
print(int_elements[1])

str_int_element =  {"zhangsan": 30, 2: 22, 3: 33}
str_int_element["zhangsan"] = 35
print(str_int_element["zhangsan"])

### 检查值是否在字典
print("carbon" in str_elements)
print(str_elements.get("dilithium"))

### 恒等运算符
#### is	检查两边是否恒等，is not	检查两边是否不恒等
## 字典中查询值
m = str_int_element.get("zhangsan") #返回None
m2 = str_int_element.get('lisi','There\'s no such element!') #返回None
#n = str_int_element["lisi"] #  KeyError ,如果你预计查询有时候会失败，get 可能比普通的方括号查询更合适。
#print(n)
print(m)
print(m2)
print(m is None)
print(m is not None)


## 检查是否相等与恒等：== 与 is
### 列表 a 和列表 b 是对等和相同的。列表 c 等同于 a（因此等同于 b），因为它们具有相同的内容。但是 a 和 c（同样 b 也是）指向两个不同的对象，即它们不是相同的对象。这就是检查是否相等与恒等的区别。
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)