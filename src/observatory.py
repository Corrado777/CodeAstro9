class Observatory():
    '''
    A class used to store information about an observatory.

    Attributes:
    -----------
    label : str
        The name or label of the observatory.
    latitude : float
        The latitude coordinate of the observatory in degrees.
    longitude : float
        The longitude coordinate of the observatory in degrees.
    altitude : float, optional
        The altitude of the observatory in meters above sea level (default is 0).

    Methods:
    --------
    __init__(label, latitude, longitude, altitude=0):
        Initializes the Observatory with the given label, latitude, longitude, and optional altitude.
    '''
    
    def __init__(self, label, latitude, longitude, altitude=0):
        self.label = label
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude