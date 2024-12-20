def invest(amount: float, rate: float, years: int) -> float:
    for year in range(years):
        amount += amount * rate
        print(f"year {year + 1}: ${amount:.2f}")

    return amount

amount = float(input("Enter initial amount: "))
rate = float(input("Enter percentage rate: "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)