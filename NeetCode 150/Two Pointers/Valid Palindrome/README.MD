# Valid Palindrome

**Difficulty:** <span style="color: green;">Easy</span>

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Example 1:**

```java
Input: s = "Was it a car or a cat I saw?"

Output: true
```
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**

```java
Input: s = "tab a cat"

Output: false
```
Explanation: "tabacat" is not a palindrome.

**Constraints:**


- `1 &lt;= s.length &lt;= 1000`

- `s` is made up of only printable ASCII characters.






<details>
<summary>Recommended Time &amp; Space Complexity</summary>

You should aim for a solution with `O(n)` time and `O(1)` space, where `n` is the length of the input string.

</details>



<details>
<summary>Hint 1</summary>

A brute force solution would be to create a copy of the string, reverse it, and then check for equality. This would be an `O(n)` solution with extra space. Can you think of a way to do this without `O(n)` space?

</details>



<details>
<summary>Hint 2</summary>

Can you find the logic by observing the definition of pallindrome or from the brute force solution?

</details>



<details>
<summary>Hint 3</summary>

A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.

</details>