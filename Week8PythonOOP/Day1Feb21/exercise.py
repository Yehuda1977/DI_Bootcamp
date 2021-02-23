class Human():
    def __init__(self, name, eye_color, age):
        print("A new human was born")
        self.name = name
        self.eye_color = eye_color
        self.age = age
    def introduce(self):
        print(f"{self.name} is {self.age} years old and has {self.eye_color} eyes")
        

matt = Human("Matt", "silver", 43)
bill = Human("Bill", 'crayon', 43)

matt.introduce()



