#!/usr/bin/env python3
# -*- coding: utf-8 -*-



print("1.判断分支")
if(1>0):
    print("python 没有大括号来区分域，一个tab 缩近来区分的。")
    print("同时要多一个冒号：")
    print("elseif： esel： 这些同样要：结尾")





print("2。循环：")
names=[12,123,3432,23423]

print("names:",names)
print("循环打印：for name in names:")
for name in names:
    print(name)




print("while 循环")
sum=0
n=1
while sum<10:
    sum=sum+1
    n=n+1
    print("sum:",sum)
    if(n%2==0):
        print("break:n=",n)
        break

    if(n%3==0):
        print("continue:n=",n)
        continue

for x in[12,32,23,12,23,123,243,43,54,2,4]:
    if(n%2==0):
        continue
    print("for continue:",x)

print("break,continue 跟其他的语言差不多。")





print("""*****************dict *******************

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
为什么dict查找速度这么快？因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。
dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。



list：使用中括号 [] 可变
tuple：使用小括号 ()  初始化之后就不可变。但是可以在初始化的时候放一个list。通过改变这个list 实现可变。
dict:使用大括号，类似对象。{}， key 不能使用list 但是key 和value 的类型都是可以多种类型共存，不过value 的类型可以是list 
set：就是tuple+list 的实现。([])  跟dict 一样，不能在用list 做key。但是其他跟list 差不多。支持多个类型。
""")

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)

print("获取字典的值：d['Bob']=%d"%d['Bob'])
print("设置字典的值是,除了初始化的时候赋值，也可以直接d['tempkey']=89,多次这样，之前的值会被覆盖。")
d["tempkey"]=89

print("获取字典的值：d['tempkey']=%d，这样做情况如果没有这个key ，那就会异常，"%d['tempkey'])

print("通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value： d.get('tempx')=%s,d.get('tempx',-1)=%s "%(d.get("tempx"),d.get("tempx",-1)))
print("TypeError: %d format: a number is required, not NoneType ,none 不能替换%d 的占位符。")


d.pop("tempkey")
print("dict  的删除key 跟list 一样的。 d.pop('tempkey')=%s "%d.get("tempkey"))

d[1]="dsfs"
d[2]=[1,2,0]

#d[[1,2,0]]="dslkjldsjf"
print("""增加一个key是list 的key，会提示异常。
 d[[1,2,0]]="dslkjldsjf"TypeError: unhashable type: 'list'
                            """)
print("d=",d)

print("""




******请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。""")





print("************* set ************************")

print("""
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
s = set(["1", "2", "3"])
如果初始化的时候有重复的值，会默认过滤的，通过 add 增加的也是没有效果。
""")

s = set(["1", "2", "3"])
print("s=",s)

s = set(["1", "2", 3])
print("初始化的list ，使用两种数据类型,可以说明python的set 跟list 一样 支持多种数据类型。。s=",s)

#s=set([1,2,3,[23,334]])
print("""初始化的时候，设置一个为list 提示异常： s=set([1,2,3,[23,334]]) TypeError: unhashable type: 'list'
""")

s.add("dsfnnix")
print("s.add('dsfnnix') ,s=",s)

s.remove("1")
print("s.remove('1'),s=",s)


s.remove("a")
print("移除不存在的，没有效果也不会异常，，s.remove('a'),s=",s)


