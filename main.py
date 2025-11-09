from app.calculator import add, sub, multi, div

def main():
    num = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

    print(f"Addition: {num} + {num2} = {add(num, num2)}")
    print(f"Subtraction: {num} - {num2} = {sub(num, num2)}")
    print(f"Multiplication: {num} * {num2} = {multi(num, num2)}")
    print(f"Division: {num} / {num2} = {div(num, num2)}")

if __name__ == "__main__":
    main()
