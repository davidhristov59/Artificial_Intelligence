from searching_framework.informed_search import *
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class ExplorerInformed(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):

        successors = dict()

        man_x, man_y = state[0], state[1]
        obstacle1 = list(state[2])
        obstacle2 = list(state[3])

        if obstacle1[2] == 1:  # gore
            if obstacle1[1] == self.grid_size[1] - 1:  # ako e najgore
                obstacle1[2] = -1  # odi dole - se dvizi dole
                obstacle1[1] -= 1  # po y - koord namaluvame
            else:
                obstacle1[1] += 1
        else:
            if obstacle1[1] == 0:  # ako e stignato najdole
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] -= 1

        if obstacle2[2] == 1:  # gore
            if obstacle2[1] == self.grid_size[1] - 1:  # ako e najgore
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else:
                obstacle2[1] += 1
        else:
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles = [(obstacle1[0], obstacle1[1]), (obstacle2[0], obstacle2[1])]

        # right
        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:
            successors["RIGHT"] = (
                man_x + 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                (obstacle2[0], obstacle2[1], obstacle2[2]))

            # left
        if man_x > 0 and (man_x - 1, man_y) not in obstacles:
            successors["LEFT"] = (man_x - 1, man_y, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                  (obstacle2[0], obstacle2[1], obstacle2[2]))

            # up
        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successors["UP"] = (man_x, man_y + 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                (obstacle2[0], obstacle2[1], obstacle2[2]))

            # down
        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["DOWN"] = (man_x, man_y - 1, (obstacle1[0], obstacle1[1], obstacle1[2]),
                                  (obstacle2[0], obstacle2[1], obstacle2[2]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def h(self, node):
        x_man = node.state[0]
        y_man = node.state[1]

        x_house = self.goal[0]
        y_house = self.goal[1]

        return abs(x_man - x_house) + abs(y_man - y_house)


if __name__ == '__main__':
    man_position = (0, 2)
    goal_position = (7, 4)
    obstacle1 = (2, 5, -1)
    obstacle2 = (5, 0, 1)

    explorer_informed = ExplorerInformed((man_position[0], man_position[1], obstacle1, obstacle2), goal_position)

    result = astar_search(explorer_informed)

    if result is not None:
        print(result.solution())
        print(result.solve())
    else:
        print("no Solution")
