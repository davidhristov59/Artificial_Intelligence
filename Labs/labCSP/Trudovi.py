from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = list(papers.keys())

    domain = [f'T{i + 1}' for i in range(num)] #domen

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    topics = {}
    for title, topic in papers.items():
        if topic not in topics:
            topic[topics] = []
        topics[topic].append(title)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    ...
