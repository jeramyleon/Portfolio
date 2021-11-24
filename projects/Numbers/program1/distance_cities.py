# Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding 
# coordinates for the cities like latitude and longitude.
from geopy.geocoders import Nominatim
from geopy import distance 
import numbers

def calculate_distance(city_a, city_b, unit):
    for par in [city_a, city_b, unit]:
        if isinstance(par, str) == False:
            print("Wrong input")
            return False

    geolocator = Nominatim(user_agent = 'calculate_distance')
    location1 = geolocator.geocode(city_a)
    location2 = geolocator.geocode(city_b)

    location1coor = (location1.latitude, location1.longitude)
    location2coor = (location2.latitude, location2.longitude)


    distance = eval("distance.distance(location1coor, location2coor)." + unit)

    print("The distance from %s to %s is %f %s." % (city_a, city_b, distance, unit)) 
    return distance   

# feet, kilometers, meters, miles, nautical miles 
calculate_distance("new york", "san juan", 'miles')




