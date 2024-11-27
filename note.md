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

**注意：**`for magician in magicians`中只是将`magicians`列表中的每个元素依次赋值给临时变量`magician`，`magician`只是保存了元素的副本，因此对`magician`进行修改并不会导致原列表的改变。如果需要修改原列表，只能通过下标索引方法访问元素并修改。
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
def greet_guests():
    print("Hello! Welcome to my home!")
```
那么在另外一份代码当中，如果我想使用这个函数，可以`import greet`从而导入该函数：
```python
import greet
greet.greet_guests()
```
具体来说，`import module`操作会让python在执行`import`的代码中打开`module.py`文件，并将`module.py`中的所有内容都复制到`import`该模块的代码当中。通常我们看不到复制代码的过程，因为python解释器会在程序即将运行的时候在幕后复制这些代码。

如果要调用被导入模块当中的函数，需要指定被导入模块的名称`module_name`和函数名称`function_name`，并用句点隔开，比如`module_name.function_name()`,`greet.greet()`。

#### 导入特定的函数
可以只导入特定模块的特定函数，语法如下：
```python
from module_name import function_name
```
用逗号分隔函数名，可以根据需要从模块当中导入任意数量的该模块当中的函数。
```python
from module_name import function_1, function_2, function_3
```
使用上面的语法的时候，不需要在调用函数的时候使用句点，而只需要指定其名称即可。比如下面的实例：
```python
from greet import greet_guests
greet_guests()
```

#### 使用`as`为模块指定别名
**注意**：`as`关键字指定别名的对象是**模块**而不是函数。使用`as`指定别名的通用语法如下：
```python
import module_name as mn
```
为模块指定别名不会改变模块内函数的函数名，还会使得代码更加简洁，使得程序员不需要关注模块名，只专注于描述性的函数名。

#### 导入模块中的所有函数
使用**星号（*）**运算符可以导入模块中的所有函数。
```python
from module_name import *
```
但是无论如何，**强烈不推荐**在自己的代码当中使用这种特性。原因同C++中不推荐使用`using namespace std;`一样。

### 8.7 函数编写指北
编写函数的时候，需要牢记下面的一些细节：
1. 应给函数指定描述性名称，且名称只使用小写字母和下划线
2. 每个函数都应该包含简要阐述其功能的注释。注释需要紧跟在函数定义的冒号后一行，采用文档字符串的形式。
3. 给函数形参指定默认值的时候，不要像往常一样在等号两侧加上空格。`def function_name(parameter_0, parameter_1='default value')`是正确的写法。
4. PEP 8 建议代码每行的长度不要超过79个字符。如果形参过多导致函数定义长度超过了79个字符，可以采用下面的写法：
```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```
5. 如果程序或者模块包含多个函数，则应该使用两个空行将相邻的函数分开。
6. 所有的`import`语句都应该放在代码文件的开头，例外是文件开头需要使用注释描述整个程序。

## CH9 类
**面向对象编程**（object-oriented programming，OOP）是最有效的程序编写方法之一。在OOP中，我们编写表示现实世界事物和情景的**类**，并基于这些类创建**对象**。

根据类创建对象的行为称为**实例化**。

### 9.1 创建和使用类

#### 创建类
```python
class Dog:
    """Simulation of dog class"""

    def __init__(self, name, age):
        """Initialize attributes name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting when asked"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate dog rolling when asked"""
        print(f"{self.name} is now rolling.")
```
根据约定，在python当中，首字母大写的名称指的是类。然后紧跟文档字符串，用于描述这个类的功能。

##### __init__方法
类中的函数称为**方法**，有关函数的一切基本都适用于方法，唯一的区别是调用的方式。`__init__()`是一个特殊方法，每次根据类创建新的实例的时候都会自动运行该方法。

**注意**：
1. `__init__()`方法的名称开头和末尾各有两个下划线，这是python的约定，用于将默认方法和普通方法发生名称冲突。
2. `__init__()`方法的定义当中，形参`self`必不可少，并且必须位于参数列表第一位。

【Tips】为什么必须在`__init__()`方法定义中包含形参`self`？因为当python调用`__init__()`方法创建实例的时候，会自动传递实参`self`，即一个指向实例本身的引用，让实例可以访问类中的属性和方法。

在`__init__()`方法内定义的变量称为**属性**，这些属性需要带有前缀`self`，可供类中的所有方法使用。`self.name = name`获取形参`name`的值并赋给属性`name`。

#### 创建实例
```python
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
```

##### 访问属性
```python
my_dog.name
```

##### 调用方法
```python
my_dog.sit()
my_dog.roll_over()
```

### 9.2 使用类和实例

#### 给属性指定默认值
```python
class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        --snip--
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```
对于上面的代码，python在创建`Car`类的实例的时候，会自动创建名为`odometer_reading`的属性，并将其**初始值**设置为0。

#### 通过方法修改属性的值
```python
class Car:
    --snip--

    def update_odometer(self, new_value):
        if new_value >= self.odometer_read:
            self.odometer_read = new_value
        else:
            print("You can't roll back an odometer!")
```
通过上面的方法修改里程数属性的时候，方法会检查新读数是否合理，并在不合理的时候给出警告。

### 9.3 继承
#### 子类的`__init__()`方法和子类的属性
```python
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        
        """初始化子类的属性"""
        self.battery_size = 40
    
    """子类的方法"""
    def describe_battery(self):
        """打印描述电池的信息"""
        print(f"The size of the battery is {self.battery_size}".)
        
```
在创建子类的时候，父类必须包含在当前同一个文件当中，并且位于子类的前面。定义子类的时候，必须在括号内指定其父类的名称。

`super()`函数是一个特殊的函数，用于调用父类的方法。父类又称为**超类**（superclass）。`super().__init()`使得子类调用了父类的初始化方法用于初始化子类的属性。

#### 重写父类的方法
有些情况，父类的方法不能满足子类的需求，就需要对父类的方法进行重写。只需要在子类的类内重新定义一次父类的方法，重写方法体，则在对子类调用该方法的时候python会自动使用子类版本而非父类版本。

#### 将一个类的实例用作另一个类的属性
```python
class Car:
    --snip--
    
class Battery:
    """一次模拟电动汽车电池简单尝试"""

    def __init__(self, battery_size=40):
        """初始化电池的属性"""
        self.battery_size = battery_size
        
        def describe_battery(self):
            """打印一条描述电池容量的消息"""
            print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_car = ElectricCar('bmw', '520Li', 2024)
```
在上面的代码示例当中，`ElectricCar`类初始化方法当中的`self.battery = Battery()`含义是在初始化`ElectricCar`类的时候，将一个`Battery`类的实例赋值给`ElectricCar`类的`battery`属性。

在调用`ElectricCar`类的`battery`相关属性和方法的时候，可以像这样：`my_car.battery.battery_size`。

### 9.4 导入类
python允许将类存储在模块当中，然后在主程序中导入所需的模块。

#### 导入单个类
*car.py*
```python
❶"""一个用来表示汽车的类"""

class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """返回格式规范的描述性名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条消息，指出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer += miles
```
❶处是一个模块级的文档字符串。应该为创建的每个模块都编写文档字符串。

在另外一个文件当中，导入模块`car`中的`Car`类，并创建一个实例：
```python
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```
导入类的一般性语句为：`from module_name import class_name`，其中`module_name`为包含该类代码的文件名。

#### 在一个模块当中存储多个类
...

#### 从一个模块当中导入多个类
从一个模块导入多个类的时候，用逗号分隔开各个类。一般性语句为：`from module_name import class_1, class_2, ...`

#### 导入整个模块
可以先导入整个模块，再利用“模块名+点号+类名”访问所有需要的类。
```python
import car

my_bmw = car.Car('bmw', '520Li', 2024)
my_audi = car.Car('audi', 'A8L', 2024)
```
使用的一般性语句为：`module_name.class_name`

#### 导入模块的所有类
可以使用下面的语法导入模块当中的所有类：
```python
from module_name import *
```
星号（*）表示某一个模块下面的所有类。  
**注意**：不推荐这种写法，可能会产生命名冲突。

#### 使用别名
可以使用以下的语法给类指定别名
```python
from electric_car import ElectricCar as EC
```
在指定了上面所指示的别名后，需要创建电动汽车的时候，可以指定别名`EC`。
```python
my_bmw = EC('bmw', '520Li', 2024)
```
此外，还可以给模块指定别名。
```python
import electric_car as ec
```
这样，下面使用该模块内的类的时候，可以采用如下的语法：
```python
my_bmw = ec.ElectricCar('bmw', '520Li', 2024)
```

### 9.5 python标准库
**python标准库**是一组模块，在安装python的时候已经包含在内。
#### `random`标准库
##### 1. `randint()`函数
`random`标准库中的函数`randint()`可以将两个整数作为参数，随即返回位于两个整数之间（含）的整数。
```python
import random
random_number = random.randint(1, 6)
```
上面的代码会生成一个`1 <= random_number <= 6`的整数。

##### 2. `choice()`函数
`random`标准库中的函数`choice()`可以接收一个列表或者元组作为参数，并随机地返回其中的一个元素。
```python
import random
guests_list = ['Jason', 'Timmy', 'Lucy', 'Vicky']
lucky_guest = random.choice(guests_list)
```

### 9.6 类的编程风格
1. 类名应该采用**驼峰命名法**，即类名中的每个单词的首字母都大写，并且**不使用下划线**。
2. 实例名和模块名都采用**全小写格式**，单词之间需要加上**下划线**。
3. 可以使用空行组织代码，但是不宜使用过多的空行。类中使用一个空行分隔方法，模块中使用两个空行来分隔类。
4. 需要同时导入 python 标准库中的模块和其他外部模块的时候，先编写导入标准库模块的`import`语句，再添加一个空行，然后编写其他外部模块的导入语句。

## CH10 文件和异常
**异常**是python创建的特殊对象，用于管理程序运行时出现的错误。

### 10.1 读取文件
#### 读取文件的全部内容
```python
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read.txt()
print(contents)
```
若需要获取文件的内容，首先要将文件的路径告知python。python使用库`pathlib`来轻松地处理文件和目录。

首先导入`pathlib`中的`Path`类。`Path`类用文件路径作为参数实例化后的对象指向该文件。`Path`类的方法`read_text()`会读取该文件的所有内容并作为一个字符串返回。

**注意**：
1. `read_text()`方法在读取到文件末尾时会返回一个空字符串，因此读取的内容相比原内容会增加一个空行。可以通过`rstrip()`方法删除多余的空行。
2. Windows的系统文件路径使用反斜杠（`\`），但是在python中所有路径一律采用**斜杆**（`/`）。
3. 直接将`Path`类在`print()`函数中输出，会输出该路径指向的文件名。

#### `splitlines()`方法
`splitlines()`方法是python的一个内置字符串方法，目的是将字符串存储到列表中，其中每行单独存储为列表的一个元素。

#### 大型文件
python没有对可处理的数据量有任何的限制，因此只要系统内存足够大，python可以处理无穷多的数据量。

若某个文件包含百万级别的数据量，为了不让终端花时间滚动显示数据，可以使用切片处理部分数据。

### 10.2 写入文件
定义了一个文件的路径之后，可以使用`Path`类的`write_text()`将数据写入文件当中。写入文件的顺序和`read_text()`方法读取文件的顺序几乎相同。

`write_text()`方法接收一个字符串作为参数，该方法会将字符串写入文件当中。

**注意**：
1. python只能将字符串写入文本文件当中，如果要将数值结果存放到文本文件当中，则需要通过`str()`函数将数值结果转换为字符串后再存放到文本文件当中。
2. 如果文件本身有内容，那么`write_text()`方法会覆盖文件原本的内容，而不是在文件后面追加内容。文件原本的内容将会被删除并且不可被恢复。

### 10.3 异常
python使用称为**异常**（exception）的对象来管理python运行过程当中出现的错误。

每当发生python错误的时候，python会创建一个异常对象。如果程序员提前编写了处理该异常对象的代码，程序将按编写好的处理程序继续运行。

如果程序员未对该类型的异常进行处理，程序将停止并显示一个令人费解的`traceback`，其中包含异常报告。

异常使用`try-except`代码块处理。`try-except`代码块让python执行指定的操作，并告诉python发生错误时的做法。在`try-except`代码块内，即使出现异常，程序仍将继续运行，显示程序员编写的错误信息，而不是迷惑的`traceback`信息。

#### `try-except`代码块
下面是一个处理`ZeroDivisionError`异常的`try-except`代码：
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

#### 异常避免崩溃
若可能出现崩溃的代码没有采用异常处理措施，在崩溃时出现的`traceback`错误信息也许会让用户迷惑。而一些训练有素的用户则会通过`traceback`获取一些你不想让他们知道的信息，比如部分代码段以及代码文件名。

#### `else`代码块
可以在`except`代码块后放入代码，这些代码只有在`try`代码块内的代码成功运行的时候才会执行。即只有`try`代码块成功执行才需要执行的代码，都需要放到`else`代码块当中。

#### `FileNotFoundError`异常
```python
from pathlib import Path

path = Path('alice.txt')
try:
    path.read_text(encoding='utf-8')
except FileNotFound:
    print(f"Sorry, the file {path} does not exist.")
```

#### 分析文本
`split()`方法默认以空白为分隔符将字符串拆分成多部份，组成一个列表。通过统计这个列表的长度，可以粗略估计一个字符串当中有多少个单词。
```python
from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    word_count = len(content.split())
    print(f"The file {path} contains about {word_count} words.")
```

#### 使用多个文件
...

#### 静默异常
并不是什么时候都需要将异常信息告知用户。如果想在发生异常的时候保持静默，可以使用`pass`语句，以明确告诉python什么都不做。

**注意**：不能采取在`except`代码块中什么都不写的方式来尝试达到静默的目的。python中代码块不能为空，否则会报错`IndentationError`。

### 10.4 数据存储
很多程序要求用户输入信息，当用户关闭程序的时候，几乎总是要保存他们提供的信息。一种方式是使用`json`模块来存储数据。

python的`json`模块可以很方便地将简单的python数据结构（比如列表，元组，字典）转换为`JSON`格式的字符串。`JSON`格式的数据有下面的好处：  
1. 可以很方便地在python程序运行的时候加载`JSON`格式的数据
2. 可以使用`JSON`方便地在程序之间共享数据
3. `JSON`格式的数据可以和python外的其他编程语言共享。

#### `json.dumps()`和`json.loads()`函数
`json.dumps()`接收一个python数据结构（列表，元组或字典），并返回一个`JSON`格式的字符串。`json.loads()`接收一个`JSON`格式的字符串，返回该`JSON`格式字符串存储的python数据结构。  

下面的代码演示了如何将python的数据结构导出到`JSON`格式的文件当中：
```python
import json
from pathlib import Path

guests_list = ['Jason', 'Timmy', 'Lucy', 'Vicky']
contents = json.dumps(guests_list)
path = Path('guests_list.json')
path.write_text(contents)
```
下面的代码展示了如何在python代码当中读取`JSON`格式的文件从而将其转换为python可以识别的数据结构。
```python
import json
from pathlib import Path

path = Path('guests_list.json')
guests_list = json.loads(path.read_text())
```

#### `Path`类的`exists()`方法
`Path`类的`exists()`方法可以用于检测文件是否存在。若文件存在则返回`True`，文件不存在则返回`False`。

#### 重构
**重构**是指将已经写好的可以正确运行的程序拆分成不同的函数，每个函数执行单一的任务。重构可以让代码更清晰，更易于理解，更容易扩展。

## CH11 测试代码
### 11.2 测试函数
#### 单元测试和测试用例
1. 单元（unit）：即软件或函数的某个方面，比如计算器能否处理除0情况是一个单元，能否进行四则运算是另一个单元。
2. 单元测试（unit test）：核实上面描述的单元能否正确运行。
3. 测试用例（test case）：一组单元测试，核实软件或函数在各种情况下行为符合要求。

下面展示的是一个待测试的函数：  
*name_function.py*
```python
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name.title()} + ' ' + {last_name.title()}"
    return full_name
```

针对上面待测试的函数的测试代码如下：
```python
from name_function.py import get_formatted_name

def test_first_last_name():
    """以下是针对一个单元的测试"""
    formatted_name = get_formatted_name('jason', 'rao')
    assert formatted_name == 'Jason Rao'
```
**注意**：  
1. 测试文件的内容是运行相关测试的**函数**。
2. 测试文件的名称必须以`test_`开头或以`_test`结尾，因为当`pytest`运行测试时，会查找以`test_`开头或以`_test`结尾的文件，并运行其中的测试。
3. 运行测试的方式是在`test_`开头或以`_test`结尾的测试文件的目录下执行`pytest`命令，`pytest`会自动运行程序调用目录下的所有测试文件中的测试函数。

#### `assert`语句
`assert`语句即断言，是指当`assert`后面的条件语句不成立的时候，python会立刻抛出`AssertionError`异常从而终止程序，而不是让程序继续运行下去。
```python
assert 条件语句
```
上面的断言语句，等价于下面的`if`语句：
```python
if not 条件语句:
    raise AssertError
```

#### 断言重写
pytest有**断言重写**机制，即当pytest运行的测试代码当中`assert`抛出`AssertionError`异常，pytest会改写该异常为实际引起`assert`不成立的错误原因。

### 11.3 测试类
#### 使用夹具（fixture）
**夹具**（fixture）用于帮助搭建测试环境。在测试类的过程中，可以利用夹具创建所有测试用例都可以共同使用的一个实例，而不需要每个测试用例都单独创建一个类的实例。

**装饰器**（decorator）是放在函数定义前的指令，python会在函数运行前将该指令用于函数，从而修改函数代码的行为。有点类似C/C++函数前的`static`修饰符等等。

在 pytest 中，创建一个夹具（fixture）用于测试，需要定义一个使用 `@pytest.fixture` 装饰的函数。`@pytest.fixture` 是 `pytest` 模块中的装饰器，因此需要先引入 `pytest` 模块。被 `@pytest.fixture` 装饰的函数，其返回值代表的资源或数据会被 pytest 管理，并可以通过依赖注入机制自动传递给其他测试函数。这些测试函数只需要在参数中声明夹具函数的名称，就能访问夹具的返回值或资源，而无需显式调用该函数。

```python
import pytest

@pytest.fixture
def public_case():
    # 夹具准备阶段
    case = {"key": "value"}
    return case  # 返回需要注入的资源

def test_case(public_case):
    # 测试函数使用夹具的返回值
    assert public_case["key"] == "value"
```
在上面的代码当中，夹具`public_case`中的返回值`case`会被注入其他函数当中，比如`test_case`当中，其他函数通过调用夹具所在的函数名来使用夹具返回的资源。

## CH15 数据
### 15.2 简单绘制
**注意**：  
1. 导入语句通常为`import matplotlib.pyplot as plt`
2. `fig, ax = plt.subplots()`显式生成一个**图表容器**`Figure`对象，和一个**绘图子区域**`Axes`对象。`Figure`理解为整张白纸hi，`Axes`理解为这张白纸上的一块矩形区域。
3. `Figure`设置对象是整个图像的大小，布局等等，`Axes`的设置对象是局部内容，比如坐标轴，标题，曲线类型等等。
4. `plot()`方法：作用于`Axes`对象，接收一个用于绘制折线图。
5. `show()`函数：打开`Matplotlib`查看器并显示绘图。

#### `plot()`方法
函数签名：
```python
plot([x], y, [fmt], *, data=None, **kwargs)
plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)
```
**注意**：  
1. 函数签名中参数列表的**星号（*）**表示紧跟后面的一个参数必须以关键字参数方式传参。即`data`参数必须以`data=...`方式传参。
2. 函数签名中参数带方括号`[]`表示该参数为可选参数。

`plot()`方法实例：
```python
# 不指定 x，默认使用索引作为 x
plt.plot([1, 4, 9, 16])  # y 数据

# 指定 x 和 y
plt.plot([0, 1, 2, 3], [1, 4, 9, 16])  # x 和 y 数据

# 使用格式字符串
plt.plot([0, 1, 2, 3], [1, 4, 9, 16], 'ro-')  # 红色圆点实线

# 使用 data 参数
data = {'x_values': [0, 1, 2, 3], 'y_values': [1, 4, 9, 16]}
plt.plot('x_values', 'y_values', data=data)  # x 和 y 是 data 的键

# 设置线条宽度和标签
plt.plot([0, 1, 2, 3], [1, 4, 9, 16], linewidth=2, label='My Line')  # 线宽=2
```
3. `**kwargs`: 其他可选参数，用于设置线条属性（如颜色、宽度等）。
```python
# **kwargs参数示例：设置线条宽度和线条标签
ax.plot([1, 4, 9, 16, 25], linewidth=3, label='Square value')
```
4. `set_title()`, `set_xlabel()`, `set_ylabel()`方法：用于设置图像标题以及坐标轴标签。可以加上`fontsize=n`关键字参数用于设置标签字体大小。
```python
import matplotlib.pyplot as plt

square = [value ** 2 for value in range(1, 11)]
fig, ax = plt.subplots()
ax.plot(list(range(1, 11)), square, label='Square line') #**kwargs部分设置线条标签（图例）
ax.set_title('Square line') #设置图表标题
ax.set_xlabel('x') #设置x轴标签
ax.set_ylabel('y') #设置y轴标签
plt.legend() #用于显示线条标签（图例）
plt.show()
```
5. 在默认情况下，`x`轴的数据为`y`轴的索引，因此从0开始，可能会导致困惑。所以注意是否需要指定`x`轴的数据。

#### `matplotlib`内置样式
该命令可以查看系统中可使用的所有绘图内置样式：
```python
import matplotlib.pyplot as plt

plt.style.available
```
`plt.style`是对`matplotlib.style`子模块的引用，`style.available`是对子模块`style`的属性`available`进行访问。

若要使用`plt.style.available`中列出的模板样式，可以在最开始加入下面的代码（下面示例使用seaborn-v0_8模板）：
```python
plt.style.use('seaborn-v0_8')
```

#### 使用`scatter()`绘制散点图
绘制单个点，可以向`scatter()`方法分别传递`x`和`y`坐标值，比如`ax.scatter(2, 4)`。`scatter()`方法可以使用关键字参数`s`用于设置绘图所使用的点的尺寸。  
`tick_params()`方法可以用于设置刻度标记的样式，比如字体大小等等。比如`ax.tick_params(labelsize=14)`。

若要使用`scatter()`绘制一系列点的散点图，可以分别向`scatter()`传递包含`x`和`y`坐标值的列表。
```python
import matplotlib.pyplot as plt

square = [value ** 2 for value in range(1, 11)]
fig, ax = plt.subplots()
ax.scatter(list(range(1, 11)), square, label='Square line', s=10) #**kwargs部分设置线条标签（图例）
ax.set_title('Square line') #设置图表标题
ax.set_xlabel('x') #设置x轴标签
ax.set_ylabel('y') #设置y轴标签
plt.legend() #用于显示线条标签（图例）
plt.show()
```

在刻度标记的数字很大的时候，`matplotlib`会自动使用科学计数法表示，`ticklabel_format(style='plain')`方法可以强制`matplotlib`始终使用常规表示法。

#### 定制颜色
向`scatter()`方法传递`color`参数可以定制点的颜色。比如`color='red'`表示数据点红色，也可以使用RGB方法表示，比如`color=(0.1, 0.5, 0.6)`，每个RGB分量在[0, 1]之间。

#### 颜色映射
**颜色映射**（colormap）是一个从起始颜色渐变到结束颜色的颜色序列，可以用于突出数据的规律。
```python
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
```
`c`参数指示需要颜色映射的参数，这里指根据`y`坐标的值决定该点的颜色。`cmap`参数指定颜色映射的模板。

#### 自动保存绘图
`savefig()`方法可以用于将绘图保存到文件当中，而不是使用`show()`方法在查看器中查看图像。

`savefig('file_name.png', bbox_inches='tight')`：第一个参数指保存的文件名，第二个参数指省略绘图周围多余的空白区域。

## CH16 下载数据
### 16.1 CSV文件格式
`CSV`（comma-separated values）格式，即以逗号分隔的值。
#### 解析CSV文件头
CSV的文件头包含一系列内容，指出后续各行包含的信息（即表头）。
```python
from pathlib import Path
import csv

path = Path('file_name.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
```
上面的代码读取CSV文件的文件头并存储到`header_row`当中。

`path.read_text().splitlines()`语句的效果是把CSV文件的内容写入一个列表内，其中列表的每个元素是CSV的一行数据。

`csv.reader()`函数接收一个CSV文件经过`splitlines()`方法生成的列表，效果是把CSV文件的每行单独组织称为一个列表，列表的元素是每个表项。

**注意**：`csv.reader()`生成的是`惰性迭代器`，在迭代结束后不会回到开头，因此在读取文件头后可以将其存入列表进行读取。
 
 `next()`函数，用于返回迭代器的下一项。当`next()`函数接收`csv.reader()`的`reader`时，效果依次返回CSV文件的每行组成的列表。执行`next()`函数会改变`reader`的起始位置。因此通常只在读取文件头的时候使用`next()`函数。

#### 打印文件头及其位置
`enumerate()`函数是python一个内置函数，接收一个可迭代对象（列表，元组...），返回每一项的索引及元素。

用法：`for index, value in enumerate(list)`
```python
import csv
from pathlib import Path

path = Path('./weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()
readers = csv.reader(lines)
header_row = next(readers)
for index, value in enumerate(header_row):
    print(f"{index}: {value}")
```

#### 提取并读取数据
```python
...
values = []
for row in readers:
    value = int(row[4]) #读取第五列的元素，并转换为整型数据
    values.append(value)
```

#### `datetime`模块
`datetime`模块可以用于解析字符串格式的时间。
```python
date = datetime.strptime(str_time, str_fmt)
```
其中`str_time`是字符串格式的时间，`str_fmt`是指示该字符串格式的格式控制字符串，如`'%Y-%m-%d'`。

`strptime()`函数用于从字符串解析时间，`strptime`是string parse time的缩写。