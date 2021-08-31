# Python高级



## 偏函数

偏函数：在函数调用之前，就可以得知某些参数的值，这样函数有一个参数或者多个参数时，一部分参数可以预先知道，这样函数就能以最少的参数进行调用，节约编程成本

```python
import functools
int_2 = functools.partial(int, base=2)  # base 代表进制
print(int_2('1'))
```

- args形式

  ```python
  import functools
  def addCount(x, y):
      return x + y
  
  
  add = functools.partial(addCount, 4)
  print(add(4))
  ```

- kwargs形式的参数

  ```python
  def show(name, age):
      return f'{name}--->{age}'
  
  
  s = functools.partial(show, age=19)
  print(s('s'))
  ```

- 回调函数形式

  ```python
  import functools
  def show1(name, age):
      print(f'{name}--->{age}')
  
  
  def ca(callback):
      print('回调函数参数未知执行')
      callback()
  
  show_1 = functools.partial(show1, name='2', age=22)
  ca(show_1)
  ```

## 装饰器

装饰器：给已经存在的函数添加额外的功能

@wraps：保留原函数，不让装饰器取代原函数

- 不带参数的装饰器

  ```python
  import time
  from functools import wraps
  
  
  def logger(func):
      @wraps(func)
      def writer_logging():
          print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
          func()
  
      return writer_logging
  
  @logger
  def work():
      print('正在工作')
  
  
  work()
  ```

- 装饰器带参数

  ```python
  import time
  from functools import wraps
  
  
  def logger(func):
      @wraps(func)
      def writer_logging(*args, **kwargs):
          print(f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}')
          func(*args, **kwargs)
  
      return writer_logging
  
  @logger
  def work():
      print('正在工作')
  
  work()
  ```

- 装饰器带参数

  ```python
  import time
  from functools import wraps
  
  
  def main_logger(logfile='work.log'):
      def logger(func):
          @wraps(func)
          def writer_logging(*args, **kwargs):
              log = f'[info] ------>时间是：{time.strftime("%H:%M:%S", time.localtime())}'
              print(log)
              with open(logfile, 'a') as f:
                  f.write(log)
              func(*args, **kwargs)
  
          return writer_logging
  
      return logger
  
  @main_logger()
  def work():
      print('正在工作')
  
  @main_logger('log1.log')
  def work1(name):
      pass 
  work()
  ```

- 类的方式定义装饰器

  ```
  类的方式定义装饰器，需要在类中实现__call__方法
  ```

  ```python
  import time
  from functools import wraps
  
  
  class Logger:
      def __init__(self, log_file='work.txt', level='INFO'):
          self.log_file = log_file
          self.level = level
  
      def __call__(self, func):
          @wraps(func)
          def logger(*args, **kwargs):
              log = f'{[self.level]}------> 时间是:{time.strftime("%H:%M:%S", time.localtime())}'
              print(log)
              with open(self.log_file, 'a') as f:
                  f.write(log)
              func(*args, **kwargs)
  
          return logger
  
  
  @Logger()
  def work():
      print('工作')
  
  
  @Logger(log_file='work1.txt', level='WARING')
  def work1():
      print('共')
  
  
  work()
  work1()
  ```

## 迭代器

- **可迭代对象**

  - 可迭代对象：内置__iter__方法的对象就是可迭代对象，该方法可以不依赖索引取值

  - 可迭代对象可以重复迭代，只能使用for循环进行迭代

- **迭代器**

  - 迭代器：内置__iter__方法和__next__方法的对象就是迭代器对象
  - 迭代器只能迭代一次，可以通过for循环或者next方法进行迭代

- **可迭代对象和迭代器的区别**
  - 可迭代对象不能通过next()函数进行迭代，但是可以通过for循环进行迭代
  - 迭代器可以通过next()函数进行迭代，也可以通过for循环进行迭代
  - 最大区别：可迭代对象可以无限迭代，迭代器只能迭代一次(是一个数据流的形式）
  - 迭代器一定是可迭代对象，可迭代对象不一定是迭代器

- **迭代器优缺点**

  - 优点：
    - 提供了一种通用不依赖索引的迭代取值方式
    - 同一时刻内存中只存在一个值，节省内存

  - 缺点：
    - 没有索引取值灵活，无法指定一个值，只能往后，不能往前
    - 不能预测迭代器的长度

- **for循环本质**
  - for循环本质是迭代器的循环
  - 调用in后面的可迭代对象的iter()方法，将可迭代对象变为迭代器
  - 调用迭代器里面的next()方法，将得到的返回值赋值给变量名
  - 循环往复，直到迭代器抛出异常，for循环自动捕获异常然后结束循环

- **判断对象是否可迭代对象或者迭代器**

  ```
  from collections.abc import Iterable  # 可迭代对象
  from collections.abc import Iterator  # 迭代器
  ```

  - 判断是否是迭代器isinstance(obj, Iterator)  返回值为布尔值
  - 判断是否是可迭代对象isinstance(obj, Iterable)  返回值为布尔值

- **可迭代对象变为迭代器**

```
iter()
__iter__()
```

## 生成器

**生成器是一种特殊的迭代器**

**为什么需要生成器**

- 列表所有的数据都存在内存中，消耗内存
- 想要得到大量的数据，又想占用空间少，可以使用生成器

**生成器的创建方式**

```python
(x for x in range(1, 10))
```

```python
def test():
    a, b = 0, 1
    while True:
        # yield用于创建生成器，返回后面的变量给生成器
        yield b  # b是斐波拉契数中的一个元素
        # print(b)
        a, b = b, (a + b)
```

如果一个函数中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator。调用函数就是创建了一个生成器（generator）对象

**生成器的工作原理**

- 生成器(generator)能够迭代的关键是它有一个next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常。
- 带有 yield 的函数不再是一个普通函数，而是一个生成器generator。可用next()调用生成器对象来取值。next 两种方式 t.__next__() | next(t)。可用for 循环获取返回值（每执行一次，取生成器里面一个值）。（基本上不会用`next()`来获取下一个返回值，而是直接使用`for`循环来迭代）。
- yield相当于 return 返回一个值，并且记住这个返回的位置，下次迭代时，代码从yield的下一条语句开始执行。
- .send() 和next()一样，都能让生成器继续往下走一步（下次遇到yield停），但send()能传一个值，这个值作为yield表达式整体的结果

```
遍历生成器中的内容：
    ① 内置的函数next()函数  获取第一个值
    ② for循环遍历
    ③ 使用object对象中的__next__()方法
    ④ 使用send函数  生成器第一次调用时需要传递 send(None) 后面没有限制
```

## 元类

元类用来创建类

```
元类：用来创建类的类
1.通过导包语句
from ... import  ... 这个时候  python解释器自动调用type函数创建了一个元类
2.手动通过type函数
type(类名, 父类, 属性)
自定义元类:
    ① 通过继承type，自定义元类
    class Class_xxx(type):
        里面可以使用__new__方法用来创建一个新的对象，但是进行返回时，需要返回type.__new__(cls, name, bases, attrs)
            cls:这个类本身
            name:名字
            bases:父类
            attrs:属性
        def __new__(cls, name, bases, attrs):
            ...
            return type.__new__(cls, name, bases, attrs)
    ② 通过def的方式
    不使用__new__方法，在返回时使用type(name, bases, attrs)函数进行创建
    def xxx(name, bases, attrs):
        name:名字
        bases:父类
        attrs:属性
        return type(name, bases, attrs)
hasattr(obj, attr)  查看对象是否有指定的属性 返回值为boolean
3.__class__ 查看对象的类型
4.__metaclass__ 用来创建类
如果当前类中有metaclass属性，那么就会使用当前这个类当中的metaclass属性进行类的创建
如果当前类中没有metaclass属性，那么就会使用在父类当中寻找metaclass属性
如果父类中没有metaclass属性，就会使用type进行类的创建
5.元类设置静态方法[@staticmethod]和类方法[@classmethod]
@classemethod
def class_method():
    print('class_method')

@staticmethod
def static_method():
    print('static_method')
type(name, bases, {'attr': attr, 'static_method': static_method, 'class_method': 'class_method'}


类方法：需要和类进行交互，不需要和实例进行交互。类方法和实例方法相似，但传递的不是类的实例，而是类本身。可以通过类实例或者类本身调用
静态方法：和类相关，和类的实例和属性无关 可以通过类的实例对象或者类本身进行调用
```

## 闭包

闭包：内部函数可以引用外部函数的变量，并且内部函数可以在外部进行调用

**闭包的三个条件**

- 必须有一个内部函数
- 内部函数的定义必须在外部函数的闭合范围内，内部函数引用外部函数的变量
- 外部函数必须返回内部函数

**注意：介于外部函数和内部函数之间的变量，需要使用nonlocal关键字进行修饰**

**闭包的陷阱**

```python
def tes():
    add_list = []
    for i in range(1, 4):
        def tes_(_i=i):
            return _i ** 2

        add_list.append(tes_)
    return add_list

f1, f2, f3 = tes()
print(f1(), f2(), f3())
```

这里给内部函数tes_添加了一个形参_i
**如果不给内部函数添加形参,那么在内部函数执行之前，for循环里面的变量就已经发生了变化,for循环已经全部执行了一遍,这个变量会影响到所有引用它的内部函数；在外部函数还没有返回内部函数之前，内部函数还不是闭包函数，只是一个普通的函数。**
**正确的做法应该是将父函数的局部变量赋值给闭包函数的形参。因为在函数在进行定义时，对形参的赋值会保存在当前函数的定义中，不会对其他函数有影响**
**注意：如果内部函数没有返回外部函数的局部变量，就不是闭包**

## 面向对象进阶

- 类中的__slots__方法

  ```
  默认情况每一个类都会有一个dict,这个dict用来维护实例的所有属性,dict只保持实例的变量，不会保存类的属性
  每次实例化都要分配一个dict，造成空间的浪费，因此有了__slots__,__slots__是一个元组，包括了当前的访问对象，
  类的实例中只能使用__slots__中定义的属性，不能增加其他属性。
  注意：
      有了__slots__,类就不再有__dict__
  ```

```python
import types


class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = 'k'
p.age = 23
```

- **给实例对象添加方法**

```python
import types 

def func(self):
    return '这是实例对象的方法'
    
p.method = types.MethodType(func, p)
p.method()
```

- **给类添加静态方法**

  ```python
  @staticmethod
  def fun():
      return '给类添加一个静态方法'
  
  Person.staticRun = fun
  Person.staticRun()
  ```

- **给类添加类方法**

  ```python
  @classmethod
  def f(cls):
      return '给类添加一个类方法'
  Person.method = f
  Person.method.run()
  ```

## property装饰器

装饰器property作用：
    ① 用来修饰方法，将方法变为一个属性
    ② 与定义的属性结合使用，防止属性被修改

python中实现私有属性的三种方法

- 常用的get,set方法

  ```python
  class M:
      def get_m(self):
          return self._m
  
      def set_m(self, value):
          if value >= 0 and value <= 88:
              self._m = value
              # print(value)
          else:
              raise ValueError('值错误')
              
  m = M()
  m.m = 5
  print(m.m)
  ```

- 使用python中的属性property

  ```python
  class M:
      def get_m(self):
          return self._m
  
      def set_m(self, value):
          if value >= 0 and value <= 88:
              self._m = value
              # print(value)
          else:
              raise ValueError('值错误')
  
      v = property(get_m, set_m)
  
  
  m = M()
  m.v = 4
  print(m.v)
  ```

- 使用python中的装饰器@property

  ```python
  class Student:
      @property
      def age(self):
          return self._age
  
      @age.setter
      def age(self, value):
          if value >= 0 and value <= 88:
              self._age = value
          else:
              raise ValueError('错误')
  
      @property
      def name(self):
          return self._name
  
      @name.setter
      def name(self, value):
          self._name = value
  
  
  s = Student()
  s.age = 1
  s.name = '李梅'
  print(s.age, s.name)
  ```

## 枚举

python中定义枚举的方式，一种使用Enum类直接进行创建，一种是类继承Enum类

**注意**

- 定于枚举时，成员名称name不能重复
- 默认情况下，不同的成员值value可以相同，但是两个相同值value的成员，第二个成员的名称被视作第一个成员的别名
- 如果枚举存在相同值的成员，在通过值value获取枚举成员，只能获取到第一个成员
- 枚举成员可以进行同一性[is]，等值比较[==]，但是不能进行大小比较

通过Enum函数定义枚举

```python
from enum import Enum

month = Enum('', ('一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'))
print(month.__class__.__class__)
print(month.__members__)  # 获取所有的数据
print(month['一'].value)  # 通过键获取值
print(month(3).name)  # 通过值获取键
```

通过继承Enum的方式创建枚举

```python
class M(Enum):
    red = 1
    orange = 4


m = M(4)
print(m)
```

## 多继承

在python中，一个类可以继承多个类

有多个父类，按照优先级进行调用，使用方法mro查看类的结构时，会按照子类的继承顺序进行调用

```
查看继承的结构 类名.__mro__
```

```python
class Father:
    def work(self):
        print('父亲的工作')


class Mather:
    def work(self):
        print('母亲的工作')


class Children(Father, Mather):  # 有多个父类，多个父类有相同的方法，按照优先级进行调用
    def __init__(self, name):
        self.name = name

    def work(self):
        print('自己的工作')


c = Children('jk')
c.work()
print(Children.__mro__)  # 打印Children的继承结构，按照优先级
```

## 定制类

```
python中的常用魔术方法
__str__:自定义对象的描述信息
__call__:将对象变为一个函数，可调用
__iter__: 将对象变为一个可迭代对象
__next__:将对象变为迭代器
__getitem__:将对象变为list
__getattr__:重写错误信息
__del__:销毁对象，解释器会自动进行调用
__hash__:返回hash值
__repr__:类似于__str__方法
__new__:实例化对象
__eq__:比较两个对象是否相同
__init__:初始话对象属性
callable(obj)  判断对象是否可以进行调用，返回值为布尔
```

```python
from collections.abc import Iterator, Iterable


class Person:
    def __init__(self):
        self.name = '李梅'
        self.a, self.b = 0, 1

    # 将对象变为可迭代对象
    def __iter__(self):
        return self

    # 将对象变为迭代器
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        """
        将对象变为list
        需要进行判断传递进来的item是index[索引]还是slice[切片]
        :param item:
        :return:
        """
        # 如果是index
        if isinstance(item, int):
            self.a, self.b = 1, 1
            for _ in range(item):
                self.a, self.b = self.b, self.a + self.b
            return self.a

        # 如果是slice
        elif isinstance(item, slice):
            # 获取传进来的start和stop
            start = item.start
            stop = item.stop
            # 如果start为None，需要进行判断
            if start is None:
                start = 0

            self.a, self.b = 1, 1
            l = []
            for _ in range(stop):
                if _ >= start:
                    l.append(self.a)
                self.a, self.b = self.b, self.a + self.b
            return l

    def __call__(self, *args, **kwargs):
        """
        将类变为一个函数，允许被调用
        :param args:
        :param kwargs:
        :return:
        """
        print('Person进行了调用')

    def __getattr__(self, item):
        """
        如果访问类中没有的属性，会出现AttributeError错误，需要进行相应的处理,不让出现提示
        :param item:
        :return:
        """
        if item == 'age':
            return 15
        elif item == 'eat':
            return lambda: print('ok')


p = Person()
print(isinstance(p, Iterator))
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())
print('索引为2的元素：', p[2])

print('切片为2到5的元素：', p[2:9])
p()
print(p.age)
p.eat()
# callable判断对象是否可以进行调用
print(callable(p))
```

## 高阶函数

**内置的高阶函数**

map, filter,reduce, max, min, sorted

```
内置的高阶函数
map:将可迭代对象中的每一个元素转换为一个新的对象，返回一个迭代器
reduce:对可迭代对象进行聚合处理 ,返回一个聚合的值
filter:对可迭代对象进行过滤处理，为True留下，False去掉
max and min
sorted:对可迭代对象进行排序，返回一个list
```

```python
from functools import reduce
from collections.abc import Iterator, Iterable


def map_func():
    lst = [1, 2, 3, 4, 5]
    lst_ = map(lambda x: x ** 2, lst)
    return lst_


def reduce_func():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = reduce(lambda x, y: x + y, lst)
    return lst_


def filter_func():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = list(filter(lambda x: x > 4, lst))
    return lst_


def max_fun():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = max(lst, key=lambda x: x)
    return lst_


def min_fun():
    lst = [1, 2, 3, 4, 5, 5]
    lst_ = min(lst, key=lambda x: x)
    return lst_


def sorted_func():
    lst = [1, 2, 0, 4, 5, 5]
    lst_ = sorted(lst, key=lambda x: x)
    return lst_

# 高阶函数作为返回值
def return_func(*args, **kwargs):
    def f():
        for i in args:
            print(i)

    return f


lst = [1, 2, 0, 4, 5, 5]
l = return_func(lst)
l()
```

## 垃圾回收

Python的垃圾回收机制主要以引用计数为主，分代回收为辅。引用计算的原理是每一个对象都有一个obj_ref，这个obj_ref是用来记录当前对象的引用次数，用来追踪有多少引用指向了这个对象。下面的四种情况对象的引用计数加1

**引用计数加1**

- 对象被创建时  a=1
- 对象被引用 b=a
- 对象作为参数，传递到函数中 func(a)
- 对象存储在容器中，List=[1,2,a]

**引用计数减1**

- 对象的别名被回收 del a
- 对象的别名引用了新的对象 a=45
- 对象离开它的作用域。例如；函数执行完成后，函数里面的局部变量引用计数减1，全局变量会
- 对象从容器中删除，或者容器被销毁

**当指向该对象的内存的引用计数为0，Python虚拟机就会将其销毁**

Python里面每一个东西都是对象，核心是一个结构体Py_Object,所有对象的头部都包含了这个结构体

PyObject是每个对象必有的东西，ob_ref是用来进行引用计数，有了新的引用，ob_ref加1，引用的对象被删除，ob_ref减1

**引用计数的优点，缺点**

优点：

- 高效
- 运行期间没有停顿，实时性；没有引用，内存直接释放，处理回收内存多大时间分摊到了平时
- 对象有确定的生命周期
- 易于实现

缺点：

- 维护计数引用消耗资源，维护计数引用的次数和引用赋值成正比
- 无法解决循环引用的问题

为了解决这两种缺点，Python引用了两种GC机制

- **标记-清除**

  针对循环引用的情况：我们有一个“孤岛”或是一组未使用的、互相指向的对象，但是谁都没有外部引用。换句话说，我们的程序不再使用这些节点对象了，所以我们希望Python的垃圾回收机制能够足够智能去释放这些对象并回收它们占用的内存空间。但无法实现

  标记清除（Mark—Sweep）算法是一种基于追踪回收（tracing GC）技术实现的垃圾回收算法。它分为两个阶段：第一阶段是标记阶段，GC会把所有的『活动对象』打上标记，第二阶段是把那些没有标记的对象『非活动对象』进行回收。那么GC又是如何判断哪些是活动对象哪些是非活动对象的呢？

  对象之间通过引用（指针）连在一起，构成一个有向图，对象构成这个有向图的节点，而引用关系构成这个有向图的边。从根对象（root object）出发，沿着有向边遍历对象，可达的（reachable）对象标记为活动对象，不可达的对象就是要被清除的非活动对象。根对象就是全局变量、调用栈、寄存器。

  <img src="images\标记清除.svg" alt="laji" style="zoom:150%;" />

  在上图中，我们把小黑圈视为全局变量，也就是把它作为root object，从小黑圈出发，对象1可直达，那么它将被标记，对象2、3可间接到达也会被标记，而4和5不可达，那么1、2、3就是活动对象，4和5是非活动对象会被GC回收。

- **分代回收**

**gc的逻辑**

```
分配内存
-> 发现超过阈值了
-> 触发垃圾回收
-> 将所有可收集对象链表放到一起
-> 遍历, 计算有效引用计数
-> 分成 有效引用计数=0 和 有效引用计数 > 0 两个集合
-> 大于0的, 放入到更老一代
-> =0的, 执行回收
-> 回收遍历容器内的各个元素, 减掉对应元素引用计数(破掉循环引用)
-> 执行-1的逻辑, 若发现对象引用计数=0, 触发内存回收
-> python底层内存管理机制回收内存
```

分代回收是一种以空间换时间的操作方式，**Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），他们对应的是3个链表**，它们的垃圾收集频率与对象的存活时间的增大而减小。**新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，老年代中的对象是存活时间最久的对象**，甚至是存活于整个系统的生命周期内。同时，**分代回收是建立在标记清除技术基础之上**。分代回收同样作为Python的辅助垃圾收集技术处理那些容器对象.

```
Python垃圾回收详解
	https://blog.csdn.net/xiongchengluo1129/article/details/80462651
Python垃圾回收源码解读
	https://wklken.me/posts/2015/09/29/python-source-gc.html
Python的垃圾回收机制
	https://foofish.net/python-gc.html
	https://www.jianshu.com/p/1e375fb40506
```

Python中查看对象的引用计数

```python
import sys
sys.getrefcount(obj_name)
```

lg:

```python
import sys


class TestObject:
    def __init__(self):
        # hex 十六进制
        print(f'当前对象已被创建，当前对象的地址是{hex(id(self))}')


a = TestObject()
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
b = a
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
```

