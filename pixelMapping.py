def convert_coordinates_to_pixels(gps_info, latitude, longitude, image_width, image_height):
    # Extract latitude and longitude of the image center
    center_latitude = gps_info.get('GPSLatitude')[0]  # Assuming degrees, minutes, seconds format
    center_longitude = gps_info.get('GPSLongitude')[0]  # Assuming degrees, minutes, seconds format

    # Calculate the pixel coordinates of the image center (assuming linear projection)
    center_pixel_x = int((longitude - center_longitude) * pixels_per_degree_longitude + image_width / 2)
    center_pixel_y = int((latitude - center_latitude) * pixels_per_degree_latitude + image_height / 2)

    # Calculate the pixel coordinates of the given latitude and longitude
    target_pixel_x = int((longitude - center_longitude) * pixels_per_degree_longitude + center_pixel_x)
    target_pixel_y = int((latitude - center_latitude) * pixels_per_degree_latitude + center_pixel_y)

    return target_pixel_x, target_pixel_y

# Example usage
latitude = 37.7749  # Replace with actual latitude
longitude = -122.4194  # Replace with actual longitude

# Assuming the image dimensions and pixel resolution per degree
image_width = 800
image_height = 600
pixels_per_degree_longitude = 10  # Adjust based on your image
pixels_per_degree_latitude = 10  # Adjust based on your image

# Example: Calculate pixel coordinates for the given latitude and longitude
gps_info = {'GPSLatitude': [37.7749], 'GPSLongitude': [-122.4194]}  # Replace with actual GPS info
target_pixel_x, target_pixel_y = convert_coordinates_to_pixels(gps_info, latitude, longitude, image_width, image_height)

print(f"Latitude: {latitude}, Longitude: {longitude}")
print(f"Target Pixel Coordinates: ({target_pixel_x}, {target_pixel_y})")
