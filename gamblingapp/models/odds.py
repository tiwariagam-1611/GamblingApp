class Odds:
    @staticmethod
    def fixed(multiplier, amount):
        return amount * multiplier

    @staticmethod
    def probability_based(probability, amount):
        return amount / probability

    @staticmethod
    def decimal(decimal_odds, amount):
        return amount * decimal_odds

    @staticmethod
    def american(odds, amount):
        if odds > 0:
            return amount * (odds / 100)
        else:
            return amount * (100 / abs(odds))