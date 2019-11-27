class Myclass():
    str = "Hello Ganesh"

    def mymethod(self):
        print(Myclass.str)


def main():
    obj = Myclass()
    obj.mymethod()


main()
