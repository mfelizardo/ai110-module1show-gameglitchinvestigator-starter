# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
  - [ ] The game's purpose is to generate a random secret number and allow the user to try and guess the secret number within a limited amount of attempts. For each attempt that isn't the correct guess, a hint will be provided guiding the user closer to the actual secret number. This game initially has a lot of bugs that I (the developer) had to fix. Fortunately, I had Claude Code to help me debug and implement fixes.
- [ ] Detail which bugs you found.
  - [ ] Hints were inverted
  - [ ] Enter button to submit guess didn't work
  - [ ] Unable to start new game after winning or losing the previous game
  - [ ] Score calculation was inaccurate
- [ ] Explain what fixes you applied.
  - [ ] Swapped hint messages in `check_guess` function
  - [ ] Implemented a Streamlit Form to allow use of Enter key to submit guess
  - [ ] Adjusted session state status back to "playing" after pressing New Game
  - [ ] Adjusted the `update_score` function to return a score that makes sense based on number of attempts remaining

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User submits guess of 50 (submitted by clicking Submit Guess button)
2. Game returns Hint: Go Higher! Attempts decreases from 8 to 7
3. User submits guess of 75 (submitted by pressing the Enter key)
4. Game returns Hint: Go Higher! Attempts decreases from 7 to 6
5. User submits guess of 90 (submitted by pressing the Enter key)
6. Game returns "Correct! You won! The secret was 90. Final score: 75"

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
```
============================================================================================================ test session starts =============================================================================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Mikey\Desktop\CodePath Courses\AI Engineering\Project 1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 29 items                                                                                                                                                                                                                            

tests\test_game_logic.py .........                                                                                                                                                                                                      [ 31%]
tests\test_new_game.py ....                                                                                                                                                                                                             [ 44%]
tests\test_score.py ................                                                                                                                                                                                                    [100%]

============================================================================================================= 29 passed in 2.43s =============================================================================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
