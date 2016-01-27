#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
mList = ['Tom','Joy','Mal']
mTuple = (1,2,'Tom')
mDict = {'Tom':99,'Joy':88,'Mal':77}
mSet = set([1,2,3])
mStr = 'ABCD'
mInt = int(123)
mGenerator = (x * x for x in range(1,10))
# def p(*x):
#     for s in x:
#         print(s)
p = print
r'''
print('hello world')

1000+1000+2333
print(22+33)
print('100 + 200 =', 100 + 200)
'''
r'''
用户输入字符串 其中name是变量名可以直接输入name打印变量信息or print(name)

name = input() 
name
print(name)

name = input('赶快输入的你姓名:')
print('你好啊，',name)
'''

r'''
print('1024 * 768 = xxx')
print('1024 * 768 = ',1024*768)
'''

#以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。
#其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
r'''
#print("please input some world:")
a = 100
if a>0:
    print(a)
else:
    print(-a)
'''

r'''
#打印出I'm "OK" 的写法.转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m "OK"\nI\'m "OK" too')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试
print('\\\t\\')
print(r'\\\t\\')
'''
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''内容内容'''的格式表示多行内容

#print('''line1
#line2
#line3''')
#好像r'''...'''与'''...'''无法前途使用

#布尔值写法大小写敏感
r'''
True
5>3 #True
True or False #True
not True      #False
#python中的空值Null,0是有意义的
'''

#变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
r'''
a=1
t_007='t_007'
true='hahaha'
answer=True
print(answer)
answer=true
print(answer)
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：
int a = 123; // a是整数类型变量
a = "ABC"; // 错误：不能把字符串赋给整型变量
'''

#常量:但事实上Python根本没有任何机制保证PI不会被改变，
#所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
r'''
PI= 3.14159265359
print(PI)
#除法
print(10/3)              #答案：3.33333333333
#底板除，只保留整数位
print(10//3)               #答案：3
#余数
print(10%3)               #答案：1
'''
#编码：对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
r'''
print(ord('A'),
ord('中'),
chr(66),
chr(25991),'\u4e2d\u6587')
#如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587') #中文
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
x= b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
abc = 'ABC'.encode('ascii') #b'ABC
print(abc)
'中文'.encode('utf-8')
#'中文'.encode('ascii') #含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#在bytes中，无法显示为ASCII字符的字节，用\x##显示。

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
test = b'ABC'.decode('ascii') #ABC
print(test)

#字符长度函数len()
print(len('中文'.encode('utf-8')))

#格式化：最后一个常见的问题是如何输出格式化的字符串。在Python中，采用的格式化方式和C语言是一致的，用%实现
print('hello , %s' %'world') #如果只有一个%?，括号可以省略。
print('Hi, %s, you have $%d.' %('zhangshan',10000))
#%d 整数
#%f 浮点数
#%s 字符串
#%x 十六进制整数
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate : %d%%' %7)
print('growth rate : 7%')
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d - %02d' %(3,1))
print('%.2f' %3.1415926)

add = 85 - 72
rate = add/72*100
print('%.1f%%' %rate)
'''

#list和tuple
r'''
#要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
classMates = ['Tom','Patter','Joy']
print(classMates)
print(len(classMates),classMates[0],classMates[2],classMates[-1]
    )
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classMates.append('Test')
print(classMates)
print(len(classMates),classMates[0],classMates[2],classMates[-1]
    )
#也可以把元素插入到指定的位置，比如索引号为1的位置
classMates.insert(1,'index1')
print(classMates)
#要删除list末尾的元素，用pop()方法
classMates.pop()
print(classMates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classMates.pop(1)
print(classMates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classMates[0] = 'tom'
#list里面的元素的数据类型也可以不同
classMates = ['sss',111,True]
print(classMates)
#list元素也可以是其他list
classMates = ['sss',['ite','ites']]
print(len(classMates),classMates)

#tuple另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改.
classMates = ('Tom','Patter','Joy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
#你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#如果要定义一个空的tuple，可以写成()：
t = ()
print(t)
#定义一个元素
t = (1)
print(t)
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)
##可变的tuple
t = ('a', 'b',['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
'''

#条件判断
r'''
temp = input('输入你的年龄吧:\n')
age = int(temp)
if age<16:
    print('你是小学生吗？')
    print('你真的不是小学生吗？')
elif age<30:
    print('小伙子要努力工作啦!')
    print('我会的啦')
else:
    print('生活什么的才是最重要的啦')
'''

#循环
r'''
names = ['Tom','Joy','Mal']
for x in names:
    print(x)
print('-------------------------------')
for x in names:
    if x == 'Tom':
        print(x)
#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，
#再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
temp = list(range(5))
print(temp)
#range(101)就可以生成0-100的整数序列，计算如下
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 1
while n<99:
    sum = sum + n
    n = n +2
print(sum)
'''

#字典dict和set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
r'''
names = ['Tom','Joy','Mal']
soures = [99,88,77]
#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
di = {'Tom':99,'Joy':88,'Mal':77}
print(di['Tom'])
di['Tom'] = 100
print(di['Tom'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Test' in di,'Tom' in di)
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(di.get('Test'))
print(di.get('Test',-1))
#注意：返回None的时候Python的交互式命令行不显示结果。
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
di.pop('Tom')
print(di)
'''
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：


#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
r'''
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.add(1)
print(s)
s.remove(4)
print(s)

#再议不可变对象

#上面我们讲了，str是不变对象，而list是可变对象。

#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
a.sort() #对元素进行排序
print(a)

#而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b = a.replace('a','A')
print(b,a)
'''
#要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，
#但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'

#函数S=π*r*r
#当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。
#有了函数，我们就不再每次写s = 3.14 * x * x，
#而是写成更有意义的函数调用s = area_of_circle(x)，而函数area_of_circle本身只需要写一次，就可以多次调用。

#抽象
r'''
计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：
100
∑n
n=1
'''


#函数
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
r'''
print(abs(100))
print(abs(-100))
'''
#数据类型转换
r'''
print(int('123'),
#int('12.35'), 不能直接转换
int(float('12.35')),
float('12.35'),
str(12.3),
bool(1),
bool(''))
'''

#定义函数
r'''
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
'''
#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
#return None可以简写为return。
#Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下
#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
#用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
r'''
def nop():
    pass
'''
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
#比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
#但是如果参数类型不对，Python解释器就无法帮我们检查。

#返回多个值
#函数可以返回多个值吗？答案是肯定的。
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
r'''
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(11,33,3,math.pi/6))
'''
#但其实这只是一种假象，Python函数返回的仍然是单一值
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

#函数的参数
#定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，
#以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
#Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
#使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

#位置参数
r'''
def power(x):
    return x * x

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''
#修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
#默认参数
#新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用
#这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
r'''
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''
#这样，当我们调用power(5)时，相当于调用power(5, 2)
#
#先定义一个函数，传入一个list，添加一个END再返回：
r'''
def add_end(L=[]):
    L.append('END')
    return L
'''
r'''
#当你正常调用时，结果似乎不错：
add_end([1, 2, 3]) #[1, 2, 3, 'END']
#当你使用默认参数调用时，一开始结果也是对的：
add_end() #['END']
#但是，再次调用add_end()时，结果就不对了：  
add_end() #['END', 'END']
'''
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
r'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
'''

#可变参数
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
#要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，
r'''
def calc(numbers):
    sum = 0
    for x in numbers:
        sum = sum + x*x
    return sum
calc([1,2,3])
'''
#但是调用的时候，需要先组装出一个list或tuple
#所以，我们把函数的参数改为可变参数：
r'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2,3)
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？
nums = [1, 2, 3]
calc(*nums)
'''

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
r'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
'''
#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
#仍以person()函数为例，我们希望检查是否有city和job参数：
r'''
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
'''
#但是调用者仍可以传入不受限制的关键字参数：
r'''
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
'''
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
r'''
def person(name, age, *, city, job):
    print(name, age, city, job)
'''
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
r'''
person('Jack', 24, city='Beijing', job='Engineer')
#Jack 24 Beijing Engineer
'''

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，
#除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
r'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
'''
#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
r'''
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
'''
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


#递归表达式
r'''
def fact(n):
    if n == 1:
        return 1
    return n*n-1
print(fact(99))
'''
#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
#所以，递归调用的次数过多，会导致栈溢出。
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
#要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
r'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
'''
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


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
im = Image.open('test.jpg')
print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
#pip install mysql-connector-python
#Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

sys.path



#面向对象编程
'''
面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
'''
#假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示
stu1 = {'name':'Tom','soure':99}
stu2 = {'name':'Joy','soure':88}
#而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_soure(stu):
    print('%s : %s' % (stu['name'], stu['soure']))
print_soure(stu1)

#如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
#这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，
#然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student(object):
    """docstring for Student"""
    def __init__(self, name, soure):
        #super(Student, self, name, soure).__init__()
        self.name = name
        self.soure = soure
    def print_soure(self):
        print('%s : %s' %(self.name, self.soure))
Tom = Student('Tom', 98)
Tom.print_soure()        

#类和实例
#面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，
#而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
class Student(object):
    """docstring for Student"""
    def __init__(self):
        super(Student, self).__init__()

st = Student()
print(st)
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，
#继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
st = Student('Tom',99)
print(st.name,st.score)

#数据封装
#面向对象编程的一个重要特点就是数据封装。在上面的Student类中，
#每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据

#访问限制
#在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

#但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
st.name = 'Joy'
print(st.name,st.score)
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
class Student(object):
    """docstring for Student"""
    def __init__(self, name, score):
        super(Student, self).__init__()
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了
st = Student('Tom', 99) 
#print(st.__name,st.__score) 
#AttributeError: 'Student' object has no attribute '__name'  
print(st.get_name(),'namessssss') 
#这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
#特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
#双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
#所以，仍然可以通过_Student__name来访问__name变量：
print('我就是这么任性的访问私有变量：',st._Student__name)

#继承与多态
#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
#而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
class Bird(Animal):
    pass
dog = Dog()
cat = Cat()
bird = Bird()
dog.run()
dog.eat()
cat.run()
bird.run()
#要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(dog)
#静态语音与动态语音
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    """docstring for Timer"""
    def __init__(self):
        super(Timer, self).__init__()
    def run(self):
        print('start.....')
timer = Timer()
run_twice(timer)
#这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
#都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，
#完全可以传入任何实现了read()方法的对象        


#获取对象信息
#当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#使用type()
print(type(123),type('123'),type(True),type(mList),type(abs))
#使用isinstance()
#对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, str))
#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
p(dir('ABC'))
p('ABC'.__len__())

#仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
hasattr(dog, 'x') # 有属性'x'吗？
setattr(dog, 'y', 19) # 设置一个属性'y'
p(getattr(dog, 'y')) # 获取属性'y'
p(dog.y) # 获取属性'y'

#实例属性和类属性
#由于Python是动态语言，根据类创建的实例可以任意绑定属性。

#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name = 'Student'
st = Student()
p(st.name)
st.name = 'Tom'
p(st.name)
del st.name
p(st.name)
#在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


#面向对象高级编程
#数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
#我们会讨论多重继承、定制类、元类等概念。


#使用__slots__
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    """docstring for Student"""
    def __init__(self):
        super(Student, self).__init__()
s = Student()
s.name = 'Tom' #给一个实例绑定属性
p('name:',s.name)  
from types import MethodType
def set_name(self, name):
    self.name = name
s.set_name = MethodType(set_name, s)# 给实例绑定一个方法
s.set_name('Joy')
p(s.name)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_name = MethodType(set_name, Student)
#给class绑定方法后，所有实例均可调用
#使用__slots__
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Tom'
s.age = 24
#s.score = 99
#AttributeError: 'Student' object has no attribute 'score'
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    """docstring for GraduateStudent"""
    def __init__(self):
        super(GraduateStudent, self).__init__()
s = GraduateStudent()
s.name = 'Tom'
s.age = 24
s.score = 99      
p(s.score)

#使用@property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
#这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
#这样，在set_score()方法里，就可以检查参数
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.set_score(60) # ok!
p(s.get_score())

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
#此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
s = Student()
s.score = 70 # ok!
p(s.score)

#多重继承
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟。
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
class Parrot(Flyable, Runnable):
    pass

#MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn


#定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

#__str__
class Student(object):
    """docstring for Student"""
    def __init__(self, name):
        super(Student, self).__init__()
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
    __repr__ = __str__
s = Student('Tom')
p(s)

#__iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
#要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr) #要让class只响应特定的几个属性，抛出AttributeError的错误：

#利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

# __call__

# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()

#使用枚举类
#当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
JAN = 1
FEB = 2
MAR = 3
NOV = 11
DEC = 12
#更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复值。
print(Weekday.Tue)

#使用元类
#type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

# 比方说我们要定义一个Hello的class，就写一个hello.py模块：
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
#当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))

# metaclass

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

# metaclass，直译为元类，简单的解释就是：

# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
' Simple ORM using metaclass '

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

# 错误、调试和测试
# 在程序运行过程中，总会遇到各种各样的错误。

# 有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。

# 有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。

# 还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。

# Python内置了一套异常处理机制，来帮助我们进行错误处理。

# 此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。

# 最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试。

#错误处理
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
#调用堆栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# main() #为了代码可以运行进行注释
# 执行，结果如下
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# 根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。

# 记录错误

# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

# Python内置的logging模块可以非常容易地记录错误信息：
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
# 样是出错，但程序打印完错误信息后会继续执行，并正常退出：
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "err_logging.py", line 13, in main
#     bar('0')
#   File "err_logging.py", line 9, in bar
#     return foo(s) * 2
#   File "err_logging.py", line 6, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# END

# 抛出错误

# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

#foo('0')#TODO
# 执行，可以最后跟踪到我们自己定义的错误：

# $ python3 err_raise.py 
# Traceback (most recent call last):
#   File "err_throw.py", line 11, in <module>
#     foo('0')
#   File "err_throw.py", line 8, in foo
#     raise FooError('invalid value: %s' % s)
# __main__.FooError: invalid value: 0
# 只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

# 最后，我们来看另一种错误处理的方式：
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

#bar()#TODO
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？

# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，
# 如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#常见错误关系
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- ResourceWarning


#调试
#断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

# 如果断言失败，assert语句本身就会抛出AssertionError

# logging

# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
#print(10 / n)
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

#单元测试
# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

# import unittest

# from mydict import Dict

# class TestDict(unittest.TestCase):

#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))

#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')

#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')

#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']

#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。

# 对每一类测试都需要编写一个test_xxx()方法。由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

# self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

# with self.assertRaises(KeyError):
#     value = d['empty']
# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

# with self.assertRaises(AttributeError):
#     value = d.empty

# setUp与tearDown

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

#文档测试
# TODO

# IO编程
# IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

# 比如你打开浏览器，访问新浪首页，浏览器这个程序就需要通过网络IO获取新浪的网页。浏览器首先会发送数据给新浪服务器，告诉它我想要首页的HTML，这个动作是往外发数据，叫Output，随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input。所以，通常，程序完成IO操作会有Input和Output两个数据流。当然也有只用一个的情况，比如，从磁盘读取文件到内存，就只有Input操作，反过来，把数据写到磁盘文件里，就只是一个Output操作。

# IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

# 由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

# 第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；

# 另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式称为异步IO。

# 同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要等5分钟，于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。

# 你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，这样你可以立刻去干别的事情（逛商场），这是异步IO。

# 很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。

# 操作IO的能力都是由操作系统提供的，每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用，Python也不例外。我们后面会详细讨论Python的IO编程接口。

# 注意，本章的IO编程都是同步模式，异步IO由于复杂度太高，后续涉及到服务器端程序开发时我们再讨论。


# 文件读写
# 二进制文件

# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
from datetime import datetime

with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

# StringIO和BytesIO
# StringIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# BytesIO

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO

# write to BytesIO:
f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO:
data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())

# 操作文件和目录
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：


from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

# 序列化
# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：

d = dict(name='Bob', age=20, score=88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# Python提供了pickle模块来实现序列化。
import pickle
d = dict(name='Tom', soure=99, age = 24)
s = pickle.dumps(d)
p(s)
f = open('dumps.txt', 'wb')
pickle.dump(d, f)
f.close()
f = open('dumps.txt', 'rb')
d = pickle.load(f)
f.close()
p(d)


# JSON

# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

# JSON类型       Python类型
# {}              dict
# []              list
# "string"        str
# 1234.56         int或float
# true/false      True/False
# null            None

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

# 进程和线程
# 很多同学都听说过，现代操作系统比如Mac OS X，UNIX，Linux，Windows等，都是支持“多任务”的操作系统。

# 什么叫“多任务”呢？简单地说，就是操作系统可以同时运行多个任务。打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。

# 现在，多核CPU已经非常普及了，但是，即使过去的单核CPU，也可以执行多任务。由于CPU执行代码都是顺序执行的，那么，单核CPU是怎么执行多任务的呢？

# 答案就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，我们感觉就像所有任务都在同时执行一样。

# 真正的并行执行多任务只能在多核CPU上实现，但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。

# 对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。

# 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

# 由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。

# 我们前面编写的所有的Python程序，都是执行单任务的进程，也就是只有一个线程。如果我们要同时执行多个任务怎么办？

# 有两种解决方案：

# 一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。

# 还有一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。

# 当然还有第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用。

# 总结一下就是，多任务的实现有3种方式：

# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。
# 同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。

# 因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。

# Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。
# import os

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 运行结果如下：

# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！

# multiprocessing
# 于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
    print('Run Child process name %s(%s)...' %(name, os.getpid()))
if __name__ == '__main__':
    print('Parent Process %s' %os.getpid())
    p = Process(target=run_proc, args = ('test',))
    print('Child Process Will start...')
    p.start()
    p.join()
    print('Child Process END...')

# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

# Pool

# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print("RUn task %s(%s)" %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task Run %.3f seconds.' %(name, (end - start)))
if __name__=='__main__':
    print('Parent process %s.' %os.getpid())
    pool = Pool(4)
    for x in range(5):
        pool.apply_async(long_time_task, args=(x,))
    print('Waiting for all subprocess done.')
    pool.close()
    pool.join()
    print('All subprocess done.')
# # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

# # 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
# # 因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。


# # 子进程

# # 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

# # subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

import subprocess
print('start...')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.comunicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print('Exit Code::',p.returncode)
# # 进程间通信

# # Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，
# # 提供了Queue、Pipes等多种方式来交换数据。
# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# # 多线程
# # 多任务可以由多进程完成，也可以由一个进程内的多线程完成。

# # 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

# # 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

# # Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

# # 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 5 #TODO n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# # Lock

# # 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# # 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，
# # 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# import time, threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


# # ThreadLocal
# # 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，
# # 但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# # ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# # 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
# # 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# # ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()

# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# # 分布式进程
# # 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

# # Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。

# # 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

# # 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

# # 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：

# import random, time, queue
# from multiprocessing.managers import BaseManager

# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()

# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')
# # 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，
# #添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，
# #必须通过manager.get_task_queue()获得的Queue接口添加。

# # 然后，在另一台机器上启动任务进程（本机上启动也可以）：
# import time, sys, queue
# from multiprocessing.managers import BaseManager

# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')

# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')


# 正则表达式
# 字符串是编程时涉及到的最多的一种数据结构，对字符串进行操作的需求几乎无处不在。比如判断一个字符串是否是合法的Email地址，
# 虽然可以编程提取@前后的子串，再分别判断是否是单词和域名，但这样做不但麻烦，而且代码难以复用
import re
r = re.match(r'^\d{3}\-\d{3,8}$','123-1234')
if r:
    print('success...')
else:
    print('error...')

# 切分字符串
s = 'a  b  c'
print(s.split(' '),re.split(r'\s+', s))
# 分组
# 除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。比如：

# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
r = re.match(r'^(\d{3})\-(\d{3,8})$','159-233333')
print(r.group(0),r.group(1),r.group(2))
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。

# 贪婪匹配
# 后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的0
print(re.match(r'^(\d+)(0*)$', '102300').groups())
# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
print(re.match(r'^(\d+?)(0*)$', '10200200').groups())










