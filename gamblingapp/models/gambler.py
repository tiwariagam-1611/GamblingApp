class Gambler:
    def __init__(self, name, initial_stake, win_limit, loss_limit):
        self.name = name
        self.initial_stake = initial_stake
        self.current_stake = initial_stake
        self.win_limit = win_limit
        self.loss_limit = loss_limit
        self.total_bets = 0
        self.wins = 0
        self.losses = 0