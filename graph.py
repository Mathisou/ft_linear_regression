import matplotlib.pyplot as plt
from tools import get_data, get_theta


def main():
	T = get_theta()
	mileages, prices = get_data()
	plt.scatter(mileages, prices, s=10)
	if T[0] != 0.0 and T[1] != 0.0:
		min_mileage = min(mileages)
		max_mileage = max(mileages)
		min_price = min(prices)
		max_price = max(prices)
		line_mileages = [min_mileage, max_mileage]
		line_prices = []
		for mileage in line_mileages:
			try:
				normalize_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
			except ZeroDivisionError:
				print("Cant divide par 0")
			mileage = T[1] * normalize_mileage + T[0]
			if mileage:
				denormalize_mileage = mileage * (max_price - min_price) + min_price
			else:
				denormalize_mileage = 0
			line_prices.append(denormalize_mileage)

		plt.plot(line_mileages, line_prices, color='red', label='Estimated Price')
	plt.ylabel("Price")
	plt.xlabel("Mileage")
	plt.grid(True)
	plt.show()


if __name__ == "__main__":
	main()
