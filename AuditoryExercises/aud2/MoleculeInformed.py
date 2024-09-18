from searching_framework.uninformed_search import *
from searching_framework.utils import Problem


# using while loops insise the movement function to continue moving something in a specific direction until one of the conditions is met

def move_right(x1, y1, x2, y2, x3, y3, obstacles):  # x1 + 1
    while x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3]:
        x1 += 1

    return x1


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1

    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 + 1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1

    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1

    return y1


class MoleculeInformed(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]

        # H1
        x_new = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["RightH1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        x_new = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["LeftH1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)

        y_new = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["UpH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["DownH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        # 0
        x_new = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["RightO"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        x_new = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["LeftO"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        y_new = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["UpO"] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["DownO"] = (h1_x, h1_x, o_x, y_new, h2_x, h2_y)

        # H2
        x_new = move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["RightH2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        x_new = move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["LeftH2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        y_new = move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["UpH2"] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        y_new = move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["DownH2"] = (h1_x, h1_x, o_x, o_y, h2_x, y_new)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if state[1] == state[3] == state[5]:  # gi proveruvame y-koordinatite
            return state[0] + 1 == state[2] and state[2] + 1 == state[4]
            # state[0] + 1 == state[2] - proveruva dali O molekulata e + 1 od desno na H1
            # state[4] - 1 == state[2] - proveruva dali 0 molekulata e -1 od levo na H2

        return False

    def h(self, node):
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]

        value = 0  # vrednosta na hevristikata - treba pomal broj da bide

        # spojuvame prvo h1 so o
        # odime so negacija prvo
        if h1[1] != o[1]:  # ako ne se vo ista redica
            if h1[0] != o[0] - 1:  # h1 ne e levo do o
                value += 2
            else:  # h1 da e levo do o
                value += 1
        else:  # da se vo ista redica
            if h1[0] > o[0]:  # h1 da e e desno od o
                value += 3
            elif h1[0] < o[0] - 1:  # h1 levo od o , no ne vednas
                value += 1

        # spojuvame sea h2 so o
        if h2[1] != o[1]:  # ne se vo ista redica
            if h2[0] != o[0] + 1:  # h2 ne e vednas do o od desno
                value += 3
            else:
                value += 2
        else:  # da se vo ista redica
            if h2[0] < o[0]:  # h2 da e levo od h2
                value += 3
            elif h2[0] > o[0] + 1:  # h2 da e vednas do o - desno do o
                value += 1

        if h1[1] == h2[1] and h1[1] != o[1]:  # h1 i h2 vo ista redica, o vo razlicna
            value -= 1

        return value


if __name__ == '__main__':
    moleculeH1 = [2, 1]
    molecule0 = [7, 2]
    moleculeH2 = [2, 6]

    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]

    molecule = MoleculeInformed(
        (moleculeH1[0], moleculeH1[1], molecule0[0], molecule0[1], moleculeH2[0], moleculeH2[1]),
        obstacles_list)

    print(breadth_first_graph_search(molecule).solution())
