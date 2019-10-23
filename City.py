from Degrees import obtain_distance_km


class City:
    def __init__(self, lat, lon, name, state):
        self.name = name
        self.state = state
        self.lat = lat
        self.lon = lon

    def distance(self, city):
        return obtain_distance_km(self, city)

    def __repr__(self):
        return self.name + "," + self.state + "," + str(self.lat) + "," + str(self.lon)
    
    def csv_representation(self):
        return self.name + "," + self.state + "," + str(self.lat) + "," + str(self.lon)
