# Top K Frequent Elements

**Difficulty:** <span style="color: orange;">Medium</span>

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always **unique**.

You may return the output in **any order**.

**Example 1:**

```java
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
```
**Example 2:**

```java
Input: nums = [7,7], k = 1

Output: [7]
```
**Constraints:**


- `1 &lt;= nums.length &lt;= 10^4`.

- `-1000 &lt;= nums[i] &lt;= 1000`

- `1 &lt;= k &lt;= number of distinct elements in nums`.






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(n)` time and `O(n)` space, where `n` is the size of the input array.

</details>



<details>
<summary>Hint 1</summary>

A naive solution would be to count the frequency of each number and then sort the array based on each element’s frequency. After that, we would select the top `k` frequent elements. This would be an `O(nlogn)` solution. Though this solution is acceptable, can you think of a better way?

</details>



<details>
<summary>Hint 2</summary>

Can you think of an algorithm which involves grouping numbers based on their frequency?

</details>



<details>
<summary>Hint 3</summary>

Use the bucket sort algorithm to create `n` buckets, grouping numbers based on their frequencies from `1` to `n`. Then, pick the top `k` numbers from the buckets, starting from `n` down to `1`.

</details>