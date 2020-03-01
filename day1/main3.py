#!/usr/bin/env python3
# -*- coding: utf-8 -*-



print("使用list和tuple")

print("1.list Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。")

names=["aa,","ddd","dsfs"]

print("len(names)=%s"%len(names))
print("names[0]=%s"%names[0])


print("要确保索引不要越界，记得最后一个元素的索引是len(names) - 1。len(names)-1=%s"%(names[len(names)-1]))
print("还可以用-1做索引，直接获取最后一个元素：names[-1]=%s"%names[-1])

print(r"list中追加元素到末尾：names.append('tempa')")
names.append('tempa')
print(r"把元素插入到指定的位置，比如索引号为1的位置：names.insert(1,'tempb')")
names.insert(1,'tempb')
print("要删除list末尾的元素，用pop()方法：names.pop()")
names.pop()

print("要删除指定位置的元素，用pop(i)方法，其中i是索引位置：names.pop(1)")
names.pop(1)

print("list里面的元素的数据类型也可以不同，比如：")
names.insert(2,1212)
names.insert(3,[123,2132,231])
print(names)
print("取list 中的list 。,names[-2][-1]=%d "%names[-2][-1])


print("2.tuple "
      "另一种有序列表，元组"
      "与list 很类似。但是tuple 一旦初始化就不能修改了。")

print("声明方式：tnames=('aaa','bb','cc')")
tnames=('aaa','bb','cc')
print(tnames)

print("""
不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：""")

print("t=():表示空的元组。")
t=()
print(t)

print("t2=(1):定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义,为了消除歧义，定义一个值的tuple时，使用 ， t3=(1,) 来声明")
t2=(1)
t3=(1,)
print("t2=",t2)
print("t3=",t3)



print("可变的 tuple ：在tuple 中放入list ，改变list 的内容")
t = ('a', 'b', ['A', 'B'])
print("初始化的t=",t)
t[-1][-1] = 'X'
t[-1].append("u")
print("改变后的t=",t)


