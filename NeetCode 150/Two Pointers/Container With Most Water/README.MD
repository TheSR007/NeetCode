# Container With Most Water

**Difficulty:** <span style="color: orange;">Medium</span>

You are given an integer array `heights` where `heights[i]` represents the height of the ithi^{th}ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

**Example 1:**

![Example img](Ex1.png)
```java
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
```
**Example 2:**

```java
Input: height = [2,2,2]

Output: 4
```
**Constraints:**


- `2 &lt;= height.length &lt;= 1000`

- `0 &lt;= height[i] &lt;= 1000`






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(n)` time and `O(1)` space, where `n` is the size of the input array.

</details>



<details>
<summary>Hint 1</summary>

A brute force solution would be to try all pairs of bars in the array, compute the water for each pair, and return the maximum water among all pairs. This would be an `O(n^2)` solution. Can you think of a better way?

</details>



<details>
<summary>Hint 2</summary>

Can you think of an algorithm that runs in linear time and is commonly used in problems that deal with pairs of numbers? Find a formula to calculate the amount of water when we fix two heights.

</details>



<details>
<summary>Hint 3</summary>

We can use the two pointer algorithm. One pointer is at the start and the other at the end. At each step, we calculate the amount of water using the formula `(j - i) * min(heights[i], heights[j])`. Then, we move the pointer that has the smaller height value. Can you think why we only move the pointer at smaller height?

</details>



<details>
<summary>Hint 4</summary>

In the formula, the amount of water depends only on the minimum height. Therefore, it is appropriate to replace the smaller height value.

</details>