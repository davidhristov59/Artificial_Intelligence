from constraint import *


def rooks_not_attacking(r1, r2):
    if r1[0] != r2[0] and r1[1] != r2[1]:  # ako nivnite redici se razlicni i kolonite da se razlicni
        return True
    else:
        return False


if __name__ == '__main__':

    problem = Problem()

    # domenot ke bide site polinja na tablata - GOLEM E
    domain = []
    for i in range(0, 8):  # redici
        for j in range(0, 8):  # koloni
            domain.append((i, j))

    rooks = range(0, 8)

    problem.addVariables(rooks, domain)

    # topovite da ne se napagaat - da bidat vo razlicen red i razlicna kolona

    for rook1 in rooks:  # za sekoj top
        for rook2 in rooks:
            if rook1 != rook2:
                problem.addConstraint(rooks_not_attacking, (rook1, rook2))
                # When you add a constraint using problem.addConstraint, you don't actually call the function with
                # arguments. Instead, you pass the function object itself along with the variables that the
                # constraint should apply to.

    solution = problem.getSolution()

    print(solution)
