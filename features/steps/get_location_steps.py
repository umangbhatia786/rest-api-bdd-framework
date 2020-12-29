from behave import *
from features.configuration.config import *
from features.configuration.api_resources import GoogleAPIResources
from features.resources.api_paylod import *
import requests


@given(u'The Place Id of the desired location')
def step_impl(context):
    context.my_config = get_config()
    context.get_loc_url = f'{context.my_config["API"]["endpoint"]}{GoogleAPIResources.get_location}'
    context.header = {'Content-Type': 'application/json'}
    context.validation_values = read_json_value_file()
    context.param = get_location_param(context.validation_values[0])


@when(u'We execute the Get Location API method')
def step_impl(context):
    context.response = requests.get(
        url=context.get_loc_url,
        headers=context.header,
        params=context.param
    )


@then(u'The Response Body has correct details for the given location')
def step_impl(context):
    response_json = context.response.json()
    assert response_json['location']['latitude'] == context.validation_values[1], 'Latitude is not same as given'
    assert response_json['location']['longitude'] == context.validation_values[2], 'Longitude is not same as given'
