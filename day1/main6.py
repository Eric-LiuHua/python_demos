
#!/usr/bin/env python3
# -*- coding: utf-8 -*-



print("*******位置参数")

def my_power(x,n=2):
    end=1
    while n>0 :
        n=n-1
        end=end*x

    return end


print("my_power(5,3),",my_power(5,3))

print("使用默认参数。my_power(5),",my_power(5))

print("""*********设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。""")

print("默认参数的声明，必须在函数的参数列表最后。不能中间设置默认参数")
def my_enroll(name,age=1,ad="dd",t="dd"):
    print(name)
    print(age)
    print(ad)
    print(t)



my_enroll("2",23,t="dd")
print(r"my_enroll('2',23,t='dd')")

def add_end(L=[]):
    L.append('END')
    return L



print("add_end()",add_end())
print("add_end()",add_end())
print("add_end()",add_end())


print("""********Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

 定义默认参数要牢记一点：默认参数必须指向不变对象！""")





print("*******可变参数")

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def calcl(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum


print("calc(12,3,2,3,4,5),",calc(12,3,2,3,4,5))

print("calcl([12,3,2,3,4,5]) 使用一个list 做可变参数,",calcl([12,3,2,3,4,5]))

print("*******定义可变参数和定义一个list或tuple参数相比，"
      ""
      "仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：")

l=[12,3,2,3,4,5]
print(l)
print("如果已经有一个list或者tuple，要调用一个可变参数怎么办？")
print("Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：calc(*l).",calc(*l))
print("*l表示把*l这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。")


def my_kw(name,**kwargs):
    print("name:",name)
    print ( ",kwargs:",kwargs)



my_kw("ma,dasd",kwargs={"ds":12,"ds":123})

print("""小结

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

""")



