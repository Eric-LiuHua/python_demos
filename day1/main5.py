#!/usr/bin/env python3
# -*- coding: utf-8 -*-



print("********** 调用函数 ********")
print("调用函数的：abs(-1921)=%d"%abs(-1921))

a=abs

print("a=abs 先给函数取个别名,在调用函数的：a(-1921)=%d"%a(-1921))

print(" 1.max ,min 等。都是支持批量 max(2, 3, 1, -5)=",max(2, 3, 1, -5))
print(" 2.max ,min 等。list 入参 max([2, 3, 1, -5])=",max([2, 3, 1, -5]))

print(" 3.list 的入参。min([1,12,23,232])=",min([1,12,23,232]))


print("****数据类型转换*****")

print("float('120.23'')=",float("120.23"))
print("float('119'')=",float("119"))
print("*int 是硬取整数，不会四舍五入")
print("int(12.34)=",int(12.34))
print("int(12.74)=",int(12.74))


print("str(1.234343)=",str(1.234343))

print("bool('')=%s,bool(0)=%s,bool(1)=%s,bool(2)=%s,bool('x')=%s,bool('false')=%s,bool('true')=%s,bool(None)=%s"
      %(bool(""),bool(0),bool(1),bool(2),bool("x"),bool("false"),bool("true"),bool(None)))
print("可以看出，对字符只有空和有值对区分。不会跟其他语言一样判断string 转换之后是否是 bool 类型。")


print("************ 声明函数 *************")
print("python 跟scala 的声明一样，都是def 开头,只是python的函数域是用tab 缩进区分的。scala 是常见的大括号。")

def my_functions(ix):
    if(ix<0):
        return("if(ix<0)")
    elif(ix>=0 and ix<8):
        return ("elif(ix>=0 and ix<8):")
    else:
        return("else:")


print("my_functions(7)=",my_functions(7))
print("my_functions(-1)=",my_functions(-1))


print("*****空函数。"
      "def my_pass():"
      "    pass "
      " 这就是定义一个空函数，pass 表示什么都不做，占位符。可以在用在其他语句 ")



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type,检查 抛出异常。参数类型！')
    if x >= 0:
        return x
    else:
        return -x



print('返回多个值 。直接return x,y ')
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny



print("原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。")
tempc=move(11,23,3)
print("tempc=move(11,23,3)，tempc=",tempc)

x,y =move(11,23,3)
print('这种是使用多参数接收 x,y =move(11,23,3),x=%d,y=%d'%(x,y))


print("练习")

def quadratic(a, b, c):
    print("ax2 + bx + c = 0")


print("""
小结
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
""")


tempv=my_abs('s')
