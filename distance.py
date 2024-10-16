from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(zip_code):
    geolocator = Nominatim(user_agent="zip_distance_calculator")
    location = geolocator.geocode(zip_code)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not find coordinates for ZIP code: {zip_code}")
        
#calculate distance
def calculate_distance(zip_code1, zip_code2):
    try:
        coords_1 = get_coordinates(zip_code1)
        coords_2 = get_coordinates(zip_code2)
        
        distance = geodesic(coords_1, coords_2).miles  # You can use .km for kilometers
        return distance
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    zip_code1 = input("Enter the first ZIP code: ")
    zip_code2 = input("Enter the second ZIP code: ")
    
    distance = calculate_distance(zip_code1, zip_code2)
    print(f"The distance between {zip_code1} and {zip_code2} is {distance:.2f} miles.")
