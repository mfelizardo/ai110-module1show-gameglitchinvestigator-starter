import pytest
from logic_utils import update_score

EASY_LIMIT = 6
NORMAL_LIMIT = 8
HARD_LIMIT = 5


class TestWinFirstAttempt:
    def test_easy_first_attempt_scores_100(self):
        assert update_score("Win", attempt_number=1, attempt_limit=EASY_LIMIT) == 100

    def test_normal_first_attempt_scores_100(self):
        assert update_score("Win", attempt_number=1, attempt_limit=NORMAL_LIMIT) == 100

    def test_hard_first_attempt_scores_100(self):
        assert update_score("Win", attempt_number=1, attempt_limit=HARD_LIMIT) == 100


class TestWinLastAttempt:
    def test_easy_last_attempt_above_zero(self):
        assert update_score("Win", attempt_number=EASY_LIMIT, attempt_limit=EASY_LIMIT) > 0

    def test_normal_last_attempt_above_zero(self):
        assert update_score("Win", attempt_number=NORMAL_LIMIT, attempt_limit=NORMAL_LIMIT) > 0

    def test_hard_last_attempt_above_zero(self):
        assert update_score("Win", attempt_number=HARD_LIMIT, attempt_limit=HARD_LIMIT) > 0

    def test_easy_last_attempt_exact_score(self):
        # round(100 * 1/6) = 17
        assert update_score("Win", attempt_number=EASY_LIMIT, attempt_limit=EASY_LIMIT) == 17

    def test_normal_last_attempt_exact_score(self):
        # round(100 * 1/8) = 12
        assert update_score("Win", attempt_number=NORMAL_LIMIT, attempt_limit=NORMAL_LIMIT) == 12

    def test_hard_last_attempt_exact_score(self):
        # round(100 * 1/5) = 20
        assert update_score("Win", attempt_number=HARD_LIMIT, attempt_limit=HARD_LIMIT) == 20


class TestLoss:
    def test_easy_loss_scores_zero(self):
        assert update_score("Too High", attempt_number=EASY_LIMIT, attempt_limit=EASY_LIMIT) == 0

    def test_normal_loss_scores_zero(self):
        assert update_score("Too Low", attempt_number=NORMAL_LIMIT, attempt_limit=NORMAL_LIMIT) == 0

    def test_hard_loss_scores_zero(self):
        assert update_score("Too High", attempt_number=HARD_LIMIT, attempt_limit=HARD_LIMIT) == 0


class TestScoreDecreasesWithAttempts:
    def test_normal_score_decreases_each_attempt(self):
        scores = [
            update_score("Win", attempt_number=i, attempt_limit=NORMAL_LIMIT)
            for i in range(1, NORMAL_LIMIT + 1)
        ]
        assert scores == sorted(scores, reverse=True)

    def test_hard_score_decreases_each_attempt(self):
        scores = [
            update_score("Win", attempt_number=i, attempt_limit=HARD_LIMIT)
            for i in range(1, HARD_LIMIT + 1)
        ]
        assert scores == sorted(scores, reverse=True)


class TestScoreRange:
    def test_all_win_scores_in_range(self):
        for limit in (EASY_LIMIT, NORMAL_LIMIT, HARD_LIMIT):
            for attempt in range(1, limit + 1):
                score = update_score("Win", attempt_number=attempt, attempt_limit=limit)
                assert 0 <= score <= 100

    def test_wrong_guess_potential_score_in_range(self):
        for limit in (EASY_LIMIT, NORMAL_LIMIT, HARD_LIMIT):
            for attempt in range(1, limit + 1):
                score = update_score("Too High", attempt_number=attempt, attempt_limit=limit)
                assert 0 <= score <= 100
