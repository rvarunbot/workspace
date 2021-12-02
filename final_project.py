def get_name():
    name = input("what is your name: ")
    return name


def get_age():
    while True:
        age = int(input("what is your age: "))
        if (age > 0) and (age < 100):
            return age


def main():
    name = get_name()
    age = get_age()
    ttd = 100 - age
    print("{:>20} {:>5} {:>10}".format("name", "age", "years"))
    print("{:>20} {:>5} {:>10}".format(name, age, ttd))
    print("Done!")


main()
