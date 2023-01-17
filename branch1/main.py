# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculation(a, b):

    for i in range(a):
        for j in range(b):
            print(i+j, end=' ')
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Choose the lenght and height of matrix")
    a, b = int(input()), int(input())
    calculation(a, b)

