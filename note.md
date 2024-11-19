# Python学习笔记
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
在Python中，两个数相除的结果默认通过浮点数表示。该行为在`PEP 238`提案中被确认，是为了使得`/`操作符的统一性，一致地执行真除法，而不是像在python2中整数相除执行地板除法。
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
#### 访问列表元素
通过索引访问列表的元素。python和C语言一样，索引**从0开始**。特别的，通过指定索引为-1，可以访问最后一个列表元素，类似的，索引-2访问倒数第2个元素。

#### 修改列表元素
通过指定索引修改列表元素。
```python
student[0] = 'sid'
```
上面的代码将`student[]`第一个元素修改为`sid`
