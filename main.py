first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

try:
    division_result = float(first_num) / float(second_num)
    print(division_result)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Not int value")
finally:
    print("End.")
