class Myclass():

    def mymethod(self):
        str = "Ganesh"
        print(str)

    def mymethod2(self, num):
        print(num)


def main():
    obj = Myclass()
    obj.mymethod()
    obj.mymethod2(25)


main()
