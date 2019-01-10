# Complete the minimumLoss function below.


def minimumLoss(price):
    min_loss = 10 ** 16
    num_prices = len(price)
    prices_dict = {}
    for i in range(num_prices):
        prices_dict[price[i]] = i
    sorted_price = sorted(price)
    for i in range(1, num_prices):
        if prices_dict[sorted_price[i]] < prices_dict[sorted_price[i - 1]]:
            difference = sorted_price[i] - sorted_price[i - 1]
            if difference < min_loss:
                min_loss = difference
    return min_loss


def minimumLoss_timeout(price):
    min_loss = 10 ** 16
    num_prices = len(price)
    sorted_price = sorted(price)
    for i in range(1, num_prices):
        if price.index(sorted_price[i]) < price.index(sorted_price[i - 1]):
            difference = sorted_price[i] - sorted_price[i - 1]
            if difference < min_loss:
                min_loss = difference
    return min_loss


if __name__ == '__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)
    print(result)
