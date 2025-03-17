# 3Sum

**Difficulty:** <span style="color: orange;">Medium</span>

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` where `nums[i] + nums[j] + nums[k] == 0`, and the indices `i`, `j` and `k` are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in **any order**.

**Example 1:**

```java
Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
```
Explanation:
`nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.`
`nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.`
`nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.`
The distinct triplets are `[-1,0,1]` and `[-1,-1,2]`.

**Example 2:**

```java
Input: nums = [0,1,1]

Output: []
```
Explanation: The only possible triplet does not sum up to 0.

**Example 3:**

```java
Input: nums = [0,0,0]

Output: [[0,0,0]]
```
Explanation: The only possible triplet sums up to 0.

**Constraints:**


- `3 &lt;= nums.length &lt;= 1000`

- `-10^5 &lt;= nums[i] &lt;= 10^5`






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(n^2)` time and `O(1)` space, where `n` is the size of the input array.

</details>



<details>
<summary>Hint 1</summary>

A brute force solution would be to check for every triplet in the array. This would be an `O(n^3)` solution. Can you think of a better way?

</details>



<details>
<summary>Hint 2</summary>

Can you think of an algorithm after sorting the input array? What can we observe by rearranging the given equation in the problem?

</details>



<details>
<summary>Hint 3</summary>

We can iterate through nums with index `i` and get `nums[i] = -(nums[j] + nums[k])` after rearranging the equation, making `-nums[i] = nums[j] + nums[k]`. For each index `i`, we should efficiently  calculate the `j` and `k` pairs without duplicates. Which algorithm is suitable to find `j` and `k` pairs?

</details>



<details>
<summary>Hint 4</summary>

To efficiently find the `j` and `k` pairs, we run the two pointer approach on the elements to the right of index `i` as the array is sorted. When we run two pointer algorithm, consider `j` and `k` as pointers (`j` is at left, `k` is at right) and `target = -nums[i]`, if the current sum `num[j] + nums[k] &lt; target` then we need to increase the value of current sum by incrementing `j` pointer. Else if the current sum `num[j] + nums[k] &gt; target` then we should decrease the value of current sum by decrementing `k` pointer. How do you deal with duplicates?

</details>



<details>
<summary>Hint 5</summary>

When the current sum `nums[j] + nums[k] == target` add this pair to the result. We can move `j` or `k` pointer until `j &lt; k` and the pairs are repeated. This ensures that no duplicate pairs are added to the result.

</details>