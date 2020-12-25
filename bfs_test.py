import problems.colored_cards.playground as pl
import search_algorithms.classic as s


def main():
    print("Enter initial state.")
    initial_state = pl.Playground.parse()
    game = pl.ColoredCards(initial_state)
    s.bfs(game)
    print(f'depth: {game.result_state.depth}')
    for state, action in game.get_solution_path():
        print(f'{action[0]} --> {action[1]}')

    print('solution:')
    print(game.result_state)
    print(f'expanded nodes: {game.num_expanded_node}')
    print(f'produced nodes: {game.num_produced_node}')


if __name__ == '__main__':
    main()
