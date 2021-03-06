# 学习笔记
## 知识点总结
### 字典树和并查集
#### 字典树 Trie，又称单词查找树或键树，典型应用是用于统计和排序大量字符串
    * 节点本身不存完整单词 （节点可存储额外信息（如，统计频次等））
    * 从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串
    * 每个节点的所有子节点路径代表的字符都不相同
   
   核心思想：
   Trie树的核心思想是空间换时间：可最大限度地减少无谓的字符串比较，查询效率比哈希表高
   利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的
 
#### 并查集 Disjoint Set
   1. 适用场景
        * 组团、配对问题
        * Group or not
   2. 基本操作
      * `makeSet(s)` : 建立一个新的并查集，其中包含s个单元素集合
      * `unionSet(x, y)` : 把元素x和元素y所在的集合合并，要求x和y所在集合不相交，如果相交则不合并
      * `find(x)` : 找到元素x所在集合的代表，该操作也可以用于判断两个元素是否位于同一个集合，只需将它们各自的代表进行比较即可

### 高级搜索
#### 初级搜索
   1. 优化方式：不重复（Fibonacci）、剪枝（生成括号问题）
   2. 搜索方向：
      * DFS: Depth First Search 深度优先搜索
      * BFS: Breadth First Search 广度优先搜索
#### 高级搜索
   1. 剪枝
   2. 双向BFS
   3. 启发式搜索（A*） Heuristic Search
      * 启发式函数：h(n)，用来评价哪些节点最有希望成为目标节点，h(n)会返回一个非负实数，也可认为是从节点n到目标节点路径的估价成本
      * 启发式函数是一种告知搜索方向的方法。它提供了一种明智的方法来猜测哪个邻居节点会导向一个目标   

### 红黑树和AVL树
#### AVL树
    1、平衡二叉搜索树
    2、每个节点存 Balance Factor = {-1, 0, 1}
    3、四种旋转操作（左旋，右旋，左右旋，右左旋）  
	
   不足：节点需要存储额外信息，且调整次数频繁
   
#### 红黑树：
   红黑树是一种近似平衡的二叉搜索树，它能够确保任何一个节点的左右子树的高度差小于两倍。
    1、每个节点要么是红色要么是黑色
    2、根节点是黑色
    3、每个叶节点（NIL节点，空节点）是黑色的
    4、不能有相邻接的两个红色节点
    5、从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点。
	
#### AVL和红黑树比较
    1、查找：AVL比红黑树快
    2、插入和删除：红黑树比AVL快
    3、内存：AVL比红黑树要占用大
