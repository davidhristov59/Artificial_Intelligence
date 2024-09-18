from sklearn.tree import DecisionTreeClassifier
import csv
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        ds = list(csv_reader)[1:]

    return ds


if __name__ == '__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)  # transformacija vo celobrojni

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)  # transformacija vo celobrojni

# ----------------------------------------------------------------------------------------

    # tree_classifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, max_leaf_nodes=20, random_state=0)
    tree_classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    tree_classifier.fit(train_x, train_y)  # karakteristikite gi predavame

    print(f'Depth = {tree_classifier.get_depth()}')
    print(f'Number of leaves = {tree_classifier.get_n_leaves()}')

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = tree_classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'Accuracy: {accuracy}')

    # samo za drva na odluka - koja karakteristika vlijae najmnogu od 6te

    feature_importances = list(tree_classifier.feature_importances_)
    print(f'Feature importances {feature_importances}')

    most_important_features = feature_importances.index(max(feature_importances))  # najvazna karakteristika
    print(f'Most important feature: {most_important_features}')

    least_important_feature = feature_importances.index(min(feature_importances))  # najmalku vazna karakteristika
    print(f'Least important feature: {least_important_feature}')

# ------------------------------------------------------------------------------------------

    # most important feature
    train_x_2 = list()  # celoto mnozestvo osven taa koja e najvazna
    for t in train_x:
        row = [t[i] for i in range(0, len(t)) if
               i != most_important_features]  # ke gi smestime site vrednosti i ke vratime t[row]
        train_x_2.append(row)

    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(0, len(t)) if i != most_important_features]
        test_x_2.append(row)

    tree_classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    tree_classifier2.fit(train_x_2, train_y)  # klasata si ostanuva

    print(f'Depth (without most important feature): {tree_classifier2.get_depth()}')
    print(f'Number of leaves (without most important feature): {tree_classifier2.get_n_leaves()}')

    accuracy2 = 0
    for i in range(len(test_set)):
        predicted_class = tree_classifier2.predict([test_x_2[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy2 += 1

    accuracy2 = accuracy2 / len(test_set)

    print(f'Accuracy (without most important feature): {accuracy2}')

# ----------------------------------------------------------------------------------------

    # least important feature
    train_x_3 = list()
    for t in train_x:
        row = [t[i] for i in range(0, len(t)) if i != least_important_feature]
        train_x_3.append(row)

    test_x_3 = list()
    for t in test_x:
        row = [t[i] for i in range(0, len(t)) if i != least_important_feature]
        test_x_3.append(row)

    tree_classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    tree_classifier3.fit(train_x_3, train_y)  # klasata si ostanuva

    print(f'Depth (without least important feature): {tree_classifier3.get_depth()}')
    print(f'Number of leaves (without least important feature): {tree_classifier3.get_n_leaves()}')

    accuracy3 = 0
    for i in range(len(test_set)):
        predicted_class = tree_classifier3.predict([test_x_3[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy3 += 1

    accuracy3 = accuracy3 / len(test_set)

    print(f'Accuracy (without least important feature): {accuracy3}')

# ----------------------------------------------------------------------------------------
