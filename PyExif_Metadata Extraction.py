from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def extract_geotagging_info(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Extract Exif data
        exif_data = img._getexif()

        if exif_data is not None:
            # Iterate through Exif data and look for GPSInfo tag
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                if tag_name == 'GPSInfo':
                    # Extract GPSInfo data
                    gps_info = {}
                    for gps_tag, gps_value in value.items():
                        tag_name = GPSTAGS.get(gps_tag, gps_tag)
                        gps_info[tag_name] = gps_value

                    return gps_info

    return None

def calculate_pixel_coordinates(gps_info, clicked_pixel_x, clicked_pixel_y):
    # Extract latitude, longitude, and altitude from GPSInfo
    latitude = gps_info.get('GPSLatitude')
    longitude = gps_info.get('GPSLongitude')

    # Implement the logic to convert latitude and longitude to pixel coordinates
    # ...

    return calculated_latitude, calculated_longitude

# Example usage
image_path = 'path/to/your/image.jpg'
clicked_pixel_x = 100  # Replace with actual clicked pixel coordinates
clicked_pixel_y = 150  # Replace with actual clicked pixel coordinates

gps_info = extract_geotagging_info(image_path)
if gps_info:
    calculated_latitude, calculated_longitude = calculate_pixel_coordinates(gps_info, clicked_pixel_x, clicked_pixel_y)
    print(f"Clicked Pixel Coordinates: ({clicked_pixel_x}, {clicked_pixel_y})")
    print(f"Calculated Latitude: {calculated_latitude}, Calculated Longitude: {calculated_longitude}")
else:
    print("No GPS information found in the image.")
