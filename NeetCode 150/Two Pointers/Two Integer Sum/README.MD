# Two Integer Sum II

**Difficulty:** <span style="color: orange;">Medium</span>

Given an array of integers `numbers` that is sorted in **non-decreasing order**.

Return the indices (**1-indexed**) of two numbers, `[index1, index2]`, such that they add up to a given target number `target` and `index1 &lt; index2`. Note that `index1` and `index2` cannot be equal, therefore you may not use the same element twice.

There will always be **exactly one valid solution**.

Your solution must use O(1)O(1)O(1) additional space.

**Example 1:**

```java
Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
```
Explanation:
The sum of 1 and 2 is 3. Since we are assuming a 1-indexed array, `index1` = 1, `index2` = 2. We return `[1, 2]`.

**Constraints:**


- `2 &lt;= numbers.length &lt;= 1000`

- `-1000 &lt;= numbers[i] &lt;= 1000`

- `-1000 &lt;= target &lt;= 1000`






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(n)` time and `O(1)` space, where `n` is the size of the input array.

</details>



<details>
<summary>Hint 1</summary>

A brute force solution would be to check every pair of numbers in the array. This would be an `O(n^2)` solution. Can you think of a better way?

</details>



<details>
<summary>Hint 2</summary>

Can you think of an algorithm by taking the advantage of array being sorted?

</details>



<details>
<summary>Hint 3</summary>

We can use the two-pointer algorithm. If `nums[0] + nums[n-1] &gt; target`, then we know `nums[n - 1]` can not possibly be included in any pairs. Why? Because `nums[n - 1]` is the largest element in the array. Even by adding it with `nums[0]`, which is the smallest element, we still exceed the target. You can think of the case when `nums[0] + nums[n - 1] &lt; target`.

</details>



<details>
<summary>Hint 4</summary>

We keep two pointers, one at the start and the other at the end of the array. If the sum of the numbers at the two pointers is greater than the `target`, decrement the right pointer, else increment the left pointer. Repeat this process until you find a valid pair.

</details>