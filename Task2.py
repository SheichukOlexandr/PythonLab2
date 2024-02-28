def main():
    x = float(input("Введіть x: "))
    epsilon = float(input("Введіть ε: "))

    n = 1
    a0 = x
    flag = False

    while n <= 10**2:
        an = a0 + 1 / (a0 + 1)
        if abs(an - a0) < epsilon:
            flag = True
            n_found = n
            an_found = an
            break  # Зупинити цикл, якщо умова досягнута
        a0 = an
        n += 1

    if flag:
        print(f"Перший член, який задовольняє умові: an = {an_found}, n = {n_found}")
    else:
        print("Членів, які задовольняють умові, не знайдено")

if __name__ == "__main__":
    main()
