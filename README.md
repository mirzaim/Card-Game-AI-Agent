# Card Game AI Agent

This repository contains implementations of various search algorithms applied to problem-solving, focusing on a **[Simple Card Game](#simple-card-game)**.

## Project Structure

```
.
├── Pipfile
├── a_star_test.py
├── bfs_test.py
├── ids_test.py
├── problems
│   └── colored_cards
│       └── playground.py  # The problem setup and state definitions
└── search_algorithms
    └── classic.py         # The core search algorithms
```

## Simple Card Game

### Problem Description
You have `M` colors of cards, each numbered 1 to `N`, arranged in `K` columns. The goal is to sort the cards such that:
- Each column contains cards of the same color.
- Cards in each column are sorted in descending order.

You can only move the top card from one column to another if the destination card has a higher number.

### Search Algorithms
Three different search algorithms are implemented to solve this problem:
1. **Breadth-First Search (BFS)**: Explores the state space level by level.
2. **Iterative Deepening Search (IDS)**: Combines depth-first and breadth-first approaches by progressively deepening the search limit.
3. **A-Star Search**: Uses a heuristic function to optimize the search by prioritizing states closer to the goal.

### Classes Overview

- **Card**: Represents a card with a number and color.
- **Playground**: Represents the state of the game, including card arrangement and available actions.
- **ColoredCards**: Defines the problem by specifying the initial state, available actions, and goal state.
- **WellDefinedProblem**: An abstract class defining the structure for a problem that can be solved using search algorithms.

### Sample Input
```
4 3 5   # 4 numbers, 3 colors, 5 columns
4y
2g 4r 3y 3g 2y
1y 4g 1r
1g 2r 3r
#
```

### Sample Output
```
started
depth: 12
1 --> 3
2 --> 3
2 --> 4
1 --> 4
1 --> 0
3 --> 4
3 --> 0
2 --> 0
1 --> 2
3 --> 2
3 --> 2
4 --> 2
solution:
4y 3y 2y 1y
2g
4r 3r 2r 1r
1g
4g 3g

expanded nodes: 1510
produced nodes: 12397
```

### Usage

To play the game, follow these steps:
1. Clone the repository.
2. Install the required dependencies using `pipenv install`.
3. For each algorithm, choose one of `a_star_test.py`, `ids_test.py`, or `bfs_test.py` to run.
