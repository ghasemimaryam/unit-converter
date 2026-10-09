def main():
    while True:
        print()
        print("=== Mini Program ===")
        print("1) Kilometers to miles")
        print("2) Miles to kilometers")
        print("3) Kilograms to pounds")
        print("4) Celsius to Fahrenheit")
        print("5) Even or odd")
        print("6) Exit")
        choice = input("Choose: ")

        try:
            if choice == "1":
                km = float(input("Enter the distance in kilometers: "))
                print(km_to_miles(km))
            elif choice == "2":
                miles = float(input("Enter the distance in miles: "))
                print(miles_to_km(miles))
            elif choice == "3":
                kg = float(input("Enter the weight in kilograms: "))
                print(kg_to_pounds(kg))
            elif choice == "4":
                c = float(input("Enter the temperature in Celsius: "))
                print(celsius_to_fahrenheit(c))
            elif choice == "5":
                n = int(input("Enter a whole number: "))
                print(f"{n} is {even_or_odd(n)}")
            elif choice == "6":
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")


def km_to_miles(km):
    return km * 0.621371


def miles_to_km(miles):
    return miles / 0.621371


def kg_to_pounds(kg):
    return kg * 2.20462


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    return "odd"


main()
