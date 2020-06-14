# 学习笔记
## 位运算
1. 指定位置的位运算  

> 1. 将 `x` 最右边的n位清零: `x & (~0 << n) `   
   `10110 & (11111111111111111111111111111111 << n) -> 10110 & (11111111111111111111111111111000)`
> 2. 获取 `x` 的第 `n` 位的值: `(x >> n) & 1`  
> `10110 >> 3 -> 10 & 1 -> 0`
> 3. 获取 `x` 的第 `n` 位的幂值: `x & (1 << n)`  
   `1 << n -> 1000 -> 10110 & 01000 -> 0000`  
   `1 << n -> 1000 -> 11110 & 01000 -> 1000`
> 4. 仅将第 `n` 位置为 `1`: `x | (1 << n)`
   `1 << n -> 1000 -> 10110 | 1000 -> 11110`
> 5. 仅将第 `n` 位置 `0`: `x & (~(1 << n))`
> 6. 将 `x` 最高位至第 `n` 位(含)清零: `x & ((1 << n) - 1)`
> 7. 将 `x` 第 `n` 位至第 `0` 位(含)清零: `x & (~((1 << n) - 1))`
> 8. 得到最低位的值: `x & 1`
> 9. 将最低位的 `1` 清 `0`: `x & (x - 1)` 

2. 位运算实战要点记录

> 1. 判断奇偶  
   `x % 2 == 1 -> (x & 1) == 1`, 奇数  
   `x % 2 == 0 -> (x & 1) == 0`, 偶数
> 2. `x >> 1 -> x / 2`  
   `mid = (left + right) / 2 -> mid = (left + right) >> 1`
> 3. `x = x & (x - 1)` 清零最低位的 `1`  // `10110 & 10101 -> 10100`
> 4. `x & -x` 得到最低位的 `1` // `10110 & 0..1011 -> 00` (负数的二进制为: 原码取反+1)
> 5. `x & ~x == 0`   

3. N皇后问题的位运算解法
```python
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        
        def DFS(row, cols, xy_dif, xy_sum):
            if row >= n:
                self.result += 1
                return 
            
            bits = (~(cols|xy_dif|xy_sum)) & ((1 << n) - 1) # 得到当前所有的空位
            print("row:{}, cols:{}, xy_dif:{}, xy_sum:{}, bits:{}".format(bin(row), bin(cols), bin(xy_dif), bin(xy_sum), bin(bits)))
            
            while bits:
                p = bits & -bits # 取到最低位的1
                bits = bits & (bits - 1) # 表示在p位置上放入皇后
                DFS(row + 1, cols | p, (xy_dif | p) << 1, (xy_sum | p) >> 1)
                # 不需要revert cols, xy_dif, xy_sum
        
        self.result = 0
        DFS(0, 0, 0, 0)
        return self.result
```
## 布隆过滤器和LRU缓存
1. 布隆过滤器
   * 使用多个 哈希函数 要加入的值进行哈希运算，计算出多个哈希值，放到对应的多个槽
   * 布隆过滤器可能会误识别：
     * 例如数值 A 计算出的哈希值是 1,2，B 计算出的哈希值是 1,3。把 A 和 B 存进布隆过滤器
     * 现在有一个值 C，想判断是否存在。C 计算出的哈希值是 2,3，刚好 A、B 把 2,3 填充过了，此时就会误识别
   * 如果不存在，一定就是不存在
   * 布隆过滤器极其省空间，因为都是存 bit。一般用于基数很大的例如垃圾邮件识别等等。

2. LRU缓存
   * 最近最少使用的缓存
   * 淘汰策略是：给定一定长度的数组(链表)，访问、插入元素的时候，会把这个元素放到最前面，当长度不够的时候，会淘汰最后一个元素。

## 排序算法
### 冒泡排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
```
时间复杂度：平均 $O(n^2)$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$，稳定算法。
两层循环；相邻两个数比较，用交换的方式，把大的放后面；每一遍都会把当前最大的数找到，放在最后面。

### 选择排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            minIndex = i
            for j in range(i + 1, len(nums)):
                if nums[minIndex] > nums[j]:
                    minIndex = j
            nums[0], nums[minIndex] = nums[minIndex], nums[0]
        return nums
```
时间复杂度：平均 $O(n^2)$, 最优 $O(n^2)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$，不稳定。
两层循环；每次遍历选出最小的值，跟第一个未排序的数交换。

### 插入排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            pre = i - 1
            cur = i
            while cur > 0 and nums[pre] > nums[cur]:
                nums[pre], nums[cur] = nums[cur], nums[pre]
                pre -= 1
                cur -= 1
        return nums
```
时间复杂度：平均 $O(n^2)$, 最优 $O(n)$, 最差 $O(n^2)$, 空间复杂度：$O(1)$，稳定。
两层循环；当前元素跟前一个元素比较，如果小于前一个元素，交换。直到比前一个元素大或者是第一个元素了。
每次遍历都会把当前索引之前的数排序好


### 归并排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums1, nums2):
            len1 = len(nums1); len2 = len(nums2)
            res = []
            idx1 = 0; idx2 = 0
            while idx1 < len1 and idx2 < len2:
                if nums1[idx1] <= nums2[idx2]:
                    res.append(nums1[idx1])
                    idx1 += 1
                else:
                    res.append(nums2[idx2])
                    idx2 += 1
            if idx1 < len1: res += nums1[idx1:]
            if idx2 < len2: res += nums2[idx2:]
            return res

        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left = nums[:mid]; right = nums[mid:]
        return merge(self.sortArray(left), self.sortArray(right))
```

时间复杂度：平均 $O(n{log_2{n}})$, 最优 $O(n{log_2{n}})$, 最差 $O(n{log_2{n}})$, 空间复杂度：$O(n)$，稳定。
将数组分成两个子数组；左右各采用归并排序（如果个数大于1，则继续分）；将左右排序好的数组合并。

### 快速排序
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(left, right):
            pivot = left; border = left + 1
            for i in range(border, right + 1):
                if nums[i] < nums[pivot]:
                    nums[i], nums[border] = nums[border], nums[i]
                    border += 1
            nums[pivot], nums[border - 1] = nums[border - 1], nums[pivot]
            return border - 1
        
        def querySort(left, right):
            if left >= right: return
            border = partition(left, right)
            querySort(left, border - 1)
            querySort(border + 1, right)
        
        querySort(0, len(nums) - 1)
        return nums
```
时间复杂度：平均 $O(n{log_2{n}})$, 最优 $O(n{log_2{n}})$, 最差 $O(n^2)$, 空间复杂度：$O(n{log_2{n}})$，不稳定。
从数组中挑一个元素作为基准（pivot），通常我们拿第一个。
把所有小于基准的元素放到左边，所有大于基准的放右边，相等的随便放哪一边都行。此操作成为分区（partition），方法会返回最终基准的位置。
根据基准的位置，分成左边和右边继续递归。

