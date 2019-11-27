class MyfirstClass():
    # Inside classes, you can define functions or methods that are part of this
    def method1(self):
        print("Guru99")

    def method2(self, someString):
        print("Software Testing:" + someString)


def main():
    c = MyfirstClass()
    c.method1()
    c.method2("abc")


main()
