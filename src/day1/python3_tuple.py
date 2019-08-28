# Python的元组与列表类似，不同之处在于元组的元素不能修改。


tuple = ( 'bobit', 786 , 2.23, 'tom', 70.2 )
list = [ 'bobit', 786 , 2.23, 'tom', 70.2 ]
# tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用
print(list)