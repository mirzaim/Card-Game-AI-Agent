from collections import deque
from queue import PriorityQueue
import itertools


class State:
    def __init__(self):
        self.parent = None
        self.action = None
        self.cost = 0
        self.depth = 0

    def set_data(self, parent, action, cost, depth):
        (self.parent, self.action, self.cost, self.depth) = (parent, action, cost, depth)


class WellDefinedProblem:
    def __init__(self, initial_state):
        self.initialState = initial_state
        self.result_state = None
        self.num_expanded_node = 0
        self.num_produced_node = 0

    def actions(self, state: State) -> list:
        return []

    def result(self, state: State, action) -> State:
        return None

    def is_goal(self, state: State) -> bool:
        return False

    def heuristic(self, state: State) -> int:
        return 0

    def path_cost(self, state1: State, action, state2: State) -> int:
        return 1

    def get_solution_path(self):
        result = []
        state = self.result_state
        while state.parent:
            result.append((state.parent, state.action))
            state = state.parent
        result.reverse()
        return result


def bfs(problem: WellDefinedProblem):
    if problem.is_goal(problem.initialState):
        problem.result_state = problem.initialState
        return problem.initialState
    frontier = deque([problem.initialState])
    explored = set()
    while frontier:
        parent = frontier.popleft()
        explored.add(parent)
        problem.num_expanded_node += 1
        for action in problem.actions(parent):
            child = problem.result(parent, action)
            if child not in frontier and child not in explored:
                child.set_data(parent, action,
                               parent.cost + problem.path_cost(parent, action, child),
                               parent.depth + 1)
                problem.num_produced_node += 1
                if problem.is_goal(child):
                    problem.result_state = child
                    return child
                frontier.append(child)
    return None


def ids(problem: WellDefinedProblem, start=0):
    def recursive_dls(node, problem: WellDefinedProblem, limit):
        if problem.is_goal(node):
            problem.result_state = node
            return node
        elif limit == 0:
            return None
        parent = node
        problem.num_expanded_node += 1
        for action in problem.actions(parent):
            child = problem.result(parent, action)
            child.set_data(parent, action,
                           parent.cost + problem.path_cost(parent, action, child),
                           parent.depth + 1)
            problem.num_produced_node += 1
            result = recursive_dls(child, problem, limit - 1)
            if result is not None:
                return result
        return None

    for i in itertools.count(start):
        result = recursive_dls(problem.initialState, problem, i)
        if result is not None:
            return result


def a_star(problem: WellDefinedProblem):
    if problem.is_goal(problem.initialState):
        problem.result_state = problem.initialState
        return problem.initialState
    explored = set()
    frontier = PriorityQueue()
    frontier.put(((problem.heuristic(problem.initialState), 0), problem.initialState))
    while frontier:
        parent = frontier.get()[1]
        explored.add(parent)
        problem.num_expanded_node += 1
        for action in problem.actions(parent):
            child = problem.result(parent, action)
            child.set_data(parent, action,
                           parent.cost + problem.path_cost(parent, action, child),
                           parent.depth + 1)
            problem.num_produced_node += 1
            if child not in explored and not any(child == item for priority, item in frontier.queue):
                if problem.is_goal(child):
                    problem.result_state = child
                    return child
                frontier.put(((child.cost + problem.heuristic(child), child.depth), child))
    return None
