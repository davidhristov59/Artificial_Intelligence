from searching_framework.informed_search import *
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def check_valid(state):
    zelka, volk, jare, farmer = state

    if zelka == jare:
        if zelka != farmer:
            return False
    if jare == volk:
        if farmer != jare:
            return False
    return True


class Farmer(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        zelka, volk, jare, farmer = state

        # farmer se prenesuva sam sebesi
        if farmer == "w":
            farmer_new = "e"
        else:
            farmer_new = "w"

            state_new = (farmer_new, zelka, volk, jare)

            if check_valid(state_new):
                successors["Farmer nosi farmer"] = state_new

        # farmer nosi volk
        if farmer == volk:
            if volk == "w":
                volk_new = "e"
            else:
                volk_new = "w"

            state_new = (farmer_new, zelka, volk_new, jare)

            if check_valid(state_new):
                successors["Farmer nosi volk"] = state_new

        # farmer nosi jare
        if farmer == jare:
            if jare == "w":
                jare_new = "e"
            else:
                jare_new = "w"

            state_new = (farmer_new, zelka, volk, jare_new)

            if check_valid(state_new):
                successors["Farmer nosi jare"] = state_new

        if farmer == zelka:
            if zelka == "w":
                zelka_new = "e"
            else:
                zelka_new = "w"

            state_new = (farmer_new, zelka_new, volk, jare)

            if check_valid(state_new):
                successors["Farmer nosi zelka"] = state_new

        return successors

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def goal_test(self, state):
        return state == ("w", "w", "w", "w")

    def h(self, node): #Hamingovo rastojanie pomegju sostojbi - broj na razlicni bukvi pomegju tekvonata i celnat sostojba

        count = 0
        #momentalnata sostojba
        state = node.state
        #celnata sostojba
        goal_s = self.goal

        for x,y in zip(state,goal_s): #gi broi razlicnite bukvi - bukvite koi sto ne se na ista pozicija
            if x != y:
                count += 1

        return count

if __name__ == '__main__':
    initial_state = ("e", "e", "e", "e")
    goal_state = ("w", "w", "w", "w")

    farmer = Farmer(initial_state, goal_state)

    result_uninformed = breadth_first_graph_search(farmer)
    print(result_uninformed.solution())
    print(result_uninformed.solve())

    result_informed = astar_search(farmer)
    print(result_informed.solution())
    print(result_informed.solve())
