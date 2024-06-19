from geopy.geocoders import Nominatim as nm
def get_location(location_name):
    locator = nm(user_agent="myGeocoder")
    location = locator.geocode(location_name) #will be a json object
    return location

#print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

'''location.raw,location.point,location.longitude,location.latitude,location.altitude,location.address
the above lines will give the informstion that is available in the json object'''

