# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.
sV
<table>
    <tr>
        <th>Edge Case</th>
        <th>Prompt Used</th>
        <th>AI-Suggested Test</th>
        <th>Did It Pass?</th>
        <th>Your Reasoning</th>
    </tr>
    <tr>
        <td>Input is a non-whole number (ex. 50.7)</td>
        <td>I'd like you to generate 3 more pytests to test the game logic. Please write them in @tests/test_game_logic.py .  One test should check if a non-whole number is entered as guess. Another test should check if a very large number is entered as a guess. The third test should check if an input that isn't considered a number is entered as a test.</td>
        <td>

```python
def test_non_whole_number_guess():
    # A decimal input like "50.7" should be accepted and truncated to an int
    ok, value, error = parse_guess("50.7")
    assert ok is True
    assert value == 50
    assert error is None
```

</td>
        <td>Yes</td>
        <td>We need to check if a decimal number can be properly handled and not throw an error or give an incorrect hint, but instead round the number down to the nearest whole number and check that instead.</td>
    </tr>
    <tr>
        <td>Input is a large number (ex. 9999999999)</td>
        <td>I'd like you to generate 3 more pytests to test the game logic. Please write them in @tests/test_game_logic.py .  One test should check if a non-whole number is entered as guess. Another test should check if a very large number is entered as a guess. The third test should check if an input that isn't considered a number is entered as a test.</td>
        <td>

```python
def test_very_large_number_guess():
    # A very large number should still compare correctly against a normal secret
    outcome, _ = check_guess(999999999, 50)
    assert outcome == "Too High"
```

</td>
        <td>Yes</td>
        <td>We need to test if entering a very large number as a guess will not crash or break the game. Since we are using Python, however, I expect this to not occur.</td>
    </tr>
    <tr>
        <td>Input is not a number (ex. the string "hello")</td>
        <td>I'd like you to generate 3 more pytests to test the game logic. Please write them in @tests/test_game_logic.py .  One test should check if a non-whole number is entered as guess. Another test should check if a very large number is entered as a guess. The third test should check if an input that isn't considered a number is entered as a test.</td>
        <td>

```python
def test_non_number_input():
    # A non-numeric string should fail parsing with a descriptive error
    ok, value, error = parse_guess("hello")
    assert ok is False
    assert value is None
    assert error == "That is not a number."
```

</td>
        <td>Yes</td>
        <td>We need to check if the game properly handles guesses that aren't numbers since users may accidently submit one. The game should not crash and should instead reject the guess and prompt the user to enter a number.</td>
    </tr>
</table>


---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
