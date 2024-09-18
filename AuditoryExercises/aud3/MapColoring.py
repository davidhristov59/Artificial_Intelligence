from constraint import *

def different(a,b):
    return a != b

if __name__ == '__main__':
    problem = Problem()

    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    domains = ["red", "green", "blue"]

    problem.addVariables(variables, domains)

    #constraints
    problem.addConstraint(different, ("WA", "NT"))
    problem.addConstraint(different, ("WA", "SA"))
    problem.addConstraint(different, ("SA", "NSW"))
    problem.addConstraint(different, ("SA", "V"))
    problem.addConstraint(different, ("SA", "Q"))
    problem.addConstraint(different, ("SA", "NT"))
    problem.addConstraint(different, ("NT", "Q"))
    problem.addConstraint(different, ("Q", "NSW"))
    problem.addConstraint(different, ("NSW", "V"))

    solution = problem.getSolution() #prvo resenie

    print(solution)