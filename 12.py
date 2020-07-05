try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10/0


except ValueError:
    print("invalid input")
except ZeroDivisionError as err:
    print("Divided by zero")
    print(err)
