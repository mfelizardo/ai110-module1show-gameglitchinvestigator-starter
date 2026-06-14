from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_hint_says_lower():
    # When the guess is too high, the hint must tell the player to go LOWER
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected hint to say LOWER, got: {message!r}"

def test_too_low_hint_says_higher():
    # When the guess is too low, the hint must tell the player to go HIGHER
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected hint to say HIGHER, got: {message!r}"

def test_hints_are_not_inverted():
    # Regression: original bug had "Too High" say go higher and "Too Low" say go lower
    _, high_msg = check_guess(99, 1)
    _, low_msg = check_guess(1, 99)
    assert "LOWER" in high_msg, f"Too High hint should say LOWER, got: {high_msg!r}"
    assert "HIGHER" in low_msg, f"Too Low hint should say HIGHER, got: {low_msg!r}"
