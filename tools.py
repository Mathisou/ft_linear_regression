import csv, sys

def min_max_scaling(data):
    min_val = min(data)
    max_val = max(data)
    scaled_data = []
    for value in data:
        try:
            scaled_value = (value - min_val) / (max_val - min_val)
        except ZeroDivisionError:
            print("Can't divide by 0")
        scaled_data.append(scaled_value)
    return scaled_data


def normalize_denormalize(mileage, mileages, prices, theta0, theta1):
    min_mileage = min(mileages)
    max_mileage = max(mileages)
    min_price = min(prices)
    max_price = max(prices)
    if max_mileage == min_mileage:
        print("Cant divide par 0")
        sys.exit(1)
    normalize_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
    mileage = theta1 * normalize_mileage + theta0
    if mileage:
        denormalize_mileage = mileage * (max_price - min_price) + min_price
    else:
        denormalize_mileage = 0
    return denormalize_mileage

def get_theta():
    try:
        with open(r"theta.csv") as file:
            content = csv.reader(file)
            T = []
            for index, row in enumerate(content):
                if index != 0:
                    if len(row) != 1:
                        print("Data from .csv is incorrect. (Wrong number of data in a row)")
                        sys.exit(1)
                    T.append(float(row[0]))
    except(ValueError):
        print("Data from theta.csv is incorrect.")
        sys.exit(1)
    except(IOError):
        print("Can't open theta.csv file.")
        sys.exit(1)
    if len(T) != 2:
        print("Wrong number of thetas")
        sys.exit(1)
    return T

def get_data():
    try:
        with open(r"data.csv") as file:
            content = csv.reader(file)
            mileages = []
            prices = []
            for index, row in enumerate(content):
                if index != 0:
                    if len(row) != 2:
                        print("Data from data.csv is incorrect. (Wrong number of data in a row)")
                        sys.exit(1)
                    mileages.append(float(row[0]))
                    prices.append(float(row[1]))
    except(ValueError):
        print("Data from data.csv is incorrect.")
        sys.exit(1)
    except(IOError):
        print("Can't open data file. It should be named 'data.csv'.")
        sys.exit(1)
    if not len(mileages) > 0 and not len(prices) > 0:
        print("Invalid columns (not enough data).")
        sys.exit(1)
    return mileages, prices