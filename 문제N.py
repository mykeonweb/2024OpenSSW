# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def calculate_y(a, b, max_x):
    for x in range(max_x + 1):
        y = a * x ** 2 + b
        print(f"{a} x {a} x {x} + {y}")


def main():
    a = float(input("a값 input 'a': "))
    b = float(input("b값 input 'b': "))
    max_x = int(input("Enter the maximum value of 'X': "))

    calculate_y(a, b, max_x)


if __name__ == "__main__":
    main()
