"""
This file contains functions used within the SightVisit application, including:
Functions for pulling and utilizing metadata in imagery
Functions for pulling external data from APIs:
- Google Maps streetview data
- Google reverse geocode/address lookup functionality
- Zillow data on house prices and details
"""
# import keys  # API keys

# Package imports for dealing with images
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Package imports for Zillow
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

# Package imports for Google Maps APIs
import google_streetview.api

# Geocoding and reverse Geocoding
from pygeocoder import Geocoder

# Imagery functionality
def get_gps_details(img):
    """Function for extracting GPS data from image

    Args:
        img (.jpeg / .png et al.): an image file

    Returns:
        Dictionary with following key: value pairs:
            'GPSLatitudeRef': str = 'N' or 'S'
            'GPSLatitude': tuple of tuples,
            'GPSLongitudeRef': str = 'E' or 'W',
            'GPSLongitude': tuple of tuples,
            'GPSAltitudeRef': byte string,
            'GPSAltitude': tuple,
            'GPSTimeStamp': tuple of tuples,
            'GPSSpeedRef': str,
            'GPSSpeed': tuple,
            'GPSImgDirectionRef': str,
            'GPSImgDirection': tuple,
            'GPSDestBearingRef': str,
            'GPSDestBearing': tuple,
            'GPSDateStamp': str representing datetime,
            'GPSHPositioningError': tuple}
    """
    gpsinfo = {}
    exif = {TAGS[k]: v for k, v in img._getexif().items() if k in TAGS}
    for item in exif['GPSInfo'].keys():
        name = GPSTAGS.get(item, item)
        gpsinfo[name] = exif['GPSInfo'][item]
    return gpsinfo


def convert_to_degress(coords):
    """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format

    Credit should be provided to Shadab Zafar; see his GitHub at
    https://gist.github.com/dufferzafar/f455099332ade457599cf97070a930b6

    Args:
        coords (tuple): coordinates in degrees as nested tuple, where tuple[0] corresponds with hours, tuple[1] corresponds with minutes, and tuple[2] (optional) corresponds with seconds

    Returns:
        (float): coordinates as float number
    """
    deg_num, deg_denom = coords[0]
    d = float(deg_num) / float(deg_denom)
    min_num, min_denom = coords[1]
    m = float(min_num) / float(min_denom)
    try:
        sec_num, sec_denom = coords[2]
        s = float(sec_num) / float(sec_denom)
    except:
        s = 0
    return d + (m / 60.0) + (s / 3600.0)


def get_img_coord_str(img):
    """Function for extracting latitude, longitude coordinates from image as string result

    Args:
        img (.jpeg / .png et al.): an image file

    Returns:
        (str): GPS coordinates as 'latitude,longitude'
    """

    lat = convert_to_degress(get_gps_details(img)['GPSLatitude'])
    if get_gps_details(img)['GPSLatitudeRef'] == 'S':
        lat = -lat

    longitude = convert_to_degress(get_gps_details(img)['GPSLongitude'])
    if get_gps_details(img)['GPSLongitudeRef'] == 'W':
        longitude = -longitude

    return str(lat) + ',' + str(longitude)


def get_img_coord_tuple(img):
    """Function for extracting latitude, longitude coordinates from image as numerical result

    Args:
        img (.jpeg / .png et al.): an image file

    Returns:
        (tuple): latitude and logitudes coordinates as floats
    """

    lat = convert_to_degress(get_gps_details(img)['GPSLatitude'])
    if get_gps_details(img)['GPSLatitudeRef'] == 'S':
        lat = -lat

    longitude = convert_to_degress(get_gps_details(img)['GPSLongitude'])
    if get_gps_details(img)['GPSLongitudeRef'] == 'W':
        longitude = -longitude

    return lat, long


# Google Maps streetview functionality
def pull_streetview(location,
                        size='640x480',
                        fov='90',
                        pitch='0',
                        radius='50',
                        key='YOURAPIKEYHERE',
                        heading=None):
    """Function for obtaining google streetview image for a given location (either address or latitude,longitude; formated as str)

    Args:
        location (str): location either as address or lat./long.

        size (str): (default='(640x480)') size of the outputted image in pixels

        fov (str): (default='90')

        ptich (str): (default='0')

        key (str): (default='YOURAPIKEYHERE') google streetview api key

        heading (str): (default=None)

    Returns:
        url with most recent google streetview photo
    """
    try:
        filename = location.replace(' ', '_')
    except:
        filename = round(time.time(), 0)
    params = [{
        'size': size,
        'location': location,
        'fov': fov,
        'pitch': pitch,
        'radius': radius,
        'key': key
    }]
    if heading != None:
        params[0]['heading'] = heading

    results = google_streetview.api.results(params)
    results.download_links('./app/img')


def reverse_lookup(lat, long, key='YOURAPIKEY'):
    """Function for lookup of addresses from latitude, longitude details using Google Maps API

    Args:
        lat (float): latitude as float

        long (float): longitude as float

        key (str): (default='YOURAPIKEYHERE') google maps api key

    Returns:
        returns a tuple with address (str), zipcode (str)
        """
    result = str(Geocoder(api_key=key).reverse_geocode(lat, long))
    location_details = result.split(",")
    address = location_details[0]
    zipcode = location_details[-2][-5:]
    return address, zipcode


# Zillow functionality
def zillow_query(address, zipcode, key='YOURAPIKEYHERE'):
    """Function for obtaining data for a given address location

    Args:
        address (str): street address

        zipcode (str): zipcode corresponding with street address

        key (str): (default='YOURAPIKEYHERE') zillow api key

    Returns:
        returns a GetDeepSearchResults object which has following attributes available:
            'zillow_id'
            'home_type'
            'home_detail_link'
            'graph_data_link'
            'map_this_home_link'
            'latitude'
            'longitude'
            'tax_year'
            'tax_value'
            'year_built'
            'property_size'
            'home_size'
            'bathrooms'
            'bedrooms'
            'last_sold_date'
            'last_sold_price'
            'zestimate_amount'
            'zestimate_last_updated'
            'zestimate_value_change'
            'zestimate_valuation_range_high'
            'zestimate_valuationRange_low'
            'zestimate_percentile'
    """
    zillow_data = ZillowWrapper(key)
    deep_search_response = zillow_data.get_deep_search_results(
        address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    return result
