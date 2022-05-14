from armes import Arms

class Enemie_fire(Arms):
    def __init__(self, name, damage, image, animation, velocity, person_position, constructor):
        super().__init__(name, damage, image, animation, velocity, person_position, constructor)
