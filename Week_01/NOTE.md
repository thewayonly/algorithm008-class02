## 知识点
先把思路整理出来，后面再慢慢优化。
看到不好的代码直接跳过，与其去理解它不如学习好的代码

写代码：
5～10分钟：读题+思考
有思路，自己开始做和coding；否则，马上看题解
默写背诵、熟练
开始自己写（闭卷）
！！反馈
看官方的解法，排序后的最优解法
去国际站看dicuss，看解法
“五毒神掌”，过遍数，反复练习

### 数组，链表，跳表
1.数组的prepend指前置、预追加
硬件实现： 内存管理器， 每当申请数组时，计算机都在内存中开辟了一段`连续`的地址，每个地址可以直接通过内存管理器访问
insert前需要保证数组的size足够，否则需要扩容，拷贝等低效操作
2.链表优化了数组的插入和删除时间复杂度，而跳表在链表有序的前提下，优化了查询方式，使得插入和删除都是logN
3.一维的数据结构要加速一般采取的方式是升维，多一个维度就可以多一层信息。
跳表就是这个思路的实现。实际应用中，随着元素的增加和删除，跳表的索引并不是非常的工整，有的多跨几步；维护成本相对较高，增加和删除一个元素都需要把所有的索引更新一遍。
跳表的核心思想： 升维+空间换时间

4.单向链表： 每个node的指针是单向的，最后一个节点指向nil；
双向链表： 
循环链表
5.工程中的应用：
o	LRU Cache - Linked list: LRU 缓存机制
o	Redis - Skip LIst
6.时间复杂度
| name       | prepend | appendd | lookup | insert | delete |
| ---------- | ------- | ------- | ------ | ------ | ------ |
| Array      | O(n)    | O(1)    | O(1)   | O(n)   | O(n)   |
| LinkedList | O(1)    | O(1)    | O(n)   | O(1)   | O(1)   |
7. 简单常见的数组算法解
主要常见的方法有暴力解法（嵌套循环），双指针，递归，其中递归和暴力解法都是时间复杂度对相对较高的解法。 

#### 总结
1.ArrayyList查找元素快，时间复杂度O（1），新增删除元素慢，时间复杂度为O（n） 
2.Linked List新增、删除元素快，时间复杂度O（1），当然，对于头数据和尾数据的查找也快，时间复杂度O（1），随机查找元素慢，时间复杂度O（n） 
3.跳表：只能用于元素有序的情况。所以，跳表（skip list）对标的是平衡树（AVL Tree）和二分查找，是一种插入/删除/搜索都是O（log n）的数据结构。1989年出现。它最大的优势是原理简单、容易实现、方便扩展、效率更高。因此在一些热门的项目里用来替代平衡树，如Redis、LevelDB等。 核心思想：1）升维。2）空间换时间

### 栈、队列、优先队列、双端队列
1. Stack 栈 —— last in first out，后入先出， 添加、删除皆为O（1），但是查询为O（n），因为元素是无序的
Queue 队列 —— First in first out， 排队，先来先出，添加、删除皆为O（1），但是查询为O（n），因为元素是无序的
2. Deque，double ended queue， 添加、删除皆为O（1），但是查询为O（n），因为元素是无序的 实战中或者高级语言中一般也不用queue和stack，而是用双端队列，可以视为queue和stack的结合体。可以在最前端pop和push，也可以在尾端pop和push。
3. Stack、Queue、Deque的工程实现
很多教程的stack实现，都是基于数组模拟
google快速查询：
（1）查询Java最新版本： latest java version （实际工程中为了稳定性，一把会比最新版低一两个版本）
（2）Java的stack文档： Stack Java 10 （10指Java的最新版本号） 
可以在官方文档中查看关键API
（3）Java中queue本身定义为接口，底层实现的类多种多样。 接口定义了一套方法，底层具体怎么实现看实际的方法
（4）Java中deque也定义为接口
一些基础数据结构，在高级语言里面的实现非常的成熟和全面。
（5）查看Java的stack部分的源代码： source stack Java
（6）下载Java的源代码： Java source code download
4. 示例代码
offer和poll不抛异常；
add和remove为空时抛出异常
5. 面试中常考点 Priority Queue 优先队列、双端队列
插入操作O（1）
取出操作O(logN)，优势：按照元素的优先级取出
底层具体实现的数据结构较为多样和复杂： 可以用heap，bst，treap。而且heap也可以是多重视。
Java中实现了queue的所有方法
6. Python的Stack和Queue代码实现示例代码
Python提供了一个高性能的container库，里面包含所有高性能的内容
Python的priprity queue是用heapq实现的
7. 作业：
分析Queue和Priority Queue的源码


## 问题
1.Question:链表的插入疑问：如果你想插入到第i个位置的话，那不是还得先遍历到第i个位置，然后再进行插入，虽然插入这个操作是O(1)，但是查的过程应该是O(n),那是不是可以说链表的插入是O(n)呢？
Answer:
array查询已知index为O(1),linked的已知node插入也是O(1)。即链表的插入为O(1),有隐形前提条件：已知节点更改指针，否则，都需要遍历，即链表也需要先从头开始寻找到需要插入的节点，再执行插入，为O（n）。
而在真正描述链表插入的时间复杂度，是指在已经知道node节点的情况下计算插入的时间复杂度。
——所以，跳表的插入和删除是logN，是因为跳表优化了查询部分的操作为logN。


## Deque示例代码改写
```java
import java.util.Deque;
import java.util.LinkedList;

public class DequeDemo {
    public static void main(String[] args) {
        Deque<String> deque = new LinkedList<String>();

        deque.addLast("a");
        deque.addLast("b");
        deque.addLast("c");
        System.out.println(deque);
		
        String str = deque.peekLast();
        System.out.println(str);
        System.out.println(deque);
		
        while (deque.size() > 0) {
            System.out.println(deque.pop());
        }
        System.out.println(deque);
    }
}
```
