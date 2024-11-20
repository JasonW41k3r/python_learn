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

#### 