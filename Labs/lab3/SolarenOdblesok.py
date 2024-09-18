from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from zad1_dataset import dataset
import csv

if __name__ == '__main__':

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset]) #osven poslednata kolona bidejki taa e klasa

    train_set = dataset[:int(0.75 * len(dataset))] #prvite 75%
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.75 * len(dataset)):] #ostanatite 25%
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    entry = [el for el in input().split(" ")]
    encoded_entry = encoder.transform([entry])

    predicted_class = classifier.predict(encoded_entry)[0]
    predicted_class_proba = classifier.predict_proba(encoded_entry)[0]

    print(accuracy)
    print(predicted_class)
    print(predicted_class_proba)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    #submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    #submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    #submit_classifier(classifier)

    # submit na encoderot
    #submit_encoder(encoder)