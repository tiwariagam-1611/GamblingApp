class GameResult:
    def __init__(self, amount, outcome, winnings, stake_before, stake_after):
        self.amount = amount
        self.outcome = outcome
        self.winnings = winnings
        self.stake_before = stake_before
        self.stake_after = stake_after

    def display(self):
        print("Outcome:", self.outcome)
        print("Bet:", self.amount)
        print("Winnings:", self.winnings)
        print("Before:", self.stake_before)
        print("After:", self.stake_after)