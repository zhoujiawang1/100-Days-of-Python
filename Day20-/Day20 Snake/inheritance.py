class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("in and out")


class Fish(Animal):

    def __init__(self):
        super().__init__()  # will inherit the animal

    def breathe(self):
        super().breathe()  # calls breathe from super class
        print("underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.breathe()
