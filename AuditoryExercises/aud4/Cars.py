import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        ds = list(csv_reader)[1:]

    return ds


if __name__ == '__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()

    encoder.fit([row[:-1] for row in dataset])  # trenira - potocno od koi podatoci go prai mapiranjeto, ke ja  vratime redicata osven poslednata kolona, od pocetok do -1

    # podatocnoto mnozestvo go delime na 2 podmnozestva
    # prvite procenti = za treniranje, ostanatite za testiranje

    train_set = dataset[:int(len(dataset) * 0.7)]  # od pocetok do prvite 70%
    # x - karakteristiki, y - klasa koja sto sakame da ja dobieme
    train_x = [row[:-1] for row in train_set]  # samo karakteristikite - od pocetok do pretposledniot element - ke vratime sve osven poslednata kolona
    train_y = [row[-1] for row in train_set] #samo klasata, samo poslednata kolona
    train_x = encoder.transform(train_x) #celobrojni

    test_set = dataset[int(0.7 * len(dataset)):]  # vtoriot del od tie 70% go zimame
    test_x = [row[:-1] for row in test_set] #vlezovi
    test_y = [row[-1] for row in test_set] #izlezi
    test_x = encoder.transform(test_x) #celobrojni - mapira vrednosti

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y) #karakteristiki se train_x i train_y

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'Accuracy {accuracy}')

    entry = [el for el in input().split(" ")]

    encoded_entry = encoder.transform([entry])
    predicted_class = classifier.predict(encoded_entry)

    print(predicted_class)
