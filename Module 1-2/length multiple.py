# Write a Python function to reverses a string if it's length is a multiple of 4

a = input("Enter A:")


def reverse(a):
    if len(a) % 4 == 0:
        print(a[::-1])
    else:
        pass


reverse(a)
