class Myclass():

    def mymethod(self):
        str = "Ganesh"
        print(str)

    def mymethod2(self,num,str):
        print(num,str)
        print(num,"\n"+str)

def main():
    obj = Myclass()
    obj.mymethod()
    obj.mymethod2(25,'Salunkhe')


main()
