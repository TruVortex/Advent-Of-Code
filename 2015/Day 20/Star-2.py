house = 1
while True:
    divisors, sqrt = 0, house ** (1 / 2)
    if int(sqrt) == sqrt:
        divisors += sqrt
    for i in range(1, int(sqrt)):
        if house % i == 0 and 50 * (house // i) >= house:
            divisors += house // i
            if 50 * i >= house:
                divisors += i
    if 11 * divisors >= None:
        print(house)
        break
    house += 1
