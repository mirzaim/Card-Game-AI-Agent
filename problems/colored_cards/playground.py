from search_algorithms.classic import WellDefinedProblem, State
import itertools
import re


class Card:
    joker = None

    @classmethod
    def get_joker(cls):
        if cls.joker is None:
            cls.joker = Card('inf', '')
        return cls.joker

    def __init__(self, number, color):
        self.number = float('inf') if number == 'inf' else int(number)
        self.color = color

    def __eq__(self, other):
        return (self.number == other.number) and (self.color == other.color)

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number

    def __str__(self):
        return f'{self.number}{self.color}'

    def __repr__(self):
        return f'{self.number}{self.color}'


class Playground(State):

    @classmethod
    def parse(cls):
        playground = Playground(*list(map(int, input().split())))
        for part in playground.parts:
            for number, color in re.findall("([1-9]+)([a-zA-Z]+)", input()):
                part.append(Card(number, color))
        return playground

    def __init__(self, n, m, k):
        super().__init__()
        self.n = n
        self.m = m
        self.k = k
        self.parts = [[] for _ in range(k)]

    def add_card(self, col: int, card: Card):
        self.parts[col].append(card)

    def pop_top_card(self, col: int):
        return self.parts[col].pop()

    def get_top_cards(self):
        return [(col, part[-1]) if part else (col, Card.get_joker()) for col, part in enumerate(self.parts)]

    def copy(self):
        result = Playground(self.n, self.m, self.k)
        result.parts = [part.copy() for part in self.parts]
        return result

    def is_goal(self):
        return all(
            (all((part[i] > part[i + 1]) and (part[i].color == part[i + 1].color) for i in range(len(part) - 1)))
            for part in self.parts)

    def heuristic(self) -> int:
        counter = 0
        for part in self.parts:
            if len(part) >= 2 and ((part[0] < part[1]) or (part[0].color != part[1].color)):
                counter += (len(part) - 1)
        return counter

    def __lt__(self, other):
        pass

    def __eq__(self, other):
        return self.parts == other.parts

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        result = ""
        for part in self.parts:
            result += (' '.join([str(card) for card in part]) if part else '#')
            result += "\n"
        return result


class ColoredCards(WellDefinedProblem):
    def __init__(self, initial_state: Playground):
        super().__init__(initial_state)

    def actions(self, state: Playground) -> list:
        return [(x[0], y[0]) for x, y in itertools.permutations(state.get_top_cards(), 2) if (x[1] < y[1])]

    def result(self, state: Playground, action) -> Playground:
        new_state = state.copy()
        new_state.add_card(action[1], new_state.pop_top_card(action[0]))
        return new_state

    def is_goal(self, state: Playground) -> bool:
        return state.is_goal()

    def heuristic(self, state: Playground) -> int:
        return state.heuristic()
