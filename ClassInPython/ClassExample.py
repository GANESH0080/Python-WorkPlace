class simpleClass():
    number = 30

    def method(self, num):
        simpleClass.number += 5

        return simpleClass.number


def main():
    c = simpleClass()
    print(c.method(25))


main()
