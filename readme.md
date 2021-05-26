 1. 可迭代对象
after adding address
   - 可更新迭代的实实在在的值
   - 内部含有iter方法的
   - 优点：操作方法多，灵活，直观
   - 缺点:占用内存
1105592115@qq.com
     stupid guy 
smart boy
2. 迭代器
zouyehang
   - 可更新迭代的数据结构
   - 内部含有iter且含有next方法的
   - 优点：节省内存，惰性机制
   - 缺点：不直观，操作单一，速度相对慢，不走回头路

3. 生成器：本质上就是迭代器，唯一的区别是，生成器是我们自己用python代码构建的数据结构，而迭代器都是提供的，或者转化得来的
git test change 
   - 获取生成器的方式：

     - 生成器表达式
     - 生成器函数

   - 生成器函数获取生成器

     ```
     def func():
         print('111')
         print('222')
         yield 2
         print('444')
         print('555')
         yield 5
     func()
     ret=func()
     print(ret)
     print(func)
     print(next(func()))
     print(next(ret))
     ```

     return：函数中只存在一个return，结束函数并返回值

     yield：可以存在多个，且一个yield对应一个next

     - 吃包子普通版

       ```
       def func():
           l1=[]
           for i in range(100):
               l1.append(f'第{i}号包子')
           return l1
       ret=func()
       print(ret)
       ```

       吃包子生成器版：

       ```
       def func():
           for i in range(1,1001):
               yield f'第{i} 号包子'
       ret=func()
       
       for i in range(100):
           print(next(ret))
          
       ```

   - yield from（一个一个取出来）

     ```
     # def func():
     #     l1=[1,2,3,4,5,6]
     #     yield l1
     #
     # ret=func()
     # print(next(ret))
     def func():
         l1=[1,2,3,4,5,6]
         yield from l1
     ret=func()
     print(next(ret))
     ```

4. 列表推导式（用一行代码构建一个比较复杂有规律的列表）

   - 循环模式

     ```
     # l1=[]
     # for i in range(1,10):
     #     l1.append(i)
     # print(l1)
     
     l1=[i for i in range(1,10)]
     print(l1)
     ```

   - 筛选模式：

     试题一：过滤掉长度小于三的字符串，并将剩下的转化为大写

     ```
     l1=['asdu','aod','dou','du','aldut']
     print([i.upper() for i in l1 if len(i)>2])
     ```

   - 试题二：含有两个e的单词留下来

     ```
     l1=['qigewhcqpwgikc','wgecphgwe','asdu','eee','elottqe']
     l2=[i for i in l1 if i.count('e')==2]
     print(l2)
     ```

5. 生成器表达式（写法几乎相同，只有一个区别）

   ```
   print([i for i in range(1,20 )])
   print((i for i in range (1,20))) 
   ```