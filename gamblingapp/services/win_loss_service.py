from models.game_result import GameResult
from models.odds import Odds
from services.outcome_strategy import RandomOutcomeStrategy

class WinLossCalculator:

    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0
        self.current_streak = 0
        self.max_win_streak = 0
        self.max_loss_streak = 0
        self.last_result = None

    def process(self, amount, probability, stake_before):

        strategy = RandomOutcomeStrategy()
        outcome = strategy.determine(probability)

        if outcome == "win":
            winnings = Odds.fixed(2, amount)
            stake_after = stake_before + winnings

            self.total_wins += 1

            if self.last_result == "win":
                self.current_streak += 1
            else:
                self.current_streak = 1

            self.max_win_streak = max(self.max_win_streak, self.current_streak)

        else:
            winnings = -amount
            stake_after = stake_before - amount

            self.total_losses += 1

            if self.last_result == "loss":
                self.current_streak += 1
            else:
                self.current_streak = 1

            self.max_loss_streak = max(self.max_loss_streak, self.current_streak)

        self.last_result = outcome

        return GameResult(amount, outcome, winnings, stake_before, stake_after)

    def stats(self):
        total = self.total_wins + self.total_losses
        win_rate = (self.total_wins / total * 100) if total else 0

        print("Wins:", self.total_wins)
        print("Losses:", self.total_losses)
        print("Win rate:", win_rate)
        print("Max win streak:", self.max_win_streak)
        print("Max loss streak:", self.max_loss_streak)