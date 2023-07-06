from tools import get_data, get_theta, normalize_denormalize
import sys

def calculate_accuracy(mileages, prices, T0, T1):
    if T0 and T1:
        length = len(prices)
        mean = sum(prices) / length
        total_sum = 0
        estimated_sum = 0
        for i in range(length):
            total_sum += pow(prices[i] - mean, 2)
            estimated = normalize_denormalize(mileages[i], mileages, prices, T0, T1)
            estimated_sum += pow(prices[i] - estimated, 2)
        try:
            coeff = 1 - (estimated_sum / total_sum)
        except ZeroDivisionError:
            print("Error: The csv file with data seems to be empty.")
            sys.exit(1)
        return coeff
    return 0.0


def main():
    mileages, prices = get_data()
    T = get_theta()
    accuracy = calculate_accuracy(mileages, prices, T[0], T[1])
    print("The accuracy of the algorithm is {}%.".format(round(accuracy * 100)))

if __name__ == "__main__":
    main()