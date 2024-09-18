from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def move_footballer(player_x, player_y, ball_x, ball_y, direction, opponents):
    if direction == "gore":
        if player_y + 1 < 6 and (player_x, player_y + 1) not in opponents and (player_x, player_y + 1) != (
                ball_x, ball_y):
            player_y += 1

    elif direction == "dolu":
        if player_y >= 0 and (player_x, player_y - 1) not in opponents and (player_x, player_y - 1) != (ball_x, ball_y):
            player_y -= 1

    elif direction == "desno":
        if player_x + 1 < 8 and (player_x + 1, player_y) not in opponents and (player_x + 1, player_y) != (ball_x, ball_y):
            player_x += 1

    elif direction == "gore-desno":
        if player_x + 1 < 8 and player_y + 1 < 6 and (player_x + 1, player_y + 1) not in opponents and (
                player_x + 1, player_y + 1) != (ball_x, ball_y):
            player_y += 1
            player_x += 1

    else:  # dolu-desno
        if player_x + 1 < 8 and player_y - 1 >= 0 and (player_x + 1, player_y - 1) not in opponents and (
                player_x + 1, player_y - 1) != (ball_x, ball_y):
            player_x += 1
            player_y -= 1

    return player_x, player_y


def move_ball(player_x, player_y, ball_x, ball_y, direction, opponents):
    if direction == "gore":
        if ball_y + 1 < 6 and (ball_x, ball_y + 1) not in opponents:
            return ball_x, ball_y + 1

    elif direction == "dolu":
        if ball_y - 1 >= 0 and (ball_x, ball_y - 1) not in opponents:
            return ball_x, ball_y - 1

    elif direction == "desno":
        if ball_x + 1 < 8 and (ball_x + 1, ball_y) not in opponents:
            return ball_x + 1, ball_y

    elif direction == "gore-desno":
        if ball_x + 1 < 8 and ball_y + 1 < 6 and (ball_x + 1, ball_y + 1) not in opponents:
            return ball_x + 1, ball_y + 1

    else:  # dolu-desno
        if ball_x + 1 < 8 and ball_y - 1 >= 0 and (ball_x + 1, ball_y - 1) not in opponents:
            return ball_x + 1, ball_y - 1

    return ball_x, ball_y


class Football(Problem):

    # staticni - konstanti - gol i protivnici, tablata - STAVAME VO CONSTRUCTOR

    def __init__(self, initial, opponents_coord, goal_coord):
        super().__init__(initial, goal=None)
        self.opponents = opponents_coord
        self.goal_coord = goal_coord

    def successor(self, state):
        successors = dict()

        # State = ((player_x, player_y), (ball_x, ball_y))
        player_x, player_y = state[0]
        ball_x, ball_y = state[1]

        directions = ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]

        for direction in directions:

            # Move footballer
            new_player_x, new_player_y = move_footballer(player_x, player_y, ball_x, ball_y, direction, self.opponents)
            if (new_player_x, new_player_y) != (player_x, player_y):
                successors[f"Pomesti coveche {direction}"] = ((new_player_x, new_player_y), (ball_x, ball_y))

            # Move player and ball
            if (new_player_x, new_player_y) == (ball_x, ball_y):
                new_ball_x, new_ball_y = move_ball(new_player_x, new_player_y, ball_x, ball_y, direction, self.opponents)
                if (new_ball_x, new_player_x) != (ball_x, ball_y):
                    successors[f"Turni topka {direction}"] = ((new_player_x, new_player_y), (new_ball_x, new_ball_y))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ball_x, ball_y = state[0]
        return (ball_x, ball_y) == (7, 2) or (ball_x, ball_y) == (7, 3)


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(",")))
    ball_pos = tuple(map(int, input().split(",")))

    opponent_position = ((3, 3), (5, 4))
    goal_position = ((7,2), (7,3))

    initial_state = (tuple(man_pos), tuple(ball_pos))

    football = Football(initial_state, opponent_position, goal_position)

    result = breadth_first_graph_search(football)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
