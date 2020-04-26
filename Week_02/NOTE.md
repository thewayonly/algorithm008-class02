# 第二周学习笔记

## 1. 课程观看笔记
### 1.1 树的三种遍历方式
    1、前序：根-左-右
    2、中序：左-根-右
    3、后序：左-右-根
  
二叉搜索树，时间复杂度一般为O(log n)<br />

### 1.2 树的遍历代码写法
#### 中序遍历
```java
public class temp{
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            helper(root, res);
            return res;
        }

        public void helper(TreeNode root, List<Integer> res) {
            if (root != null) {
                if (root.left != null) {
                    helper(root.left, res);
                }
                res.add(root.val);
                if (root.right != null) {
                    helper(root.right, res);
                }
            }
        }
}
```
#### 前序遍历
```java
public class temp{
        public List<Integer> preorderTraversal(TreeNode root) {
            List<Integer> res = new ArrayList<>();
            helper(root, res);
            return res;
        }

        public void helper(TreeNode root, List<Integer> res) {
            if (root != null) {
                res.add(root.val);
                if (root.left != null) {
                    helper(root.left, res);
                }
                if (root.right != null) {
                    helper(root.right, res);
                }
            }
        }
}
```
### 1.3 递归与迭代
树的遍历建议使用递归写法，递归不代表程序运行效率低。在现代编译器对递归程序的优化下，只要算法本身不写崩，
递归程序的运行效率基本可等同非递归写法。

## 2.面试做题步骤:
    1、和面试官共同把题目搞清楚
    2、想解决方案，并从中找出最优的(time & space)
    3、code
    4、test cases

## 3. leetcode刷题笔记
- 树的遍历写法属于基本功，没啥可讨论的，理解背熟就好。
- 算法写的时候可以直接调用语言本身的库，例如在非考察排序的算法题目中对数组进行排序处理。
- 数组计数器是一种很常见的辅助技术。
- 善用Map和Set这两个数据结构。
