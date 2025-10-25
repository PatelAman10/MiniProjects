n = int(input("How many numbers do you want to calculate? "))

numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = sum(numbers)

elif operation == "-":
    result = numbers[0]
    for num in numbers[1:]:
        result -= num

elif operation == "*":
    result = 1
    for num in numbers:
        result *= num

elif operation == "/":
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            print("Error: Division by zero!")
            break
        result /= num
    else:
        print("Result:", result)
        exit()

else:
    print("Invalid operation!")
    exit()

print("Result:", result)
