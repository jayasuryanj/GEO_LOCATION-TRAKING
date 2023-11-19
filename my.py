from geopy.geocoders import Nominatim

#create the geolocator object with a useragent
geolocator = Nominatim(user_agent="geoapiExersize")
place = input("Enter the city Name: ") #get ther city name

location = geolocator.geocode(place)
if location:
    # Extract latitude and longitude
    latitude, longitude = location.latitude, location.longitude

print(location)
print(f"Latitude: {latitude}, Longitude: {longitude}")

    # Generate Google Maps link
google_maps_link = f"https://www.google.com/maps/place/{latitude},{longitude}"
print(f"Google Maps Link: {google_maps_link}")