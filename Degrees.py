from math import sin, cos, sqrt, atan2, radians
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# approximate radius of earth in km
R = 6373.0


def obtain_distance_km(city_A, city_B):
    lat1 = radians(city_A.lat)
    lon1 = radians(city_A.lon)
    lat2 = radians(city_B.lat)
    lon2 = radians(city_B.lon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
