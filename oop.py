class User:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def UpdateName(self, newName):
        self.name = newName

    def UpdateAge(self, newAge):
        self.age = newAge

    def Print(self):
        print("Name: " + self.name + " - Age: " + str(self.age))

user = User("Alisson", 12)
user.Print()

user.UpdateName("Gustavo")
user.UpdateAge(23)
user.Print()
