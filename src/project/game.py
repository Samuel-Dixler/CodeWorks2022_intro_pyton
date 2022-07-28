
class Character:
    char = {}

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Character.char.update({'name': self.name})
        Character.char.update({'position': self.position})

    def move(self):
        pass

class Hero(Character):
    def move(self):
        x = 5
        self.position = int(self.position) + x
        Character.char.update({'position': self.position})
        return self.position


class Villain(Character):
    def move(self):
        x = 5
        self.position = int(self.position) - x
        Character.char.update({'position': self.position})
        return self.position

h = Hero("Sam", 10)
print(h.move())
print(Character.char)
