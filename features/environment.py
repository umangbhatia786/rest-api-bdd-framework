from features.configuration.config import *
from features.configuration.api_resources import GoogleAPIResources
from features.resources.api_paylod import *
import requests


def after_all(context):
    """Hook To Delete a Location after all API Methods have been executed"""
    context.my_config = get_config()
    context.validation_values = read_json_value_file()
    context.header = {'Content-Type': 'application/json'}
    context.response = requests.post(
            url=f'{context.my_config["API"]["endpoint"]}{GoogleAPIResources.delete_location}',
            json=delete_location_payload(context.validation_values[0]),
            headers=context.header,
            params=params_payload()
        )
    assert context.response.status_code == 200, 'Location Deletion failed'
