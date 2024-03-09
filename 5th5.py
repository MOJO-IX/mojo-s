for number in range(1,100):
    if number % 5 == 0 and number % 3 == 0:
        print("fizzbuzz ")
    elif number % 5 == 0:
        print("bizz ")
    elif number % 3 == 0:
        print("fizz ")
    else:
        print(number)