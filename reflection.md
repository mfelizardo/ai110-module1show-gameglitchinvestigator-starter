# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  - The first time I ran the game, I was able to see the game's simple UI and understood that the game is a Guess the Number game. Afer entering my first guess, I was provided with a hint of "Go Higher". This led me to believe that the number to be guessed was higher than my initial guess, however, after guessing numbers higher and using all my attempts, I was unable to successfully guess the number.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. The hints were backwards (guessing a number that was higher than the secret number gave the hint "Go Higher" when it should say "Go Lower")
  2. When entering a guess in the given text box, pressing Enter to submit the guess doesn't actually do anything. Guesses can only be submitted by clicking the Submit Guess Button. 
        1. The following comment may only apply to when the Develop Debug Info section is expanded:
         
         However, when entering a second guess by changing the current value in the text box and then pressing the Enter key, it appears that the previous guess gets recorded into the History as well as increments the Attempts value. (Note: the same behavior can occur when simply clicking out of the text box after changing the number instead of clicking Enter. This may also confuse the player because if they enter their second guess and immediately click the Submit Guess Button, it doesn't actually submit their second guess. They would have to click the button again. This confusion however, will only occur if the Developer Debug Info is expanded. If the info panel is closed, then it looks like submitting subsequent guesses and then clicking the Submit Guess Button once is working as intended).
  3. It looks like the first game when launching already has Attempts at 1 when it should start at 0 (since the player hasn't made a guess yet). We also know that Attempts should probably start at 0 because when clicking the New Game Button, the Attempts value gets updated to 0.
  4. Clicking the New Game Button after the end of a current game (either Win or Lose) doesn't start a new game. It appears that the Secret number still changes and the Attempts reset to 0 (if not already) however but the player cannot input anymore guesses.
  5. Adjusting the Difficulty in the Settings sidebar does not update the range of the secret number. The range of the secret numbers remains unchanged at any value between 1 and 100, even though the range for Easy should be 1 to 20 and the range for Hard should be 1 to 50.
  6. The score appears to be calculated incorrectly. Successfully guessing the correct number on the first attempt gives a final score of 70. At this point I am still unsure of the intended way that the score should be calculated (does it take into account of the number of remaining attempts?)

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Submitting a Guess of 50 (given Secret Number 90 or any other number larger than 50) | Hint says "Go Higher" | Hint says "Go Lower" | None |
| Clicking the New Game Button after the end of a game | New game starts, with a new secret number and new set of attempts. The player should be able to input new guesses. | There is a new secret number and attempts are set to 0 (at least according to the Dev Debug Info), however, the player is unable to input any more guesses | None |
| User inputs a number into the Enter your Guess Text Box and presses the Enter key | The guess gets submitted, and the game will give the appropiate feedback. | The number does not get submitted and nothing else happens. If the user wants to submit their guess, they must click the Submit Guess Button. | None |
| Changing the Difficulty to Easy, then clicking the New Game Button | The number of Attempts should be adjusted to 6. The secret number should always be within the range of 1 to 20, with 6 guessing Attempts. | The number of Attempts is correctly adjusted to 6. However, the secret number is not guaranteed to be within the range 1 to 20 (for example, in one case it was 31) | None |
| Opening the Game for the first time. If the game is alrady open, then refreshing the browser | The blue text box should read: "Guess a number between 1 and 100. Attempts left: 8" This is because the default difficulty should be at Medium which gives the user 8 Guess Attempts. | The blue text box reads: "Guess a number between 1 and 100. Attempts left: 7" | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
