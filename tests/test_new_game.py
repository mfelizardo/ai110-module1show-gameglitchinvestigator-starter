"""
Tests that verify the New Game button correctly resets session state so that
players can make guesses again after a game ends.

Uses Streamlit's AppTest utility to run the real app.py.
"""

import os
from streamlit.testing.v1 import AppTest

APP_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py")

# The New Game button is the second button rendered (index 1).
# Render order in app.py: Submit Guess (0), New Game (1).
NEW_GAME_BTN = 1


def test_new_game_after_win_sets_status_to_playing():
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.session_state["status"] = "won"
    at.run()
    at.button[NEW_GAME_BTN].click().run()
    assert at.session_state["status"] == "playing"


def test_new_game_after_loss_sets_status_to_playing():
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.session_state["status"] = "lost"
    at.run()
    at.button[NEW_GAME_BTN].click().run()
    assert at.session_state["status"] == "playing"


def test_new_game_clears_history():
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.session_state["history"] = [10, 20, 30]
    at.session_state["status"] = "won"
    at.run()
    at.button[NEW_GAME_BTN].click().run()
    assert at.session_state["history"] == []


def test_new_game_resets_attempts_to_zero():
    at = AppTest.from_file(APP_PATH)
    at.run()
    at.session_state["attempts"] = 6
    at.session_state["status"] = "lost"
    at.run()
    at.button[NEW_GAME_BTN].click().run()
    assert at.session_state["attempts"] == 0
