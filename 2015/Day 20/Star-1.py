house = 1
while True:
    divisors, sqrt = 0, house ** (1 / 2)
    if int(sqrt) == sqrt:
        divisors += sqrt
    for i in range(1, int(sqrt)):
        if house % i == 0:
            divisors += i + house // i
    if 10 * divisors >= None:
        print(house)
        break
    house += 1
