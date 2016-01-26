import math
mList = ['Tom','Joy','Mal']
mTuple = (1,2,'Tom')
mDict = {'Tom':99,'Joy':88,'Mal':77}
mSet = set([1,2,3])
mStr = 'ABCD'
mInt = int(123)
mGenerator = (x * x for x in range(1,10))
#切片
l = mList
print(l)
print(l[0:3])
print(l[0:2])
print(l[-2:-1]) #支持最后一个节点为-1
print(l[:1]) #默认为0时可以省略

#迭代
for x in mList:
	print(x)
for x in mStr:
	print(x)
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
#同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(mList):
	print(i,value)

#列表生产式
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
l = []
for x in range(1,10):
	l.append(x)
print(l)
#2
l = []
for x in range(1,10):
	l.append(x*x)
print(l)
#3
l = [x*x for x in range(1,10)]
print(l)
#4 包含if判断
l = [x*x for x in range(1,10) if x % 2 == 0 ]
print(l)
#5 双层循环
l=[m + n for m in 'ABC' for n in 'abc']
print(l)
#6 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os #导入os模块
l = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
#7for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
for k,v in mDict.items():
	print(k,'=',v)

#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
#不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
l = [x * x for x in range(1,10)] #list
g = (x * x for x in range(1,10)) #generator
#一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(mGenerator)) 
for x in mGenerator:
	print(x)
#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(3)
o = odd()
print(next(o),next(o),next(o))
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

#迭代器
#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([], Iterable),isinstance(mList,Iterable),isinstance(mStr,Iterable),isinstance(mInt,Iterable))
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator),isinstance(mList,Iterator),isinstance(mStr,Iterator),isinstance(mInt,Iterator))
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
#直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
#只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


#函数式编程
'''
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''

#高阶函数
#变量可以指向函数
abs(-1) #1
abs     #<built-in function abs>
#可见，abs(-10)是函数调用，而abs是函数本身。

#要获得函数调用结果，我们可以把结果赋值给变量：
'''
f = abs
f(-1) #1
# 函数名也是变量
abs = 10
print(abs(-10))
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not callable
'''
##注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

#传人函数，把函数当做变量传人函数中
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

#map/reduce
#Python内建了map()和reduce()函数。
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x * x
r = map(f, [1,2,3])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
#因此通过list()函数让它把整个序列都计算出来并返回一个list。

#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def fn(x, y):
	return x*10 + y
print(reduce(fn,[1, 3, 5, 7, 9]))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
#还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


##filter
#Python内建的filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_old(x):
	return x % 2 == 1
list(filter(is_old, [0,1,2,3,4]))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
#需要用list()函数获得所有结果并返回list。

#sorted
#排序算法
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
#如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
#因此，比较的过程必须通过函数抽象出来。
sorted(['bob', 'about', 'Zoo', 'Credit'])
#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
#print(f1) <function lazy_sum.<locals>.sum at 0x101c6ed90>
#调用函数f1时，才真正计算求和的结果：
f1()
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1()==f2())
print(f1==f2)
#f1()和f2()的调用结果互不影响。
#闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
#所以，闭包用起来简单，实现起来可不容易。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，
#因此最终结果为9。

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
#已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
#缺点是代码较长，可利用lambda函数缩短代码。


#匿名函数
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x*x时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，
#也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))
#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2016-01-26')
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__,f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
	def wapper(*args, **kw):
		print('call function %s()' %func.__name__)
		return func(*args, **kw)
	return wapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，
#把decorator置于函数的定义处：
@log
def now():
	print('2016-01-26')
now()
#把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
#于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
#首先打印日志，再紧接着调用原始函数。

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2015-3-25')
now()
print(now.__name__)
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now = log('execute')(now)
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
#所以，一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()
print(now.__name__,'sssssss')
#只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。有先后顺序之分，装饰器比赛位于函数之前才能起作用

#偏函数
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
#要注意，这里的偏函数和数学意义上的偏函数不一样。

#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print( int('12345'))
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345', base=8))
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
#调用这个新函数会更简单。

#注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(int2('1000000', base=10))
#
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
#相当于：

args = (10, 5, 6, 7)
print(max(*args))
#结果为10。

#模块
#在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

#为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
#很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。

#一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。

#请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
#否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，
#因为__init__.py本身就是一个模块，而它的模块名就是mycompany

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'pyl'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
#最常见的就是运行测试。

#作用域
'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，
调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''

#安装第三方库
#，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
#比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#pip install Pillow                #
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
#pip install mysql-connector-python
#Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

sys.path












