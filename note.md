# Python学习笔记
## CH2 变量名和数据类型
### `title()`方法
`title()`方法可以用于字符串对象，输出字符串每个单词的首字母大写形式。方法常用于格式化标题，句子或者人名。
```python
print("jason rao".title())
```  
### 字符串插入变量
字符串插入变量值，在引号前加上字母f（formatted的缩写），再将要插入的变量放在大括号内。
```python
print(f"Hello, {first_name} {last name}!")
```
### C风格格式输出
C风格字符串格式输出：`"格式化字符串" % (变量1, 变量2, ...)`
```python
print("Hello, %s %s!" % (first_name.title(), last,name.title()))
```
### 删除空白方法`strip()`
`strip()`方法可以找出字符串两端多余的空白。`lstrip()`和`rstrip()`分别用于找出左侧和右侧的空白。  
该方法不会修改原字符串。若要修改原字符串，将方法赋值给原字符串即可。
```python
my_name = my_name.strip()
```
