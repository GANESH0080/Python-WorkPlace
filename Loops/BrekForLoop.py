def sampleForLoop():
    number = [3, 13, 14, 21, 10, 27, 35, 44, 78]
    for x in range(1, 7):
        print("The Numbers is", number[x])
        if (number[x] == 14):
            break
        print("The Break numbers is", number[x])
        if (number[x] % 2 == 0):
            continue
        print("the", number[x])


sampleForLoop()
