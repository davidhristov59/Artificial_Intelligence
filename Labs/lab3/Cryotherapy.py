from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder
import csv

dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':

    #neprekinat tip - koristime GaussianNB

    dataset = [[float(i) for i in row] for row in dataset_sample] #???

    train_set = dataset_sample[:int(0.85 * len(dataset_sample))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset_sample[int(0.85 * len(dataset_sample)):]
    test_x = [row[:-1] for row in train_set]
    test_y = [row[-1] for row in train_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    entry = [float(el) for el in input().split(' ')]

    predicted_class = int(classifier.predict([entry])[0])
    predicted_class_proba = classifier.predict_proba([entry])

    print(accuracy)
    print(predicted_class)
    print(predicted_class_proba)

    # submit na trenirachkoto mnozestvo
    #submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    #submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    #submit_classifier(classifier)