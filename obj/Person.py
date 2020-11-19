class Person():

    def details(self):
        print(self.name,self.age,self.children)

    def children_check(self):
        if self.children>0:
            print(f"{self.name} have children")
        else:
            print(f"{self.name} does not have any children")
