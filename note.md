# Python学习笔记

# 目录

## [CH2 变量名和数据类型](#ch2-变量名和数据类型)
- [2.3 字符串](#23-字符串)
- [2.4 数](#24-数)

## [CH3 列表](#ch3-列表)
- [3.1 什么是列表](#31-什么是列表)
- [3.2 操作列表](#32-操作列表)
- [3.3 管理列表](#33-管理列表)

## [CH4 操作列表](#ch4-操作列表)
- [4.1 遍历列表](#41-遍历列表)
- [4.2 缩进](#42-缩进)
- [4.3 创建数值列表](#43-创建数值列表)
- [4.4 列表的一部分](#44-列表的一部分)
- [4.5 元组 (Tuples)](#45-元组-tuples)
- [4.6 PEP 8：代码格式](#46-pep-8代码格式)

## [CH5 if语句](#ch5-if语句)
- [5.2 条件测试](#52-条件测试)
- [5.3 if语句](#53-if语句)
- [5.4 if语句处理列表](#54-if语句处理列表)

## [CH6 字典](#ch6-字典)
- [6.2 使用字典](#62-使用字典)
- [6.3 遍历字典](#63-遍历字典)

## CH2 变量名和数据类型
### 2.3 字符串
#### `title()`方法
`title()`方法可以用于字符串对象，输出字符串每个单词的首字母大写形式。方法常用于格式化标题，句子或者人名。
```python
print("jason rao".title())
```  
#### 字符串插入变量
字符串插入变量值，在引号前加上字母f（formatted的缩写），再将要插入的变量放在大括号内。
```python
print(f"Hello, {first_name} {last name}!")
```
#### C风格格式输出
C风格字符串格式输出：`"格式化字符串" % (变量1, 变量2, ...)`
```python
print("Hello, %s %s!" % (first_name.title(), last,name.title()))
```
#### 删除空白方法`strip()`
`strip()`方法可以找出字符串两端多余的空白。`lstrip()`和`rstrip()`分别用于找出左侧和右侧的空白。  
该方法不会修改原字符串。若要修改原字符串，将方法赋值给原字符串即可。
```python
my_name = my_name.strip()
```
#### 删除前缀方法`removeprefix()`
`removeprefix()`方法接收一个前缀字符串作为参数，该方法施加的字符串若含参数前缀字符串，则前缀被删除。不会修改原字符串。
```python
url = 'https://www.google.com'
print(url.removeprefix('https://'))
```
以上代码执行后会输出`www.google.com`  
类似的，`removesuffix()`方法可以删除给定的后缀。

### 2.4 数
#### 乘方运算
Python用双乘号`**`表示乘方运算，例如2的3次方表示为`2**3`
#### 浮点数
在Python中，两个数相除的结果**默认通过浮点数表示**。该行为在`PEP 238`提案中被确认，是为了使得`/`操作符的统一性，一致地执行真除法，而不是像在python2中整数相除执行地板除法。
#### 下划线表示多位数
书写很大的数字的时候可以使用下划线将位进行分组，使得数字清晰易读。python在内部实现并不会特殊看待，因此这种行为更像是注释的一种。
```python
universe_age = 14_000_000_000
print(universe_age)
```
上面的代码段执行后会输出`14000000000`
#### 多个变量同时赋值
```python
x, y, z = 1, 2, 3
```
#### 常量
python没有内建的常量类型。程序员应该使用全大写指出某个变量视为常量。

#### 注释
python注释使用`#`为开头进行表示，约定俗成`#`号后需要有空格。

## CH3 列表
### 3.1 什么是列表
**列表**是一系列**顺序排列**的元素组成的数组。在python中方括号`[]`表示列表，**逗号**分隔其中的元素。
```python
student = ['sname', 'sid', 'sgrade']
```
基于以上的代码，若让python直接打印该列表`print(student)`，python会输出列表的内部表示形式而不是用户期望的输出。
```python
# 实际输出
['sname', 'sid', 'sgrade']

# 期望输出
sname, sid, sgrade
```
### 3.2 操作列表
#### 访问列表元素
通过索引访问列表的元素。python和C语言一样，索引**从0开始**。特别的，通过指定索引为-1，可以访问最后一个列表元素，类似的，索引-2访问倒数第2个元素。

#### 修改列表元素
通过指定索引修改列表元素。
```python
student[0] = 'sid'
```
上面的代码将`student[]`第一个元素修改为`sid`。

#### `append()`方法：追加元素
列表的`append()`方法可以在列表的末尾添加元素。
```python
student.append('course')
```
上面的代码在student列表最后添加了元素`'course'`。

#### `insert()`方法：插入元素
```python
student.insert(0, 'course')
```
上面的代码在索引为0的位置插入元素`'course'`。

#### del关键字
利用关键字del的语句，可以通过指定索引删除任意位置的元素。
```python
del student[0]
```
上面的语句删除`student[0]`元素。

#### `pop()`方法：返回指定位置元素值后弹出元素
```python
pop_element = student.pop()
```
上面的代码将`student[]`的最后元素存储在`pop_element`中，然后将该元素弹出。  
```python
pop_element = student.pop(0)
```
上面的代码将`student[0]`存储在`pop_element`中，然后将该元素弹出。  
通过`pop()`方法，可以利用列表实现队列和栈。

#### `remove()`方法：根据值删除元素
```python
student.remove('sid')
```
上面的代码执行后会删除`student[]`中**第一个**满足值为`'sid'`的元素。  
***注意：***`remove()`方法只会删除第一个值为给定参数的元素。若想删除所有满足条件的元素，需要利用循环。

### 3.3 管理列表
#### `sort()`方法：对列表进行永久排序
```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
```
上面的代码会对`cars[]`进行字典序从小到大排序。
```python
cars.sort(reverse = True)
```
若需要进行从大到小的排序（逆序排序），则向`sort()`方法传递参数`reverse = True`即可。  
**特别需要注意的是**，`sort()`方法对列表**永久排序**，该操作不可逆。

#### `sorted()`函数：对列表进行临时排序
*注意：`sorted()`是函数，直接把列表作为参数放入即可。*
```python
sorted_list = sorted(cars)
```
上面的代码将排序结果存储到`sorted_list[]`中，但是不会修改原列表。  
*记忆方法：sort更短，因此操作直接原地修改。sorted更长，因此需要复制新的列表，排序才能不改变原列表。*

#### `reverse()`方法：永久反转列表
```python
cars.reverse()
```
上面的代码将`cars[]`逆序储存。若想恢复原样，只需要再执行一次`reverse()`方法即可。

#### `len()`函数：确认列表的长度
*注意：`len()`是函数而不是方法，因此直接将列表名作为参数放入即可。*
```python
len(cars)
```
上面的代码会输出`cars[]`的长度4。

## CH4 操作列表
### 4.1 遍历列表
#### 简单for循环打印
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```
for循环的第一行代码`for magician in magicians:`中，`magician`是与循环列表每个值相关联的临时变量，可以取任何名称，但是建议选择与描述单个列表元素相关的名称。比如`for cats in cat:`, `for dog in dogs:`, `for item in item_lists:`  

### 4.2 缩进
for循环的循环体通过缩进标识，缩进结束表示循环结束。

### 4.3 创建数值列表
#### `range()`函数
`range()`函数用于生成一系列的数。  
python代码：
```python
for cnt in range(a, b):
    ...
```
等价于C/C++代码：
```c
for (int cnt = a; cnt < b; cnt++) {
    ...
}
```
`range(a, b)`可以理解为生成了一个[a, b-1]的列表并循环遍历,但是实际上是生成了一个**迭代器**。  
`range(0, a)`可以简写为`range(a)`。

#### `range()`+`list()`创建数值列表
`list()`函数可以直接将`range()`函数的结果转换为列表。
```python
list(range(a))
```
上面的代码会生成一个长度为a，大小[0, a - 1]的列表

`range()`可以创建第三个参数用于指定步长，即`range(a, b, step)`  
python代码：
```python
for cnt in range(a, b, step):
    ...
```
等价于C/C++代码：
```c++
for (int cnt = a; cnt < b; cnt += step) {
    ...
}
```

#### 数值列表的统计计算
`min()`函数找出数值列表的最小值，`max()`函数找出数值列表最大值，`sum()`函数对数值列表进行求和。

#### 列表推导式
```python
squares = [value ** 2 for value in range(10)]
```
以上代码等价于：
```python
squares = []
for value in range(10):
    squares.append(value ** 2)
```
`value ** 2 for value in range(10)`代表将`range(10)`逐个元素提供给表达式`value ** 2`  
*注意：这里的`for`语句末尾没有冒号。*

### 4.4 列表的一部分
通过python的切片功能，可以对列表的部分元素进行处理。
#### 切片
可以通过指定要使用的第一个元素和最后一个元素的**索引**创建切片。
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```
上面的代码会输出`players[]`的索引0，1，2三个元素。  

如果没有指定切片的第一个索引，自动从列表开头开始。比如`players[:4]`等价于`players[0:4]`。要让切片终止于列表结尾，可以采用类似语法。

索引也可以使用负数。比如`players[-3:]`表示提取最后三个元素。

#### 遍历切片
```python
for player in players[-3:]:
    print(player)
```
上面的代码只会打印最后三个球员的名字。

#### 复制列表
***注意：直接通过列表名进行赋值，比如`list_a = list_b`是引用赋值，本质是将`list_a`和`list_b`两个别名同时关联到同一个列表上。修改list_a的内容会直接影响list_b。***

如果只是根据既有的列表创建**全新**的列表，可以通过起始和终止索引均省略的切片创建。
```python
list_a = [1, 2, 3]
list_b = list_a[:]
```
上面的代码将`list_a[]`的元素复制到了`list_b[]`，对`list_a[]`的修改和`list_b[]`的修改互不干预。

### 4.5 元组 (Tuples)
元组是不可以修改元素值的列表。

元组和列表的定义很相似，只是将列表的方括号改为圆括号即可。比如`dimensions = (200, 50)`定义了一个长度为2的元组。

**注意**：元组是由逗号标识的，因此在创建单元素元组时必须加上逗号。比如`dimensions = (200,)`。

#### 遍历元组
跟列表一模一样。

#### 修改元组变量
元组变量名表征的元组内的元素不可变，但可以通过给整个元组重新赋值来重新定义整个元组。
```python
dimensions = (200, 50)
dimensions = (100, 100)
```
以上的操作是被允许的，而下面的操作则不被允许：
```python
dimensions = (200, 50)
dimensions[0] = 100
```
综上所述，在存储生命周期内元素值不变的列表，可以使用元组。

### 4.6 PEP 8：代码格式
1. **缩进**：每级缩进采用4个空格缩进。在使用Tab缩进时，必须设置成将制表符转换为指定数量的空格模式。
2. **行长**：每行代码建议不超过80个字符，注释的行长建议不超过72个字符
3. **空行**：**绝对应该**使用空行组织程序，但是不要滥用空行。python解释器根据水平缩进解读代码，不关心垂直间距。

## CH5 `if`语句
```python
if 布尔表达式:
    ...
```
忽略大小写的检查：`car.lower() = 'audi'`
### 5.2 条件测试
#### 检查多个条件
1. `and`关键字：两个条件为`True`时表达式为`True`，否则为`False`。
2. `or`关键字：只要有条件为`True`，则表达式为`True`。

#### `in`关键字：检查特定的值是否在列表或元组中
```python
list_1 = [1, 2, 3, 4]
1 in list_1
tuple_1 = (1, 2, 3, 4)
1 in tuple_1
```
上面的代码会输出两个`True`。

类似的，`not in`关键字可以检查特定的值是否不在列表或元组当中。

### 5.3 `if`语句
#### `if-else`语句
```python
if 条件语句:
    ...
else:
    ...
```

#### `if-elif-else`语句
```python
if 条件语句1:
    ...
elif 条件语句2:
    ...
else:
    ...
```
在明确`else`会执行的情况的时候，建议将`else`替换为`elif`及`else`执行的相关条件语句，使得代码逻辑更加清晰。

### 5.4 `if`语句处理列表
#### 检查列表元素
```python
sids = [0, 1, 2, 0, 5]
for sid in sids:
    if sid == 0:
        print("sid error!")
    else:
        print(sid)
```

#### 检查列表非空
```python
sids = []
if sids:
    ...
else:
    print("Empty list!")
```
**注意**：对于数值`0`，空值`None`，空字符串`''`，空列表`[]`，空元组`()`，空字典`{}`，在条件语句当中python都会返回`False`。

## CH6 字典
可以从表面上把字典理解为索引不局限为整数的列表。下面的代码定义了一个简单的字典，并通过键访问字典的值：
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
```

### 6.2 使用字典
字典的本质是一系列的**键值对**，每个键都与一个特定的值关联，可以使用键来访问与之关联的值。任意的python对象都可以作为字典的值。

既然键是作为索引，因此键不可以重复。但值可以重复

键和值之间用冒号分隔，键值对之间用逗号分隔。字典可以储存任意任意数量的键值对。
#### 访问字典的值
```python
# 字典名[键名] = 值
print(alien_0['color'])
```

#### 键值对的添加
字典是动态结构，可以随时添加键值对。
```python
alien_0['x_posision'] = 0
alien_0['y_posision'] = 25
```
上面的代码给字典`alien_0`添加了两个键值对。

#### 键值对的修改
```python
alien_0['x_posision'] = 10
```
上面的代码将键为`'x_posision'`的对应值修改为10

#### `del`关键字：键值对的删除
```python
del alien_0['color']
```
上面的代码将`alien_0`字典中键为`'color'`的键值对**永久删除**。

#### `get()`方法：访问有可能不存在的键
*在用方括号访问字典中不存在的键的时候，若指定的键不存在，则会引发错误。*  

`get()`方法可以接收两个参数，第一个参数是要访问的键，第二个参数（可选）是若要访问的键不存在于字典时返回的值（可选）。若第二个参数不给出，在访问字典中不存在的键的时候会输出`None`。
```python
print(alien_0.get('z_posision', 'z posision not included!'))
```
若`z_posision`键不存在的话，上面的代码会输出`z posision not included!`

### 6.3 遍历字典
#### `items()`方法：遍历键值对
对字典施加`items()`方法会生成字典的**键值对列表**
```python
for key, value in alien_0.items():
    print(f"key: {key}, value:{value}")
```
上面的代码会遍历字典的键值对并分别输出键和值。

#### `keys()`方法：遍历字典键
对字典施加`keys()`方法会生成字典的**键列表**
```python
for key in alien_0.keys():
    print(key)
```
上面的代码会遍历字典的键并循环输出所有的键。

*注意：直接对字典遍历时，默认遍历字典的键。因此：*
```python
for key in alien_0:
    ...
```
和
```python
for key in alien_0.keys():
    ...
```
上面两段代码是等价的代码。实际运用中，推荐显式使用`keys()`方法。
#### `values()`方法：遍历字典值
对字典施加`values()`方法会生成字典的**值列表**
```python
for value in alien_0.values():
    ...
```
如果需要对字典的值进行无重复的访问，可以借助集合`set`，`set`要求所有的元素不能重复存在。`set()`函数可以生成列表对应的集合（筛选掉列表中重复的元素）。
```python
for value in set(alien_0.values()):
    ...
```
#### 集合：`set`
集合使用一对花括号直接创建，并在其中用逗号直接分隔元素。不同于字典以及列表，集合**不以特定的顺序存储元素。**
```python
my_set = {1, 2, 2, 3}
my_set
```
上面的代码输出`{1, 2, 3}`。

### 6.4 嵌套
...

## CH7 用户输入和`while`循环
### 7.1 `input()`
`input()`函数可以让程序暂停运行，等待用户输入，并将输入赋值给一个变量以供使用。`input()`函数接收一个参数，即要向用户显示的提示信息。

```python
age = input("Please input your age: ")
print(f"Your age is {age}.")
```

#### 编写清晰的提示
以下是对编写清晰的提示的一些建议。  
1. 在提示的末尾添加空格，以将提示与用户输入分开，让用户知道其输入从何处开始。
2. 若提示超过一行，可以通过多次赋值给提示词变量的方式使`input()`语句变得清晰。
```python 
prompt = "Hello! This is Jason, welcome to my program!"
prompt += "\nIf you meet with any problem, please contact me! What's your name? "
name = input(prompt)

```

#### `int()`函数用于转换数值输入
**注意：**在使用`input()`函数时，python会将输入解释为**字符串**。通过`int()`函数，我们可以将数字字符串（如“12”）转换为数字。
```python
age = int(input("Please input your age: "))
type(age)
```
上面的代码运行后会显示`<class 'int'>`，代表成功转换输入格式为整型数字格式。

#### 求模运算符`%`
`a % b`返回`a`整除`b`后的余数。若可以被整除，则返回`0`。

### 7.2 `while`循环
```python
while 条件语句:
    ...
```
只要条件语句成立，python就会一直执行条件语句冒号后缩进部分的语句。

#### `break`关键字：退出循环
`break`关键字会立即退出循环，不再运行剩下的代码。`break`关键字不仅可以用于`while`循环，也可以用于`for`循环。

#### `continue`关键字：继续执行循环
在循环体内，`continue`关键字后面的部分在该次循环会被忽略，然后进入下次循环。

### 7.3 `while`循环处理列表和字典
#### 删除特定值的所有列表元素
`remove()`方法可以删除第一个列表中的参数元素，`remove()`方法和`while`语句结合可以删除特定值的所有列表元素。
```python
pets = ['cat', 'dog', 'wolf', 'fish', 'lion', 'tiger']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```
`while 'cat' in pets:`语句在`pets[]`中仍然有`'cat'`元素的时候持续执行删除`'cat'`元素的行为，并在列表中不含有`'cat'`元素的时候停止执行。

## CH8 函数
### 8.1 定义函数
```python
def greet_user():
    """display greeting"""
    print("Hello!")

greet_user()
```
`def greet_user():`整体为函数定义，紧跟在后面的所有缩进行构成函数体。

紧跟在函数定义后的`"display greeting"`文本称为**文档字符串**（docstring），用于描述函数的功能。python在为函数生成文档时，会查找紧跟在函数定义后的文档字符串。

通过`help()`函数，可以显示函数的文档字符串。 

#### 函数传参
```python
def greet_user(username):
    message = f"Hello, {username}!"
    print(message)

greet_user("Jason")
```

#### 实参vs形参
函数定义的时候，参数列表中的参数是**形参**，而在函数调用的时候，传入函数列表的参数是**实参**。

比如在上面的例子当中，`username`是形参，`Jason`是实参。

### 8.2 传递实参
#### 位置实参
**位置实参**指基于参数列表中形参的顺序和实参传入的**顺序**进行关联。比如：
```python
def introduction(name, job):
    message = f"My name is {name}, I am a {job}."
    print(message)


introduction("Jason", "student")
```
上面的代码会输出`My name is Jason, I am a student.`。

#### 关键字实参
**关键字实参**指直接将实参的值和形参名称关联起来。关键字实参使得无需考虑函数调用的实参顺序，并且在参数列表当中清楚地指出了函数调用各个值的用途。
```python
def introduction(name, job):
    message = f"My name is {name}, I am a {job}."
    print(message)

introduction(job="student", name="Jason")
```
上面的代码会输出`My name is Jason, I am a student.`。

**注意：**在使用关键字实参的时候，务必准确指定函数定义的形参名。

#### 参数默认值
可以在函数定义时为形参指定默认值。调用函数时若提供实参，则使用指定实参值，否则使用形参的默认值。

**注意**：在定义函数的时候应该把含默认值的形参放在参数列表的后面，不含默认值的形参放在参数列表的前面。这样可以保证在通过位置实参和关键字实参调用函数的时候python都可以正确解读参数。
```python
def introduction(job, name="Jason"):
    message = f"My name is {name}, I am a {job}."
    print(message)
introduction("student")
introduction(job="student")
```
由于默认参数放在参数列表的后面，所以上面的两种方式都可以正常调用`introduction()`函数。

#### 等效函数调用
...

#### 避免实参错误
...

### 8.3 返回值
```python
def name(first_name, last_name):
    full_name = (first_name + ' ' + last_name).title()
    return full_name

my_name = name("Jason", "Rao")
print(my_name)
```

#### 可选实参
可以通过默认值来让实参变成可选实参。**注意**：此时带默认值的实参需要放在参数列表末尾。

#### 函数返回字典
```python
def name(first_name, last_name):
    full_name = {'first_name': first_name, 'last_name': last_name}
    return full_name

my_name = name("Jason", "Rao")
print(my_name)
```

#### 列表作为参数
```python
def greet(guests):
    for guest in guests:
        message = f"Hello {guest}! Welcome to my home!"
        print(message) 

guests_list = ['Jason', 'Timmy', 'Lucy', 'Vicky']
greet(guests_list)
```

#### 函数中修改列表
将列表作为参数传输给函数后，就可以在函数当中对列表进行修改。在函数中对列表的修改是**永久的**。

#### 禁止函数修改列表
可以通过将列表的副本作为参数传输给函数，防止函数内部未经授权对列表的修改。
```python
function_name(list_name[:])
```
其中，`list_name[:]`表示列表`list_name`的全切片，即列表的副本。在复制列表的时候也采用这种方式进行复制。

### 8.5 传递任意数量的实参
在一些函数当中，可能需要传递任意数量的实参。也有可能你预先不知道函数需要接受多少实参。

```python
def greet(*guests):
    print(guests)

greet('Jason', 'Lucy', 'Timmy', 'Vicky')
```
其中，`*guests`表示创建一个名为`guests`的元组，包含函数收到的所有值。

#### 位置实参和任意数量的实参结合
如果需要将位置实参和任意数量实参进行结合，则位置实参需要放在参数列表的开头，任意实参`args`需要放在参数列表的末尾，从而保证python可以正确读取参数列表。
```python
def greet(my_name, *guests):
    for guest in guests:
        message = f"Hello {guest}! I am {my_name}, welcome to my home!"
        print(message)

guests = ('Timmy', 'Lucy', 'Vicky')
greet('Jason', *guests)
greet('Jason', 'Timmy', 'Lucy', 'Vicky')
```
在上面的代码当中，`greet('Jason', *guests)`和`greet('Jason', 'Timmy', 'Lucy', 'Vicky')`的作用是一样的。

也就是说，如果直接将元组名作为参数传入任意数量形参设置的函数，需要先对其进行解包`*`再传入函数。

在标准python代码当中，任意数量位置参数实参常常用`*args`表示。

#### 任意数量的关键词实参
在预先不知道传递给函数的是什么样子的信息的时候（不知道传入参数的具体含义），可能需要使用到字典作为任意数量关键词实参的载体。

```python
def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('Albert', 'Einstein', location='Priceton', field='Physics')
```
`**`引导的变量名在参数，会在函数的作用域当中创建一个以该参数为名的字典。在上面的代码当中，`Albert`和`Einstein`是固定的前两个实参，后面的键值对则会被加入到`user_info`字典当中。

**注意**：
1. 在参数列表当中，字典的键不需要加引号。python默认将等号左侧转换为字符串形式的键。
2. 在标准python代码当中，常常将`**kwargs`用作形参名，指收集任意数量的关键字实参。`kwargs`是`keyword arguments`的缩写。

### 8.6 将函数存储在模块当中
#### 导入整个模块
**模块**是扩展名为`.py`的文件，包含了要导入程序的代码。比如我定义了如下的函数:  
*greet.py*
```python
def greet():
    print("Hello! Welcome to my home!")
```
那么在另外一份代码当中，如果我想使用这个函数，可以`import greet`从而导入该函数：
```python
import greet
greet()
```
具体来说，`import module`操作会让python在执行`import`的代码中打开`module.py`文件，并将`module.py`中的所有内容都复制到`import`该模块的代码当中。通常我们看不到复制代码的过程，因为python解释器会在程序即将运行的时候在幕后复制这些代码。




