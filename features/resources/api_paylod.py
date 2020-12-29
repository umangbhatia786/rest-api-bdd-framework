# Functions to return Payload for various API Methods
def params_payload():
    return {'key': 'qaclick123'}


def add_location_payload(input_lat, input_lng, name, contact, address):
    body_json = {
        "location": {
            "lat": input_lat,
            "lng": input_lng,
        },
        "accuracy": 50,
        "name": name,
        "phone_number": contact,
        "address": address,
        "types": [
            "shoe park",
            "shop"
        ],
        "website": "http://google.com",
        "language": "French-IN"
    }

    return body_json


def delete_location_payload(location_id):
    body_json = {
        "place_id": location_id
    }

    return body_json


def get_location_param(location_id):
    return {'key': 'qaclick123', 'place_id': location_id}


def update_location_payload(location_id, new_address):
    body_json = {
        "place_id": location_id,
        "address": new_address,
        "key": "qaclick123"
    }
