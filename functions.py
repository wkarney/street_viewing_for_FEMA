"""
Functions for pulling data from APIs:
- Google Maps streetview data
- Zillow data on house prices and details
"""
import keys #API keys
import time

# Package imports for Zillow
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

# Package imports for Google Maps APIs
import google_streetview.api

# Google Maps functionality
def pull_streetview(location, size='640x480',
                    fov='90', pitch='0', radius='50',
                    key=keys.google['api_key']):
    '''
    Pulls streetview photos and saves data to ./streetview_images/
    returns streetview results.
    '''

    try:
        filename = location.replace(' ','_')
    except:
        filename = round(time.time(),0)
    params = [{
        'size': size,
    	'location': location,
        'fov': fov,
    	# 'heading': '',
    	'pitch': pitch,
        'radius': radius,
    	'key': keys.google['api_key']
    }]

    results = google_streetview.api.results(params)
    results.download_links(f'./streetview_images/{filename}')
    return results

# Zillow functionality
def zillow_query(address, zipcode):
    '''
    Given an address and zipcode as strings returns id, zestimate (or last sold price if zestimate unavilable), and latest tax appraisal value
    '''
    zillow_data = ZillowWrapper(keys.zillow['api_key'])
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    if result.zestimate_amount == None:
        return result.last_sold_price
    else:
        return result.zillow_id, result.zestimate_amount, result.tax_value
