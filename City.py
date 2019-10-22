from Degrees import obtain_distance_km


class City:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def distance(self, city):
        return obtain_distance_km(self, city)

    def __repr__(self):
        return "(" + str(self.lat) + "," + str(self.lon) + ")"
