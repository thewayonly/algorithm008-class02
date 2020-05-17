学习笔记

# 搜索 - 遍历
在树（图、状态集合）中寻找特点的节点
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```
* 每个节点都要访问一遍，仅且访问一遍
* 对于节点的访问顺序分为dfs和bfs

## 深度优先搜索 DFS 

```python
visited = set() 

"""递归写法"""
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)

"""多叉树"""
visited = set()

def dfs(node, visited):
    # terminator 
    if node in visited:
        # already visited
        return 
    visited.add(node)

    # process current node
    # ToDO ... logic here

    for next_node in node.children():
    if not next_node in visited:
        dfs(next_node, visited)

"""非递归写法，维护一个stack"""
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```

## 广度优先搜索 BFS
```
def bfs(graph, start, end):


    visited, queue = [], [start]    

    while queue:
        node = queue.pop()
        visited.append(node)

        process(node)

        nodes = generate_related_nodes(node)

        queue.push(nodes)

    # other processing work 
```

# 贪心算法
## 贪心算法是一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

## 贪心和动态规划的区别
贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退。动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能。

贪心法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。

一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。

## 适用贪心算法的场景
简单地说，问题能够分解成子问题来解决，，如：求图中的最小生成树、求哈夫曼编码等,子问题的最优解能递推到最终问题的最优解。子问题的最优解能递推到最终问题的最优解。这种子问题最优解称为最优子结构。

# 二分查找
## 适用场景
* 目标函数单调性（单调递增或者递减，**当集合仅具有两种单调情况下也适用**） 
* 存在上下界（bounded）
* 能够通过索引访问（index accessible)



## 代码模板
```python
left, right = 0, len(array) - 1 
while left <= right: 
    mid = (left + right) / 2 
    if array[mid] == target: 
        # find the target!! 
        break or return result 
    elif array[mid] < target: 
        left = mid + 1 
    else: 
        right = mid - 1
```

## 关于二分查找边界条件：

1. 中间索引mid可以写成`mid = left + (right - left) / 2 `防止整数溢出
2. 如果递增序列A有重复元素，需要找到第一个大于等于给定值x的位置L以及第一个大于x的位置R，即x的存在区间为左闭右开[L, R)，这两个问题都是在寻找有序序列中**第一个**满足某条件的元素位置（如果要寻找**最后一个**满足条件C的元素位置，可以先求第一个满足条件!C的元素位置，然后将位置-1），在进行比较时：
   - 求解L时（lower_bound问题）：
     - `A[mid] ≥ x`，则第一个≥x的元素一定在mid或mid左侧，继续查找有`right = mid`
     - `A[mid] < x`，则继续查找有`left = mid + 1`，由于没有等号，可以排除mid。
     - 循环条件为`left < right`，因为不需要假定x存在，当`left == right`时就是需要的结果，返回值可以选择其中一个
     - 二分查找的下界一定是0，上界根据问题判断是n还是n-1，如果要查询的元素可能比序列中所有元素都大，则选择n（此时n为应该在的位置）
   - 求解R时（upper_bound问题）：
     - `A[mid] > x`，则第一个大于x的元素一定在mid处或者mid左侧，继续查找有`right = mid`
     - `A[mid] ≤ x`时，则第一个大于x的元素一定在mid的右侧，继续查找有`left = mid + 1`
     - 循环条件与上面相同，`left == right`时就是要找的位置
     - 上下界和上面相同

# 关于交换两个数的最佳实践
原理: 异或操作的可逆性, 两个数异或之后再异或一次就得到原来的数
```
a = 3
b =17
print(a, b)
a ^= b
b ^= a
a ^= b
print(a, b)
```

# 判断一个整数是否为奇数
* 常规做法 
```
def is_odd(n):
    return n % 2 == 1
```
* 位运算  
原理: n % 2 的本质是取n的二进制数的最后末位（左高右低排列各比特位）
 因此只需要将数按位与上数字1即可，得到是数字，转换成bool即可，很多时候可以不用转换直接用，比如在if语句中
 ```
def is_odd_bit(n):
    return bool(n & 1)

print(is_odd_bit(2))
```
