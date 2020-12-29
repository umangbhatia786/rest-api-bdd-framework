from behave import *
from features.configuration.config import *
from features.configuration.api_resources import GoogleAPIResources
from features.resources.api_paylod import *
import requests


@given(u'The Location Details with {lat}, {lng}, {name}, {contact} and address as {address}')
def step_impl(context, lat, lng, name, contact, address):
    context.my_config = get_config()
    context.add_loc_url = f'{context.my_config["API"]["endpoint"]}{GoogleAPIResources.add_location}'
    context.header = {'Content-Type': 'application/json'}
    context.add_loc_payload = add_location_payload(lat, lng, name, contact, address)


@when(u'We execute the AddLocation API method')
def step_impl(context):
    context.response = requests.post(
        url=context.add_loc_url,
        params=params_payload(),
        json=context.add_loc_payload,
        headers=context.header
    )


@then(u'Response Status Code is {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, 'Response Code is not 200'


@then(u'Status Message is Ok')
def step_impl(context):
    response_json = context.response.json()
    create_json_value_file(response_json['place_id'], context.add_loc_payload['location']['lat'], context.add_loc_payload['location']['lng'])
    assert response_json['status'] == 'OK', 'Response Status is not Ok, Assertion Failed!'
