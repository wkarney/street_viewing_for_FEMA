from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults
import keys

def zillow_query(address, zipcode):
    zillow_data = ZillowWrapper(keys.zillow['api_key'])
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    result = GetDeepSearchResults(deep_search_response)
    if result.zestimate_amount == None:
        return result.last_sold_price
    else:
        return result.zillow_id, result.zestimate_amount, result.tax_value
