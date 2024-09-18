from searching_framework.informed_search import *
from searching_framework.utils import Problem

class Maze(Problem):

    def __init__(self, initial, grid_size, obstacles, goal = None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.grid_size = grid_size

    def successor(self, state):

        successors = dict()

        man_x, man_y, house_x, house_y, direction = state

        for i in range(2,4):
            valid_move = True
            for j in range(i):
                new_x = man_x + j + 1
                if new_x >= self.grid_size and (new_x, man_y) in self.obstacles:
                    valid_move = False
                    break
            if valid_move: #desno
                new_x = man_x + i
                state_new = (new_x, man_y)
                successors[f"Desno {i}"] = state_new

            #ostanati nasoki

            #gore
            new_y = man_y + 1
            if new_y < self.grid_size and (man_x, new_y) not in self.obstacles:
                state_new = (man_x, new_y)
                successors["Gore"] = state_new

            #dolu
            new_y = man_y - 1
            if new_y >= 0 and (man_x, new_y) not in self.obstacles:
                state_new = (man_x, new_y)
                successors["Dolu"] = state_new

            #levo
            new_x = man_x - 1
            if new_x >= 0 and (new_x, man_y) not in self.obstacles:
                state_new = (new_x, man_y)
                successors["Levo"] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man_x, man_y, house_x, house_y = state[0], state[1], state[2], state[3]

        return man_x == house_x and man_y == house_y

    def h(self, node): #mhd
        man_x, man_y = node.state
        house_x, house_y = self.goal

        return (abs(man_x - house_x) + abs(man_y - house_y)) / 3


if __name__ == '__main__':

    n = int(input())
    num_walls = int(input())

    walls = set()
    for _ in range(num_walls):
        wall_x, wall_y = map(int, input().split(","))
        walls.add((wall_x, wall_y))

    man_position_x, man_position_y = map(int,input().split(","))
    start_state = (man_position_x, man_position_y)

    house_position_x, house_position_y = map(int, input().split(","))
    goal_state = (house_position_x, house_position_y)

    maze = Maze(start_state, n, walls, goal_state)

    result = astar_search(maze).solution()

    if result is not None:
        print(result)
    else:
        print("No Solution")





