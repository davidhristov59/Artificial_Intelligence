from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from zad1_dataset import dataset

if __name__ == '__main__':

    x = float(input())
    x /= 100
    crit = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset]) #osven poslednata kolona - MORA VO LIST

    train_set = dataset[int((1.0 - x) * len(dataset)):] #poslednite 80% za treniranje
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[:int((1.0 - x) * len(dataset))] #prvite 20% za testiranje
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion=crit, random_state=0)
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = float(accuracy / len(test_set))

    print(f'Accuracy: {accuracy}')

    #feature_importances

    feature_importances = list(classifier.feature_importances_)

    most_important_features = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {most_important_features}')

    least_important_features = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {least_important_features}')




