# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
import re
if __name__ == '__main__':
    print_hi('PyCharm')
def calculator():
    try:
        z = re.match("^(\d+[.,]?\d*)(\+|-|\*|\/)(\d+[.,]?\d*)$", '21+55').groups()
        ('5.12', '+', '6.43')
        a = list(z)
        a[0], a[2] = float(a[0]), float(a[2])
        if '+' in a:
            return a[0] + a[2]
        elif '-' in a:
            return a[0] + a[2]
        elif '*' in a:
            return a[0] * a[2]
        elif '/' in a:
            return a[0] / a[2]
        return a
    except:
        print("непонимаю")
print(calculator())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
