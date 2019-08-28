# Python 函数
## 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

### 内建函数，比如print()。

### 自定义函数
def hello() :
    print("Hello World!")

hello()
#### 参数传递
##### python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
##### 传不可变对象实例
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print( b ) # 结果是 2
##### 传可变对象实例
###### 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print ("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
#传入函数的和在末尾添加新内容的对象用的是同一个引用。