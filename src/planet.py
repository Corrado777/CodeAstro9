class Planet():
    '''
    A class used to represent a planet with various attributes.

    Attributes:
    -----------
    label : str
        The name or label of the planet (default is 'None').
    period : float
        The orbital period of the planet (default is 0.0).
    radius : float
        The radius of the planet (default is 0.0).
    distance : float
        The distance of the planet from its star or another reference point (default is 0.0).
    tilt : float
        The axial tilt of the planet (default is 0.0).
    ra : float
        The right ascension coordinate of the planet in degrees (default is 0.0).
    dec : float
        The declination coordinate of the planet in degrees (default is 0.0).

    Methods:
    --------
    __init__():
        Initializes the Planet with default attributes.
    '''
    def __init__(self):
        self.label = 'None'
        self.period = 0.
        self.radius = 0.
        self.distance = 0.
        self.tilt = 0.
        self.ra = 0.
        self.dec = 0.
        