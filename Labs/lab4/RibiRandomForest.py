from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from zad2_dataset import dataset

if __name__ == '__main__':

    #neprekinat tip - RandomForest

    col_index = int(input())
    num_trees = int(input())
    crit = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    #train_set = dataset[:int(0.85 * len(dataset))]
    train_set = [row[:col_index] + row[col_index + 1:] for row in dataset[:int(0.85 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    #row[:col_index] - gi zima kolonite pred col_index
    #row[col_index + 1 :] - gi zima site koloni posle col_index

    #test_set = dataset[int(0.85 * len(dataset)):]
    test_set = [row[:col_index] + row[col_index + 1:] for row in dataset[int(0.85 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_trees, criterion=crit, random_state=0)
    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = float(accuracy) / len(test_set)

    print(f'Accuracy: {accuracy}')

    #nov zapis koj treba da se klasificira so treniraniot klasifikator
    entry = [int(el) for el in input().split(' ')]
    #encoded_entry = encoder.transform([entry])[0]
    del entry[col_index]

    print(classifier.predict([entry])[0])
    print(classifier.predict_proba([entry])[0])

    #submit_train_data(train_X, train_Y)
    #submit_test_data(test_X, test_Y)
    #submit_classifier(classifier)