class AClass:
    the_dict = {}

    def displayprops(self):
        print(self.name
    def keyfinder(self,k1):
        if k1 in the_dict:
            print(k1 + " is in the dictionary")
        else:
            print(k1 + ": not found")

    def __init__(self, name, salary):
        self.the_dict['name'] = "AClass"

#end keyfinder

ac1 = AClass("hi", 200)
# ac1.keyfinder('name')
print( ac1)
