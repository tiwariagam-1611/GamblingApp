from services.validator_service import InputValidator

validator = InputValidator()


def get_float(prompt):
    while True:
        value = input(prompt)
        try:
            num = validator.parse_number(value)
            return num
        except Exception as e:
            print("Error:", e)


def get_positive_stake(prompt):
    while True:
        try:
            value = get_float(prompt)
            validator.validate_initial_stake(value)
            return value
        except Exception as e:
            print("Error:", e)