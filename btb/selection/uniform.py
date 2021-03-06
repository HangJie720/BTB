import random

from btb.selection.selector import Selector


class Uniform(Selector):
    def select(self, choice_scores):
        """Select a choice uniformly at random."""
        return self.choices[random.randint(0, len(self.choices) - 1)]
