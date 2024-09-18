from constraint import *

if __name__ == '__main__':

    problem = Problem()

    domain = range(0, 8)
    rooks = range(0, 8)

    problem.addVariables(rooks, domain)

    # not in same row
    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 != rook2:
                problem.addConstraint(lambda r1, r2: r1 != r2, (rook1, rook2))

    solution = problem.getSolution()
    print(solution)
