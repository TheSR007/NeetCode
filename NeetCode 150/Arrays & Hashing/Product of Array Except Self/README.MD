# Products of Array Except Self

**Difficulty:** <span style="color: orange;">Medium</span>

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is **guaranteed** to fit in a **32-bit** integer.   

Follow-up: Could you solve it in O(n)O(n)O(n) time without using the division operation?

**Example 1:**

```java
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
```
**Example 2:**

```java
Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
```
**Constraints:**


- `2 &lt;= nums.length &lt;= 1000`

- `-20 &lt;= nums[i] &lt;= 20`






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution as good or better than `O(n)` time and `O(n)` space, where `n` is the size of the input array.

</details>



<details>
<summary>Hint 1</summary>

A brute-force solution would be to iterate through the array with index `i` and compute the product of the array except for that index element. This would be an `O(n^2)` solution. Can you think of a better way?

</details>



<details>
<summary>Hint 2</summary>

Is there a way to avoid the repeated work? Maybe we can store the results of the repeated work in an array.

</details>



<details>
<summary>Hint 3</summary>

We can use the prefix and suffix technique. First, we iterate from left to right and store the prefix products for each index in a prefix array, excluding the current index's number. Then, we iterate from right to left and store the suffix products for each index in a suffix array, also excluding the current index's number. Can you figure out the solution from here?

</details>



<details>
<summary>Hint 4</summary>

We can use the stored prefix and suffix products to compute the result array by iterating through the array and simply multiplying the prefix and suffix products at each index.

</details>