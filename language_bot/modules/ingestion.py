import csv

def load_words(path):
    words = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['priority'] = 1
            words.append(row)
    return words