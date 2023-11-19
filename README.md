# GEO_LOCATION-TRAKING


1. **Importing the necessary library:**
   ```python
   from geopy.geocoders import Nominatim
   ```
   This line imports the `Nominatim` class from the `geopy.geocoders` module. `Nominatim` is a geocoding service provided by OpenStreetMap.

2. **Creating the geolocator object:**
   ```python
   geolocator = Nominatim(user_agent="geoapiExersize")
   ```
   Here, an instance of the `Nominatim` class is created with a specified user agent ("geoapiExersize"). The user agent is a unique identifier for your application when making requests to the geocoding service.

3. **Getting the city name from the user:**
   ```python
   place = input("Enter the city Name: ")
   ```
   This line prompts the user to enter the name of a city, and the input is stored in the `place` variable.

4. **Getting the location information:**
   ```python
   location = geolocator.geocode(place)
   ```
   The `geocode` method is called with the provided city name (`place`) to get the location information. The result is stored in the `location` variable.

5. **Checking if location is found:**
   ```python
   if location:
   ```
   This conditional statement checks if the `location` variable is not `None`, meaning that a valid location was found.

6. **Extracting latitude and longitude:**
   ```python
   latitude, longitude = location.latitude, location.longitude
   ```
   If a location is found, this line extracts the latitude and longitude from the `location` object.

7. **Printing latitude and longitude:**
   ```python
   print(f"Latitude: {latitude}, Longitude: {longitude}")
   ```
   The latitude and longitude are printed to the console.

8. **Generating Google Maps link:**
   ```python
   google_maps_link = f"https://www.google.com/maps/place/{latitude},{longitude}"
   ```
   A Google Maps link is constructed using the latitude and longitude values.

9. **Printing Google Maps link:**
   ```python
   print(f"Google Maps Link: {google_maps_link}")
   ```
   The Google Maps link is printed to the console.

10. **Handling case when location is not found:**
    ```python
    else:
        print("Location not found.")
    ```
    If the geocoding operation did not return a valid location (i.e., `location` is `None`), this message is printed to the console.

This code essentially takes a city name as input, uses the `geopy` library to obtain the corresponding geographical coordinates, prints the latitude and longitude, and generates a Google Maps link for the location. If the location is not found, it indicates that to the user.
