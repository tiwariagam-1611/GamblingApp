class Strategy:
    def __init__(self, name, probability, multiplier):
        self.name = name
        self.probability = probability
        self.multiplier = multiplier


def get_strategy(choice):
    if choice == "1":
        return Strategy("EASY", 0.7, 1)
    elif choice == "2":
        return Strategy("MEDIUM", 0.5, 2)
    elif choice == "3":
        return Strategy("HARD", 0.3, 3)
    else:
        return Strategy("MEDIUM", 0.5, 2)