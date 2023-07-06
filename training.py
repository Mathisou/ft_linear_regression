def estimatePrice(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def train_theta0(theta0, theta1, mileages, prices, learningRate):
    tmpTheta0 = learningRate * (1/len(mileages))
    error_sum = 0
    for i in range(len(mileages)):
        error_sum += estimatePrice(theta0, theta1, mileages[i]) - prices[i]
    return tmpTheta0 * error_sum


def train_theta1(theta0, theta1, mileages, prices, learningRate):
    tmpTheta1 = learningRate * (1/len(mileages))
    error_sum = 0
    for i in range(len(mileages)):
        error_sum += (estimatePrice(theta0, theta1, mileages[i]) - prices[i]) * mileages[i]
    return tmpTheta1 * error_sum


def train(mileages, prices):
    generation = 300
    learningRate = 0.5
    theta0 = 0.0
    theta1 = 0.0
    for i in range(generation):
        tmpTheta0 = train_theta0(theta0, theta1, mileages, prices, learningRate)
        tmpTheta1 = train_theta1(theta0, theta1, mileages, prices, learningRate)
        theta0 -= tmpTheta0
        theta1 -= tmpTheta1
    return theta0, theta1
