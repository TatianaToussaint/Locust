import csv
import random


def get_row(csvfile):
    rows =[]
    with open(csvfile) as f:
        allrows = csv.reader(f)
        next(allrows)
        for row in allrows:
            row = [item.strip() for item in row]
            rows.append(row)
    return random.choice(rows)

#print(get_row("../params/orders.csv"))