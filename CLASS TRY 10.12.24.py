class Festival:
    def __init__(self, Xmas, Newyear):
        self.Xmas = Xmas
        self.Newyear = Newyear

    def display(self):
        print(f"December: {self.Xmas}\nJanuary: {self.Newyear}")


class Things:
    def __init__(self, Tree, Star):
        self.Tree = Tree
        self.Star = Star

    def Decoration(self):
        print(f"Christmas: {self.Tree}\nNew Year: {self.Star}")


class Sweet(Festival, Things):
    def __init__(self, Xmas, Newyear, Tree, Star, cookies, cake):
        Festival.__init__(self, Xmas, Newyear)
        Things.__init__(self, Tree, Star)
        self.cookies = cookies
        self.cake = cake

    def sweet_feast(self):
        self.display()
        self.Decoration()
        print(f"Christmas: {self.cookies}\nNew Year: {self.cake}")



xmas = input("Enter the Christmas festival name: ")
newyear = input("Enter the New Year festival name: ")
tree = input("Enter the decoration for Christmas: ")
star = input("Enter the decoration for New Year: ")
cookies = input("Enter the Christmas sweet: ")
cake = input("Enter the New Year sweet: ")


s = Sweet(xmas, newyear, tree, star, cookies, cake)
s.sweet_feast()
