class Planet():
    def __init__(self, ID, mass, radius, distance, tilt=0):
        self.mass = mass
        self.radius = radius
        self.distance = distance
        self.tilt = tilt
        self.ID = ID