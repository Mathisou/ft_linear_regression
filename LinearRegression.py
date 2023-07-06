import matplotlib.pyplot as plt
import csv
import sys

from training import train
from tools import get_data, min_max_scaling

def main():
    mileages, prices = get_data()
    try:
        normalized_mileages = min_max_scaling(mileages)
        normalized_prices = min_max_scaling(prices)
        T0, T1 = train(normalized_mileages, normalized_prices)
    except ZeroDivisionError as e:
        print(e)
        sys.exit(1)
    with open('theta.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Theta"])
        writer.writerow([T0])
        writer.writerow([T1])


if __name__ == "__main__":
    main()
