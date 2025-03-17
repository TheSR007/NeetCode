# Group Anagrams

**Difficulty:** <span style="color: orange;">Medium</span>

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in **any order**.

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

```java
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```
**Example 2:**

```java
Input: strs = ["x"]

Output: [["x"]]
```
**Example 3:**

```java
Input: strs = [""]

Output: [[""]]
```
**Constraints:**


- `1 &lt;= strs.length &lt;= 1000`.

- `0 &lt;= strs[i].length &lt;= 100`

- `strs[i]` is made up of lowercase English letters.






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(m * n)` time and `O(m)` space, where `m` is the number of strings and `n` is the length of the longest string.

</details>



<details>
<summary>Hint 1</summary>

A naive solution would be to sort each string and group them using a hash map. This would be an `O(m * nlogn)` solution. Though this solution is acceptable, can you think of a better way without sorting the strings?

</details>



<details>
<summary>Hint 2</summary>

By the definition of an anagram, we only care about the frequency of each character in a string. How is this helpful in solving the problem?

</details>



<details>
<summary>Hint 3</summary>

We can simply use an array of size `O(26)`, since the character set is `a` through `z` (`26` continuous characters), to count the frequency of each character in a string. Then, we can use this array as the key in the hash map to group the strings.

</details>