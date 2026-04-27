from models.exceptions import *
from models.validation_type import ValidationErrorType
import math


class InputValidator:

    def validate_initial_stake(self, stake):
        if stake is None:
            raise StakeValidationException("Stake cannot be null")

        if not isinstance(stake, (int, float)):
            raise StakeValidationException("Stake must be numeric")

        if math.isnan(stake) or math.isinf(stake):
            raise StakeValidationException("Invalid numeric value")

        if stake <= 0:
            raise StakeValidationException("Stake must be positive")

        return True


    def validate_bet_amount(self, bet, current):
        if bet <= 0:
            raise BetValidationException("Bet must be positive")

        if bet > current:
            raise BetValidationException("Bet exceeds current stake")

        return True


    def validate_limits(self, stake, win_limit, loss_limit):
        if win_limit <= stake:
            raise LimitValidationException("Win limit must be greater than stake")

        if loss_limit >= stake:
            raise LimitValidationException("Loss limit must be less than stake")

        return True


    def validate_probability(self, probability):
        if probability < 0 or probability > 1:
            raise ProbabilityValidationException("Probability must be between 0 and 1")

        return True


    def parse_number(self, value):
        try:
            num = float(value)

            if math.isnan(num) or math.isinf(num):
                raise ValidationException("Invalid numeric value")

            return num

        except:
            raise ValidationException("Invalid input, not a number")