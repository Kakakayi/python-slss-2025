# Boilerplate
# Karina Luo
# Nov 14


def age_2049(age: int) -> int:
    # calculate age
    return 2049 - 2025 + age


def olympic_average(a: float, b: float, c: float, d: float, e: float) -> float:
    # add up and return
    return (a + b + c + d + e) / 5


def McDonalds(fries: str, burger: str) -> float:
    # if want fries, total + 3
    total = 0
    if fries.lower() == "yes":
        total += 3
    if burger.lower() == "yes":
        total += 5

    return total * 1.14


def main():
    # age = int(input("How old are you now?"))
    # print(f"In 2049 you would be {age_2049(age)} years old!")
    print("What did the 5 judges give you on Olympics?\n")
    a = float(input("Judge 1: "))
    b = float(input("Judge 2: "))
    c = float(input("Judge 3: "))
    d = float(input("Judge 4: "))
    e = float(input("Judge 5: "))
    print(f"Your Olumpic score is {olympic_average(a, b, c, d, e)}!!!")
    burger = input("Would you like a burger for $5?")
    fries = input("Would you like fries for $3?")
    print(f"Your total is {McDonalds(fries, burger)}")


if __name__ == "__main__":
    main()
