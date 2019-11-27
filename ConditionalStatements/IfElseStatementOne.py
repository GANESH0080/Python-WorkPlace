def SampleIfElse():
    num, num1 = 25, 35
    st = (num, "Is less than num1") if (num < num1) else print(num, "Is greater than num1")
    print(st)

SampleIfElse()
