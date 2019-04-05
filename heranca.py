class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age    #public
        self._year = 1990 #protected (acessível de qualquer maneira, não entendi a usabilidade)
        self.__year2 = 20 #private (não acessível de outros arquivos, somente através de getters e setters, feitos à mão, estilo java)

    def MakeSound(self):
        print("Hello, my name is: " + self.name)

    def SetYear(self, newYear):
        self.__year2 = newYear

class Dog(Animal):
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy

    def MakeSound(self):
        print("Hoof")

    def Play(self):
        print(self.toy)

animal = Animal("Rubert", 13)
animal.MakeSound()
print(animal._year)

animal = Dog("Juriscreito", 3, "Ball")
animal.MakeSound()
animal.Play()