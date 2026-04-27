import random

class RandomOutcomeStrategy:
    def determine(self, probability):
        return "win" if random.random() < probability else "loss"


class WeightedProbabilityStrategy:
    def __init__(self, house_edge=0.02):
        self.house_edge = house_edge

    def determine(self, probability):
        adjusted = probability - self.house_edge
        return "win" if random.random() < adjusted else "loss"