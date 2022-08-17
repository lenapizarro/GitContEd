print ("Hola mundo")

print("Enter an option from the menu")
print("1. SUM")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


selection = int(input())

number1 = int(input('Enter the first number'))
number2 = int(input('Enter the second number'))

if selection == 1:

    print(number1 + number2)

elif selection == 2:

    print(number1 - number2)

elif selection == 3:

    print(number1 * number2)

elif selection == 4:

    if number1 < number2:
        print("The second number cannot be greater than the first number in division")
    else:
        print(number1 / number2)
else:

    print("Your selection is not listed in the options")