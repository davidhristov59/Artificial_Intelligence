from constraint import *


if __name__ == '__main__':

    problem = Problem()

    variables = range(0, 16) #polinjata
    domain = range(1, 17) #vrednostite

    problem.addVariables(variables, domain)

    #vo sekoe pole sakame da iamme razlicen broj

    problem.addConstraint(AllDifferentConstraint()) #bidejki sakame da ni bidat site polinja so razlicna vrednost

    #sumata na redicite, kolonite i dijagonalata da bide razlicna

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34), [row * 4 + i for i in range(4)])  # sumata mora da bide 34 i se odnesuva na promenlivite

    for column in range(4):
        problem.addConstraint(MaxSumConstraint(34), [column + j for j in range(4)])

    #dijagonalata
    problem.addConstraint(ExactSumConstraint(34), range(0, 16, 5))
    problem.addConstraint(ExactSumConstraint(34), range(3, 13, 3))

    solution = problem.getSolution()

    print(solution)



