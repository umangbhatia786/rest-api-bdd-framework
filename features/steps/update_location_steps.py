from behave import *
from features.configuration.config import *
from features.configuration.api_resources import GoogleAPIResources
from features.resources.api_paylod import *
import requests


@given(u'The Place Id of the location along with New Address as {new_address}')
def step_impl(context, new_address):
    context.my_config = get_config()
    context.update_loc_url = f'{context.my_config["API"]["endpoint"]}{GoogleAPIResources.update_location}'
    context.header = {'Content-Type': 'application/json'}
    context.validation_values = read_json_value_file()
    context.param = get_location_param(context.validation_values[0])
    context.update_payload = update_location_payload(context.validation_values[0], new_address)


@when(u'We execute the Update Location API method')
def step_impl(context):
    context.response = requests.put(
        url=context.update_loc_url,
        params=context.param,
        headers=context.header,
        json=context.update_payload
    )

