# Python 内置函数

## abs() 函数返回数字的绝对值。
print("abs(-40) : ", abs(-40))
print("abs(100.10) : ", abs(100.10))

## max() 方法返回给定参数的最大值
print("max(80, 100, 1000) : ", max(80, 100, 1000))
print("max(-20, 100, 400) : ", max(-20, 100, 400))
print("max(-80, -20, -10) : ", max(-80, -20, -10))
print("max(0, 100, -400) : ", max(0, 100, -400))

print(max(["3","23","10","22"]))
print(min(["3","23","10","22"]))
print(max(["23","23","10","22"]))
print(max([3,23,10,22]))
print(min([3,23,10,22]))

print(["3","23","10","22"])
print(max("-1"))
print(max("23"))
print(max("23","22"))
print(max("23","13"))
print(max("23","3"))


## round() 方法返回浮点数x的四舍五入值。
print("round(70.23456) : ", round(70.23456))
print("round(56.659,1) : ", round(56.659, 1))
print("round(80.264, 2) : ", round(80.264, 2))
print("round(100.000056, 3) : ", round(100.000056, 3))
print("round(-100.000056, 3) : ", round(-100.000056, 3))

## type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
print(type(4))  # returns <class 'int'>
print(type(3.7))  # returns <class 'float'>
print(type('this'))  # returns <class 'str'>
print(type(True))  # returns <class 'bool'>


### type() 与 isinstance()区别
#### type() 不会认为子类是一种父类类型，不考虑继承关系。
#### isinstance() 会认为子类是一种父类类型，考虑继承关系。
#### 如果要判断两个类型是否相同推荐使用 isinstance()。
class A:
    pass
class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False

## eval() 函数用来执行一个字符串表达式，并返回表达式的值。
x = 7
_eval = eval('3 * x')
_eval = eval('pow(2,2)')
_eval = eval('2 + 2')
n = 81
_eval = eval("n + 4")
print('3 * x')
print(3 * x)
print("n + 4")
print(_eval)