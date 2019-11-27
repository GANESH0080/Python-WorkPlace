def main():
    # use the break and continue statements
    for x in range(10, 21):
        if (x == 15): break
    print("numbers", x)
    for x in range(x, 21):
        if (x % 5 == 0):
            print("Divisible by 5", x)


main()
