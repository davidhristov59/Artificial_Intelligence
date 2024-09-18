from searching_framework.informed_search import *
from searching_framework.utils import Problem


class ManHouse(Problem):

    def __init__(self, initial, allowed_obstacles, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [5, 9]
        self.allowed_obstacles = allowed_obstacles

    def successor(self, state):

        successors = dict()

        man_x, man_y, house_x, house_y, direction = state

        # house
        if house_x == "levo":
            if house_x == 0:
                direction = "desno"
                house_x = 1
            else:
                house_x -= 1  # odi nakaj levo
        else:  # desno
            if house_x == 4:
                direction = "levo"
                house_x = 3
            else:  # ako e vo desniot del ama ne e na kraj i odi levo
                house_x += 1  # odi nakaj desno

        self.allowed_obstacles.append((house_x, house_y))

        successors["Stoj"] = (man_x, man_y, house_x, house_y, direction)

        # Man movement
        for i in range(1, 3):  # za 1 ili 2 pozicii se dvizi
            # gore
            new_man_y = man_y + i
            if new_man_y < 9 and (man_x, new_man_y) in self.allowed_obstacles:
                new_state_man = (man_x, new_man_y, house_x, house_y, direction)
                successors[f'Gore {i}'] = new_state_man

            # gore-desno
            new_man_y = man_y + i
            new_man_x = man_x + i
            if new_man_x < 5 and new_man_y < 9 and (new_man_x, new_man_y) in self.allowed_obstacles:
                new_state_man = (new_man_x, new_man_y, house_x, house_y, direction)
                successors[f'Gore-desno {i}'] = new_state_man

            # gore-levo
            new_man_y = man_y + i
            new_man_x = man_x - i
            if new_man_x > 0 and new_man_y < 9 and (new_man_x, new_man_y) in self.allowed_obstacles:
                new_state_man = (new_man_x, new_man_y, house_x, house_y, direction)
                successors[f'Gore-levo {i}'] = new_state_man

        self.allowed_obstacles.remove((house_x, house_y))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_x, man_y, house_x, house_y = state[0], state[1], state[2], state[3]
        return man_x == house_x and man_y == house_y

    def h(self, node):
        man_x, man_y, house_x, house_y = node.state
        goal_x, goal_y = house_x, house_y

        return abs(man_y - goal_y) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    grid_size = (5, 9)

    man_x, man_y = map(int, input().split(","))
    goal_x, goal_y = map(int, input().split(","))
    direction = input()

    maze = ManHouse((man_x, man_y, goal_x, goal_y, direction), allowed)

    result = astar_search(maze).solution()

    if result is not None:
        print(result)
    else:
        print("No solution!")