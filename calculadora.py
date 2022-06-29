result = open("result.txt", "a")
List = []
num1 = float
num2 = float
def calculator(num1, num2):
    num1 = float(input("Num1: "))
    num2 = float(input("Num2: "))
    operation = input("Operation(+, -, *, /, **): ")
    if operation == "+":
        print(num1 + num2)
        List.append(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
        List.append(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
        List.append(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
        List.append(num1 / num2)
    elif operation == "**":
        print(num1 ** num2)
        List.append(num1 ** num2)

while True:
    calculator(num1, num2)
    anotherCalculation = input("Another calculation?(y/n): ")
    if anotherCalculation == "n":
        break
string = str(List)
result.writelines(string)
