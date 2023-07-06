import sys
from tools import get_data, get_theta, normalize_denormalize


def main():
	T = get_theta()
	mileages, prices = get_data()
	try:
		mileage = float(input("Please enter a mileage:\n"))
	except ValueError:
		print("The mileage is not a number.")
		sys.exit(1)
	value = normalize_denormalize(mileage, mileages, prices, T[0], T[1])
	if value < 0:
		print("The mileage is too high, you cannot sell it.")
	else:
		print("This car worth " + str(int(value)) + "euros.")


if __name__ == "__main__":
	main()
