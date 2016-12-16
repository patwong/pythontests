import sc2

class SomeClass(sc2.SomeClass):
    sc1 = 12

    def hw(self):
        return "hello world"

def main():
    x = SomeClass()
    print (x.hw())
    print (x.sc2)

main()
