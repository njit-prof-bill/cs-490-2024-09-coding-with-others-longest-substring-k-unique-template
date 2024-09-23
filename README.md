Here are the precise instructions you can paste into the `README.md` file for your GitHub Classroom assignment:

---

# Longest Substring with K Unique Characters

## Problem Statement

Write a Python function that finds the longest substring of a given string that contains exactly `K` unique characters. If no such substring exists, return 0.

### Function Signature:
```python
def longest_substring_k_unique(s: str, k: int) -> int:
```

### Example Input/Output:
1. **Example 1**:
   ```
   Input: S = "araaci", K = 2
   Output: 4
   Explanation: The longest substring with exactly 2 unique characters is "araa".
   ```

2. **Example 2**:
   ```
   Input: S = "cbbebi", K = 3
   Output: 5
   Explanation: The longest substring with exactly 3 unique characters is "cbbeb" or "bbebi".
   ```

3. **Example 3**:
   ```
   Input: S = "aa", K = 1
   Output: 2
   Explanation: The longest substring with exactly 1 unique character is "aa".
   ```

### Constraints:
1. The string `S` will have at least one character and at most 10^6 characters.
2. The integer `K` will be between 1 and the number of distinct characters in the string.

## Instructions

1. **Fork the Assignment Repository**:
   - Click on the "Fork" button in the top right corner of this repository to fork it into your own GitHub account.

2. **Clone Your Forked Repository**:
   - Clone the repository to your local machine using the following command in your terminal:
     ```bash
     git clone https://github.com/<your-github-username>/source-code-management-exercise.git
     ```
   - Replace `<your-github-username>` with your GitHub username.

3. **Create a New Branch**:
   - In your local repository, create a new branch to work on your solution:
     ```bash
     git checkout -b gcd-feature
     ```

4. **Implement Your Solution**:
   - Implement the `longest_substring_k_unique` function in the provided `solution.py` file. Ensure your code handles edge cases and test it thoroughly before submission.

5. **Commit Your Changes**:
   - Once you’ve written and tested your solution, stage and commit the changes:
     ```bash
     git add solution.py
     git commit -m "Implemented solution for longest substring with K unique characters"
     ```

6. **Push the Changes**:
   - Push your changes to the `gcd-feature` branch on your forked repository:
     ```bash
     git push origin gcd-feature
     ```

7. **Create a Pull Request**:
   - Go to your forked repository on GitHub.
   - Click the "Compare & pull request" button to create a pull request back to the original repository.
   - Make sure you are comparing your `gcd-feature` branch with the `main` branch of the original repository.
   - Submit the pull request.

## Peer Review

Once you submit your pull request, you will be assigned a peer’s solution to review. Follow these steps for peer review:

1. **Review the Peer’s Code**:
   - Check the peer’s code for correctness, efficiency, and readability.
   - Provide constructive feedback and suggest improvements where necessary.

2. **Submit Your Feedback**:
   - Use the GitHub review feature to submit your feedback.

## Submission Deadline

Please make sure your pull request is submitted before the deadline: **Friday, September 28, 2024**.

---

### Notes:
- Ensure your code follows the required Python function signature.
- Make sure your solution is efficient and can handle large inputs (up to 10^6 characters).
- Be respectful and constructive in your peer reviews.
